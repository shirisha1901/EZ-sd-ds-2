stc=[]
        
def push_element():
    if len(stc)==n:
        print("stack is full!")
    else:
        element=input("Enter element for the stack:")
        stc.append(element)
        print(stc)
        
def pop_element():
    if not stc:
        print("stack is empty..Add the element")
    else:
        element=stc.pop()
        print(element,"removed")
        print(stc)
        
n=int(input("Enter the size of stack:"))
while True:
    print("Select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter correct operation!")