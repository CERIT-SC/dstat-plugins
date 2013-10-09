# Dstat Plugins

Additional plugins for dstat (http://dag.wieers.com/home-made/dstat/)

# List of Plugins

### NUMA policy statistics

Displays NUMA policy hit/miss statistics

Example:

    $ dstat --numastat -f
    ---------------node/0------------------------------node/1--------------
     hit   miss  frgn  int   loc   oth : hit   miss  frgn  int   loc   oth 
    1439k    0     0     0  1439k    0 :1488k    0     0     0  1488k    0 
    1438k    0     0     0  1438k    0 :1481k    0     0     0  1481k    0 
    1470k    0     0     0  1470k    0 :1255k    0     0     0  1255k    0 
     116k    0     0     0   116k    0 :  29k    0     0     0    29k    0 
       4     0     0     0     4     0 :   0     0     0     0     0     0 
       2     0     0     0     2     0 :   0     0     0     0     0     0 

***

CERIT Scientific Cloud, <support@cerit-sc.cz>
