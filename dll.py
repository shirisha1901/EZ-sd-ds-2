class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
                                                    
class DLL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.next
                
    def insert_begining(self,data):
        new_node = Node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node
        
    def insert_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev= temp
        
    def insert_position(self,pos,data):
        new_node = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        
    def delete_begining(self):
        temp = self.head
        self.head.next = temp.next
        temp.next.prev = None
        temp.next = None
        
    '''def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None'''
        
    def delete_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        temp.prev = prev
        
        
            
node_1 = Node("shirisha")
dl = DLL()
dl.head = node_1
node_2=Node("Abhinandana")
node_1.next = node_2
node_2.prev = node_1
node_3 = Node("Harshini")
node_4 = Node("Siri")
node_5 = Node("Abhi")
node_2.next = node_3
node_3.next = node_4
node_3.prev = node_2
node_4.next = node_5
node_4.prev = node_3
dl.display()
print("")
dl.insert_begining("Harshu")
dl.display()
print("")
dl.insert_end("varshi")
dl.display()
print("")
dl.insert_position(6,"ritesh")
dl.display()
print("")
dl.delete_begining()
dl.display()
print("")
#dl.delete_end()
#dl.display()
print("")
dl.delete_position(3)
dl.display()
