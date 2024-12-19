#inches to centimeter
def itc(num):
    return (num * 2.54)
      
num = int(input("Enter the Measurement in inches: "))
print(f"{num} inches is equal to {itc(num)} centimeters")



