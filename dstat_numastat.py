### Author: Vlastimil Holer <xholer@mail.muni.cz>

class dstat_plugin(dstat):
    """
    Numa policy hit/miss statistics.
    https://www.kernel.org/doc/Documentation/numastat.txt
    """

    def __init__(self):
        self.vars_ = ('numa_hit','numa_miss','numa_foreign','interleave_hit','local_node','other_node')
        self.nick = ('hit','miss','frgn','int','loc','oth')
        self.cols = len(self.nick)
        self.type = 'd'
        self.scale = 1000
        self.nodefilter = re.compile('node/node(\d+)/numastat$')

    def discover(self, *objlist):
        ret = []
        for numastat in glob.glob('/sys/devices/system/node/node*/numastat'):
            match = self.nodefilter.search(numastat)
            if match:
                ret.append(match.group(1))
        for item in objlist:
            ret.append(item)
        if not ret:
            raise Exception, 'System does not provide any numastat'
        return ret

    def vars(self):
        if not op.full:
            return ['total']
        else:
            return self.discover

    def name(self):
        return ['node/'+nodeid for nodeid in self.vars]

    def extract(self):
        for name in self.vars:
            self.set2[name] = len(self.set2[name]) * [0]
        for nodeid in self.discover:
            for line in dopen('/sys/devices/system/node/node%s/numastat' % (nodeid,)).readlines():
                (key, value) = line.split()
                index = self.vars_.index(key)
                if nodeid in self.set2:
                    self.set2[nodeid][index] = long(value)
                self.set2['total'][index] = self.set2['total'][index] + long(value)

        for name in self.set2.keys():
            for i in range(len(self.nick)):
                self.val[name][i] = (self.set2[name][i] - self.set1[name][i]) / elapsed
        if step == op.delay:
            self.set1.update(self.set2)

# vim:ts=4:sw=4:et
