n = int(input("Enter the number: "))

for i in range (1,n+1):
    if(i==1 or i==n or i==(n+1)/2):
     print("*"*(n),end="")
    
    else:
       print("*",end="")
       print(" "*(n-2),end="")
       print("*",end="")
    print("")
   