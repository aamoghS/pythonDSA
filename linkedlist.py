class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def createNode(self, data):
        return Node(data)

    def insertAtStart(self, data):
        new_node = self.createNode(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        if self.head is None:  
            self.insertAtStart(data)
            return
        
        new_node = self.createNode(data)
        walking = self.head
        while walking.next:
            walking = walking.next
        walking.next = new_node  

    def display(self):
        temp = self.head
        while temp:  
            print(temp.data)  
            temp = temp.next
    
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = val
        else:
            print("index not present")

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        
        if index ==0: 
            self.remove_first_node()
            return 
        
        current_node = self.head 
        position =0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("out of range mr white")
        
    def remove_node(self, data):
        current_node = self.head
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return
    
        while current_node is not None and current_node.data == data:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next 
        print("node")
    
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size 
        





llist = LinkedList()
llist.insertAtStart(5)
llist.insertAtStart('C')
llist.insertAtEnd(10) 

print("display old:")
llist.display()


print("display new:")
llist.remove_last_node() #remove the last 
llist.display()


print("display newer:")
llist.remove_first_node() #remove the first 
llist.display()

print("display new:")
llist.updateNode('E', 1)
llist.display()
