def pattern(n):
  if(n==size):
    return
  else:
    print("*"*n)
    pattern(n+1)



n = int(input("Enter your num: "))
size =int(input("Enter the size of the pattern: "))
pattern(n)