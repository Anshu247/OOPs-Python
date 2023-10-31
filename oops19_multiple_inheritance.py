class Employee:
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    
    def show(self):
        print(f"The dance is {self.dance}")

class Dancer_Employee(Employee,Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = Dancer_Employee("Kathak","Sneha")

print(o.name)
print(o.dance)

o.show()
print(Dancer_Employee.mro())
    