class Employee:

    company = "Google"


    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def change_company(self, new_company):
        self.company = new_company

e1 = Employee()

e1.name = "Anshu"
e1.show()

e1.change_company("Tesla")
e1.show()

print(Employee.company)

