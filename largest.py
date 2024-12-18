a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the Fourth number: "))

if(a>b and a>c and a>d):
    print("The largest number is: ",a)
elif(b>a and b>c and b>d):
    print("The largest number is: ",b)
elif(c>a and c>b and c>d):
    print("The largest number is: ",c)
else:
    print("The largest number is: ",d)