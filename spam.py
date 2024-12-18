p1= "Click This Link To Get 100% Off"
p2= "Avail 100% Discount On Your First Order"
p3="buy 1 get 1 free"

message = input("Enter Your Message: ")

if p1 in message:
    print("Spam Detected")
elif p2 in message:
    print("Spam Detected")
elif p3 in message:
    print("Spam Detected")
else:
    print(" This isNot Spam")
