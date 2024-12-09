subject= ["English","Maths","Science"]
Marks= [15,14,18,19]
list.append(subject,"Physics")
list.sort(subject)
Marks.insert(0,20)
print(Marks)
print(subject)
avg = Marks[0]+Marks[1]+Marks[2]+Marks[3]/4
subject[0]=Marks[0]
print("English Marks:",subject[0])

print("GPA:",avg)