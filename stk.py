stk =[]
top = -1

def push():
    global top
    global stk

    print("Enter the element to be pushed: ", end='')
    num = int(input())
    stk.append(num)
    top += 1

def Disp():
    global top
    global stk

    if(stk == []):
        print("Stack is empty")
    else:
        print("Stack elements: ", end='')
        for i in range(top,-1,-1):
            print(stk[i])

def pop():
    global top
    global stk

    if(top == -1):
        print("Stack is empty")
    else:
        print(" After pop operation: ")
        stk.pop()
        top -= 1
    

def peek():
    global top
    global stk

    if(top==-1):
        print("Stack is empty")
    else:
        print("Top element of the stack is: ",stk[top])



while(True):
    print("Stack Operations: ")
    print("1] PUSH : ")
    print("2] DISP : ")
    print("3] PEEK : ")
    print("4] POP  : ")
    print("5] EXIT : ")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
        Disp()
    elif choice == 2:
        Disp()
    elif choice == 3:
        peek()
    elif choice == 4:
        pop()
        Disp()
    elif choice == 5:
        print("TErminating The Program!!!")
        break    
    else:
        print(" ANDHA HAI KYA .....LAWDE!!")

# push()
# Disp()
# peek()
# pop()
