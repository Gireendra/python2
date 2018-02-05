#! /usr/bin/python
# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable,key):
    i=hash_string(key,len(htable))
    for x in range(len(htable[i])):
        if key in htable[i][x]:
            return htable[i][x][1]
    return None
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

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
