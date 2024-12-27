LL =[]
#Creating the LinkedList
def createLL():
    global LL
    print("ENter an element:" , end=" ")
    val = int(input())
    LL.append(val)

    print("\n")
    Disp()
    print("\n")
    #Displaying the Linkedlist
def Disp():
    if LL == []:
        print("LL is empty")
    else:
        for i in range(len(LL)):
            print(LL[i], end=" ")


#Inserting a node at the beginning of the linked list
def insertBegin():
    global LL
    print("Enter the value to be inserted first: ")
    ele =int(input())
    LL.insert(0,ele)
    print("\n")
    Disp()
    print("\n")


#Inserting a node at the end of the linked list
def insertEnd():
    global LL
    print("Enter the value to be inserted at the end: ")
    ele = int(input())

    LL.append(ele)
    print("\n")
    Disp()
    print("\n")


#Inserting a node at specific position of the linked list
def insertgiven():
    global LL
    print("Enter the value to be inserted: ")
    ele = int(input())
    print("Enter the position: ")
    pos = int(input())
    LL.insert(pos-1,ele)
    print("\n")
    Disp()
    print("\n")


#Deleting a node from the Beginning of the LinkedList
def deleteBegin():
    global LL
    if LL ==[]:
        print ("LL is empty")
    else:
        print("After deletion: ", end="")
        LL.pop(0)
        print("\n")
        Disp()
        print("\n")
#Deleting a node from the end of the LinkedList    

def deleteend():
    global LL
    if(LL == []):
        print("LL is empty")
    else:
        print("After deletion: ", end="")
        LL.pop()    
          
        print("\n")
        Disp()

#Deleting a node from a specific position of the LinkedList

def deletegiven():
    global LL
    print("Enter the position: ")
    pos = int(input())
    if(LL == [] or pos <= 0):
        print(" Invalid Input!! ")
    else:
         print("After deletion: ", end="")
         LL.pop(pos-1)
    print("\n")
    Disp()

# sorting the linkedList
def sortLL():
    global LL
    LL.sort()
    Disp()
    
 #Prime number in LinkedList
def prime():
    global LL
    for i in range(len(LL)):
        flag = True
        if LL[i] > 1:

            for j in range(2, LL[i]):
                if(LL[i]%j ==0):
                    flag = False
                    print("The number is not prime")
                else:
                    print("The number is prime")    
while(True): 
    print("\n")
    print("1]Create a linkedList")
    print("2]Display a linkedList")
    print("3]Insert a node at the beginning of the linkedList")
    print("4]Insert a node at the end of the linkedList")
    print("5]Insert a node at a specific position of the linkedList")
    print("6]Delete a  node from the beginning of the linkedList")    
    print("7]Delete a node from the end of the linkedList")
    print("8]Delete a node from a specific position of the linkedList")
    print("9]Sort the linkedList")
    print("10] Find Prime number in the linkedList")
    print("11]Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        createLL()
    elif choice == 2:
        Disp()
    elif choice == 3:
        insertBegin()
    elif choice == 4:
        insertEnd()
    elif choice == 5:
        insertgiven()
    elif choice == 6:
        deleteBegin()
    elif choice == 7:
        deleteend()
    elif choice == 8:
        deletegiven()
    elif choice == 9:
        sortLL()
    elif choice == 10:
        prime()
    elif choice == 11:
        print("Exiting the program!!")
        break
    else:
        print("Invalid choice!!")
    

# createLL()
# insertBegin()
# insertEnd()
# insertgiven()
# # deletegiven()
# sortLL()
# # Disp()
# # deleteBegin()
# # deleteend()
