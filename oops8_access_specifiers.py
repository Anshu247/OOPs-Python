class Employee:
    
    def __init__(self):
        self.name1 = "Anshu" # public access specifier
        self.__name2 = "Harshit" # private access specifier

a = Employee()
print(a.name1)
# print(a.__name2) #this will give error because we cannot access private object directly

print(a._Employee__name2) # this can be access indirectly
print(a.__dir__())