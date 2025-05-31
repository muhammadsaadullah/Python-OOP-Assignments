class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

emp = Employee("John", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)
try:
    print(emp.__ssn)
except AttributeError:
    print("Cannot access private attribute directly.")