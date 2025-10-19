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
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
    def remove_at_beginning(self):
        if self.head:
            removed_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_node.data
        return None
    
    def remove_at_end(self):
        if self.head:
            if self.head == self.tail:
                removed_node = self.head
                self.head = None
                self.tail = None
                return removed_node.data
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            removed_node = self.tail
            current_node.next = None
            self.tail = current_node
            return removed_node.data
        return None
    
    def remove_at(self, data):
        if self.head:
            if self.head.data == data:
                return self.remove_at_beginning()
            current_node = self.head
            while current_node.next:
                if current_node.next.data == data:
                    removed_node = current_node.next
                    current_node.next = current_node.next.next
                    if removed_node == self.tail:
                        self.tail = current_node
                    return removed_node.data
                current_node = current_node.next
        return None
    