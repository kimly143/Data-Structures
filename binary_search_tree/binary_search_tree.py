"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: 
            if self.left: # we have a left node
                self.left.insert(value)
            else: # it doesnt have a left node yet, we create a new node for it
                self.left = BSTNode(value)
        else:
            if self.right: # we have a right node
                self.right.insert(value)
            else: # it doesnt have a right node, we create a new node for it
                self.right = BSTNode(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left: #left
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # in order left - middle - right
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        nodes = [self]
        while len(nodes) >  0:
            node = nodes.pop(0)
            print(node.value)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print in-order recursive DFT
    def in_order_dft(self):
        pass

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
