
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
as the underlying storage structure.
Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
implementing a Queue?
Both enqueue and dequeue in an array take O(n)
In linkedList it take O(1)

Operation for LinkedList is more effecient but storage is double because on LinkedList, each item need itself and also a pointer

Stretch: What if you could only use instances of your Stack class to implement the Queue?
What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList 

# class Queue:
#     def __init__(self):
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self) == 0:
#             return None
#         return self.storage.pop(0)


class Queue:
    def __init__(self):
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()
