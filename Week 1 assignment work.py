## Assignment_1
print("Hello, World!")

## Assignment_2
name = input("Jamie")
age = int(input(20))
height = float(input(6))
is_student = bool(input(True))

displayValues(name, age, height, is_student)

message = dataCheck(name,age,height,is_student)

if message == None:
    print('Data types check out - well done!')
    print('Assignment Complete')

else:
    print(message)