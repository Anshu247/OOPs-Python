class Employee:

    company_name = "Google"
    no_of_Employees = 0

    def __init__(self,name):

        self.name = name
        self.raise_amount = 0.02
        Employee.no_of_Employees +=1
    
    def show_details(self):

        print(f"The name of the Employee is {self.name} and the raise amount in {self.no_of_Employees}  sized {self.company_name} is {self.raise_amount}")

emp1 = Employee("Anshu")
emp2 = Employee("Harshit")

emp1.raise_amount = 0.3
emp1.company_name = "Microsoft"

print(Employee.company_name)
Employee.company_name = "Facebook"

emp2.company_name = "Tesla"

emp1.show_details()
emp2.show_details()

# Employee.show_details(emp1)