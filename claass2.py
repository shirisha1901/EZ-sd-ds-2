class Employee:
    def __init__(self):
        self.emp_id=input("Emp id:")
        self.emp_name=input("Emp name:")
        self.emp_salary=float(input("Salary:"))
        self.emp_dept=input("Department:")
        self.hoursworked=int(input("Hours worked:"))
    def Calculate_emp_salary(self,hoursworked):
        if self.hoursworked>50:
            overtime=self.hoursworked-50
            overtimeamount=overtime*(self.emp_salary/50)
            self.emp_salary+=overtimeamount
            print("salary:",self.emp_salary)
        else:
            print(self.emp_salary)
    def Employee_details(self):
        print("Emp id =",self.emp_id)
        print("Emp name =",self.emp_name)
        print("Emp salary =",self.emp_salary)
        print("Emp department =",self.emp_dept)
obj1=Employee()
obj1.Calculate_emp_salary(60)
obj1.Employee_details()