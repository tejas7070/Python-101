number = int(input("Enter the number: "))

if number >1:
    for i in range(2, number):

        if (number%i==0):
            print("This is not a prime number")
            break
        else:
            print("The number is a prime number")
            break
            