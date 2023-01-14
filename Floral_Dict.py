from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for ll in list_at_array:
            if ll[0] == key:
                ll[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for ll in list_at_index:
            if ll[0] == key:
                return ll[1]
            else:
                return None


blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
    blossom.assign(i[0], i[1])

for i in flower_definitions:
    print(i[0])

while True:
    key = str(input("Choose the the flower you wish to know the meaning of! "))
    # if key not in flower_definitions[i[0]]:
    #   print("Please choose a flower in the dictionary! ")
    #   continue

    print(blossom.retrieve(key))
