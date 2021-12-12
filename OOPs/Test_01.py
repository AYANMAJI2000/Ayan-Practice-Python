'''
My Very First program and commit
'''

class Employee:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
    
    @staticmethod
    def greet():
        print("Good Morning")

employee_1 = Employee("Ayan",21)
employee_2 = Employee("Rahul",44)

employee_1.print()
employee_1.greet()
employee_2.print()
employee_2.greet()

