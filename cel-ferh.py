#Celsius to Fahrenheit

def ctf(num):
    return (num * 9/5)+32

num = int(input("Enter the Temperature in Celsius: "))
print(f"{num}°C is equal to {ctf(num)}°F")