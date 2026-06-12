class Employee:
    def __init__(self):
        self._salary = 50000

    def increment(self):
        self._salary += 10000

    def deduct(self):
        self._salary -= 5000

    def get_salary(self):
        print("Salary =", self._salary)


m1 = Employee()
m2 = Employee()

m1.increment()
m1.deduct()
m1.get_salary()

m2.increment()
m2.deduct()
m2.get_salary()