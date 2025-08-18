# Class Methods

class Student:
    count = 0
    total_gpa = 0
    def __init__(self,name,GPA):
        self.name = name
        self.GPA = GPA
        Student.count += 1
        Student.total_gpa += GPA
    def get_info(self):
        return f"{self.name}, {self.GPA}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
        


student1 = Student("Spongebob",4.0)
student2 = Student("Squidward",3.0)
print(student1.get_info())
print(student2.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
        
        