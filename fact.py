# num = int(input("Enter a num: "))
# fact = 1
# if(num >= 0):

#     for i in range(num,0,-1):
#         fact = fact * i
#     print("Factorial of",num,"is",fact)
# else:
#     print("Factorial of a negative number doesn't exist")
        
#Using recursion

def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*fact(num-1)
    
num = int(input("Enter a number: "))

print(f"Factorial of",{num},"is",{fact(num)})