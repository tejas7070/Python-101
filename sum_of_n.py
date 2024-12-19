num =int(input("Enter a number:"))
sum =0
i = 0
while(i<num):
    i=i+1
    sum=i+sum

   
print(sum)
# using recursion
'''
def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)

n = int(input("Enter a num: "))

print(f"The sum of",n,"natural number is ",sum(n))
'''