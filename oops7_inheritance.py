class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def show_details(self):
        print(f"The name of the Employee is {self.name} and the id is {self.id}")

class Programmer(Employee):

    def show_language(self):
        print(f"The default language is Python")

e1 = Employee("Anshu",777)
e2 = Programmer("Harshit",888)

e1.show_details()
e2.show_details()
e2.show_language()
