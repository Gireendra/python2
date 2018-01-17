#! /usr/bin/python
def find_element(l,x):
    i=0
    if x in l:
        s=l.index(x)
        return s
    return -1    
print find_element([1,2,3],3)
