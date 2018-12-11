'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list
'''

def tower_builder(n_floors):
    tower = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        tower.append(' '*n + '*'*(i*2+1) + ' '*n)
    
    return tower