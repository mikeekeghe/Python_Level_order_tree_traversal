class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque  # Import the deque class for the queue


class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.maxSize = 100

    def enqueue(self, element):
        if self.isFull():
            return False
        self.queue.append(element)
        self.tail += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return None  # You can also raise an exception if you prefer
        item = self.queue[self.head]
        self.head += 1
        return item

    def peek(self):
        if self.isEmpty():
            return None  # You can also raise an exception if you prefer
        return self.queue[self.head]

    def getLength(self):
        return self.tail - self.head

    def isEmpty(self):
        return self.getLength() == 0

    def isFull(self):
        return self.getLength() == self.maxSize


def levelOrder(root):
    # If the root is None, return an empty list.
    if not root:
        return []

    result = []
    visited = []
    queue = Queue()

    # Add the root to the queue.
    queue.enqueue(root)

    while queue.isEmpty() == False:
        # Remove a node from the queue.
        current = queue.dequeue()
        # Add the node's data to the result.
        result.append(current.info)

        # If the node has a left child, add it to the queue.
        if current.left:
            queue.enqueue(current.left)
            visited.append(current.left)

        # If the node has a right child, add it to the queue.
        if current.right:
            queue.enqueue(current.right)
            visited.append(current.right)

    result_str = ' '.join(map(str, result))
    print(result_str)
