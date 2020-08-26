"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.head.prev = None # we dont have previous anymore
            self.length = self.length - 1
            return current_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail = self.tail
            old_tail.next = new_tail
            new_tail.prev = old_tail 
            self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.length = self.length - 1
            return current_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        while current is not None:
            if current == node:
                previous_node = current.prev
                if previous_node is not None:
                    previous_node.next = current.next

                next_node = current.next
                if next_node is not None:
                    next_node.prev = current.prev

                if current == self.head:
                    self.head = next_node
                if current == self.tail:
                    self.tail = previous_node

                current.prev = None
                current.next = self.head
                self.head.prev = current
                self.head = current

                return 
            
            current = current.next
        


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        while current is not None:
            if current == node:
                previous_node = current.prev
                if previous_node is not None:
                    previous_node.next = current.next

                next_node = current.next
                if next_node is not None:
                    next_node.prev = current.prev
                
                if current == self.head:
                    self.head = next_node
                if current == self.tail:
                    self.tail = previous_node

                current.prev = self.tail
                current.next = None
                self.tail.next = current
                self.tail = current
                return 
            
            current = current.next

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current is not None:
            if current == node:
                previous_node = current.prev
                if previous_node is not None:
                    previous_node.next = current.next
                next_node = current.next
                if next_node is not None:
                    next_node.prev = current.prev

                if current == self.head:
                    self.head = next_node
                if current == self.tail:
                    self.tail = previous_node

                self.length -= 1

                return 
            
            current = current.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_value = None
        while current is not None:
            if max_value is None or current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
