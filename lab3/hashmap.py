size = 10
hashMap = {}

class DataItem:
    def __init__(self, key):
        self.key = key

def hashCode(key):
    return key % size

def search(key):
    hashIndex = hashCode(key)
    while hashIndex in hashMap:
        if hashMap[hashIndex].key == key:
            return hashMap[hashIndex]
        hashIndex = (hashIndex + 1) % size
    return None

item2 = DataItem(25)
item3 = DataItem(64)
item4 = DataItem(22)

hashIndex2 = hashCode(item2.key)
hashMap[hashIndex2] = item2

hashIndex3 = hashCode(item3.key)
hashMap[hashIndex3] = item3

hashIndex4 = hashCode(item4.key)
hashMap[hashIndex4] = item4

keyToSearch = 64
result = search(keyToSearch)
if result:
    print("Element found")
else:
    print("Element not found")