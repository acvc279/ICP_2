class Employee:
    Emp_count = 0
    salarytotal = 0
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.Emp_count += 1
        Employee.salarytotal += salary

    def empcount(self):
        print("No. of Employee Count =", Employee.Emp_count)

    def avgsalary(self):
        print("Total Salary " ,Employee.salarytotal)
        a = Employee.salarytotal / Employee.Emp_count
        print("Average salary =", a)

    def call_fun(self):
        print("function call")

class Fulltime_Employee(Employee):
    def __init__(self):
        print("subclass")

if __name__ == "__main__":
      emp = int(input("enter no of employee:"))
      for i in range(emp):
          Na = input("Name:")
          Fa = input("Family:")
          Sa = float(input("Salary:"))
          De = input("Department:")
          b = Employee(Na,Fa,Sa,De)
      e = Fulltime_Employee()
      e.empcount()
      e.avgsalary()
      b.call_fun()