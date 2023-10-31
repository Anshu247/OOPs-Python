class Person:

    def __init__(self,name,occ):

        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Anshu","M.L Engineer")
b = Person("Abhijeet","Data Scientist")

a.info()
b.info()