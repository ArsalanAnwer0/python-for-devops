

class Company:
    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position
        def get_details(self):
            return [f"{self.name}, {self.position}"]
    def __init__(self,company_name):
        self.company_name = company_name
        self.employee = []
        
    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employee.append(new_employee)
    def list_employee(self):
        return [employee.get_details() for employee in self.employee]
    
company = Company("Krusty Krab")
company.add_employee("Eugene","Manager")
company.add_employee("Spongebob","Cook")
company.add_employee("Squidward","Cashier")

for employee in company.list_employee():
    print(employee)