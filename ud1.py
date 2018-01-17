#! /usr/bin/python
def find_element(l,x):
    u=0
    while u<len(l):
        if l[u]==x:
            return u
        u=u+1
    return -1
        
        
print find_element([1,2,3],3)
