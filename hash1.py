#! /usr/bin/python
def hashtable_add(htable,key,value):
    htable[hash_string(key,len(htable))].append([key,value])
        return htable

def hashtable_get_bucket(htable,keyword):   #only to test, to get the whole bucket to see what's in it
    return htable[hash_string(keyword,len(htable))]

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out
