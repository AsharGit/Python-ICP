class Employee:
    num_employees = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.emp_name = name
        self.emp_family = family
        self.emp_salary = salary
        self.emp_dept = department
        self.increment(salary)

    # Increment num_employees and total_salary
    def increment(self, salary):
        self.__class__.num_employees += 1
        self.__class__.total_salary += salary

    # Return the average salary of employees
    def avg_salary(self):
        return self.total_salary / self.num_employees


class FulltimeEmployee(Employee):

    # Increment num_employees and total_salary in parent class
    def increment(self, salary):
        Employee.num_employees += 1
        Employee.total_salary += salary


# Initialize an employee and a full time employee
emp1 = Employee('Bob', 'Smith', 40000, 'health')
emp2 = FulltimeEmployee('Linda', 'Smith', 80000, 'health')

print(emp1.emp_name)
print(emp1.emp_salary)

print(emp2.emp_name)
print(emp2.emp_salary)

print(emp1.num_employees)
print(emp2.num_employees)

print(emp1.avg_salary())
print(emp2.avg_salary())
