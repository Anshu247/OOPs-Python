class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def from_str(self,string):
        return self(string.split("-")[0],int(string.split("-")[1]))

e1 = Employee("Anshu","77000")

print(e1.name)
print(e1.salary)

string = "Harshit-88000"
# e2 = Employee(string.split("-")[0],string.split("-")[1])
e2 = Employee.from_str(string)

print(e2.name)
print(e2.salary)

