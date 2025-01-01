Q =[]
f =-1
r =-1

def Push():
	global f, r, Q
	print("Enter the element to be pushed: ", end='')
	num = int(input())
	Q.append(num)
	if(f == -1):
		f = r = 0
	else:
		r += 1	
	Disp()

def Disp():
	global Q, f, r
	if(f == -1):
		print("Queue is empty")
	else:
		print("Queue: ")
		for i in range(f, r + 1):
			print(Q[i])
		

def Peek():
	global Q, f, r
	if(f == -1):
		print("Queue is empty")
	else:
		print("Front element is:")
		print( Q[f])


def Pop():
	global Q, f, r
	
	if(f == -1):
		print("Queue is Empty")
	else:
		print("Popped element is:", Q[f])
		Q.pop(f)
		f += 1
		r -= 1
		if(r == -1):
			f = -1
			print("Queue is Empty")
    
while True:
	
	print("\nQueue Operations:")
	print("1. Push")
	print("2. Display")
	print("3. Peek")
	print("4. Pop")
	print("5. Exit")
	
	choice = int(input("Enter your Choice of Actions to be performed: "))
	if choice == 1:
		Push()
	elif choice == 2:
		Disp()
	elif choice == 3:
		Peek()
	elif choice == 4:
		Pop()
	elif choice == 5:
		break
	else:
		print("Invalid choice, please try again.")
