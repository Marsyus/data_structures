from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = new_node
        else:
            self.head = new_node
            self.tail = new_node
    