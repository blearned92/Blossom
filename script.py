from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap():
    def __init__(self, array_size):
      self.array_size = array_size
      self.array = [LinkedList() for item in range(array_size)]

    def hash(self, key):
      return sum(key.encode()) % self.array_size 

    def assign(self, key, value):
      array_index = self.hash(key) 
      for item in self.array[array_index]: # starts as a list of empty linked lists
        if key == item[0]: # has to treat each linked list (item) as if it has key:value pairs
          item[1] = value # this will overwrite an existing value if a key matches
          return # ends to not execute next command
      self.array[array_index].insert(Node([key, value])) # if key does not match, insert a new node as head node with key:value pair

    def retrieve(self, key):
      array_index = self.hash(key)
      for item in self.array[array_index]: # searches through items in linked list at this index
        if key == item[0]: # searches for specific key to return the value of
          return item[1] # returns value when found
      return None # if not found, cannot return so returns none

blossom = HashMap(10)

for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

for items in blossom.array:
  for item in items:
    print(item[0])

