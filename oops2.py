class Person:

    name = "Anshu"
    occupation = "Software Developer"
    networth = 100000000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "Harshit"
# a.occupation = "Data Scientist"
# print(a.name)
a.info()