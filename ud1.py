#! /usr/bin/python
def find_element(l,x):
    u=0
    v=-1
    for i in l:
        if i==x:
            break
        u =u+1
    if u<len(l):
        return u
    else:
        return v
        
        
print find_element([1,2,3],3)
           #>>> 2
print find_element(['alpha','beta'],'gamma')
