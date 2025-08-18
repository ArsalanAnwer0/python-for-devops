# Search 
# Add


def printList(students):
        print("Student List ")
        for i,name in enumerate(students,start = 1):
            print(f"{i}.{name}")
def search():
        student = input("Search for student: ")
        object1 = enumerate(students,1)

        for i,name in object1:
            if student in students:
                if name == student:
                    print(f"{name} found at {i}")
        else:
            print("Not found")

def add(name,students):
    students.append(name)
    print("student added")
    printList(students)

students = ["Arsalan","Ali","Aisha","Aman","Abdul"]

print("Student List ")
for i,name in enumerate(students,start = 1):
    print(f"{i}.{name}")


search()

choice = input("Add a new student? (yes/no)").strip().lower()
name = input("Enter name: ")

add(name,students)

    

