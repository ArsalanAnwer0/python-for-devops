# Exception Handling and File operations

file_name = input("Please enter the name of file you want to create ")
data_one = input("Enter line 1 ")
data_two = input("Enter line 2 ")
data_three = input("Enter line 3 ")

try:
    with open(file_name, 'w') as file:
        file.write(data_one)
        file.write(data_two)
        file.write(data_three)
        print("File created sucessfully")

except:
    print("Found error")

file.close()
try:
    with open(file_name,'r') as file:
        print("File contents")
        print(file.read())
except:
    print("Found error")
file.close()