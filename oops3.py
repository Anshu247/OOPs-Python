class Person:

    name = "Anshu"
    occupation = "Software Developer"
    networth = 100000000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Harshit"
a.occupation = "Data Scientist"

b.name = "Abhijeet"
b.occupation = "Web Developer"

a.info()
b.info()
c.info()