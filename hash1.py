#! /usr/bin/python
# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

def hashtable_update(htable,key,value):
    if hashtable_lookup(htable,key)==None:
        hashtable_add(htable,key,value)
    else:
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key:
                entry[1]=value
        
        
    return htable

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
