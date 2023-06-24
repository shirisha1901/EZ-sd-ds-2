queue=[]

def enqueue():
    if len(queue)==n:
        print("Queue is full!")
    else:
        element=input("Enter element for the queue:")
        queue.append(element)
        print(queue)
    
def dequeue():
    if not queue:
        print("Queue is empty..Add the element")
    else:
        element=queue.pop(0)
        print(element,"removed")
        print(queue)      

n=int(input("Enter the size of Queue:"))
while True:
    print("Select operation 1.Enqueue 2.Dequeue 3.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("Enter correct operation!")