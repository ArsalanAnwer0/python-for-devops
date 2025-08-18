

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Cook")
print(Employee.is_valid_position("Cook"))
print(employee3.get_info())
        
        