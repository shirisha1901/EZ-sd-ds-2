#overtime=hourworked-50
#overtimeamount=overtime*(salary/50)
'''
class Employee:
    emp_id=int(input("emp id:"))
    emp_name=input("emp name:")
    emp_department=input("emp dept:")
    emp_salary=int(input("emp salary:"))
    hourworked=int(input("hours worked:"))
obj=Employee()
print("Employee ID: ",obj.emp_id)
print("Employee Name: ",obj.emp_name)
print("Employee Department: ",obj.emp_department)
if(obj.hourworked > 50):
   overtime=obj.hourworked-50 
   overtimeamount=overtime*(obj.salary/50)
   print("Salary=",overtimeamount+obj.emp_salary)
else:
    print("salary=",obj.emp_salary)
    '''
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
        print("Emp name =",self.emp_id)
        print("Emp salary =",self.emp_id)
        print("Emp department =",self.emp_id)
obj1=Employee()
obj1.Calculate_emp_salary(60)
obj1.Employee_details()
    
        

