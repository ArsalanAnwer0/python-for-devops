age = int(input("enter your age: "))
if age>=18:
    print("you can vote!")
elif age<=0:
    print("Invalid age")
else:
    print("you are less than 18")