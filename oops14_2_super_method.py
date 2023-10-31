class Employee:

    def __init__(self, name, id):

        self.name = name
        self.id = id

class Programmer(Employee):

    def __init__(self, name, id, lang):

        super().__init__(name,id)
        self.lang = lang

        # self.id = id
        # self.lang = lang
    
Anshu = Employee("Anshu","77")
Harshit = Programmer("Harshit","88","Python")

# print(Anshu.name)

print(Harshit.name)
print(Harshit.id)
print(Harshit.lang)