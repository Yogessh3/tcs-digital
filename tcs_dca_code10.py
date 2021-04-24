class Employee:
  def __init__(self,empId,empName,empDept,salary,role):
    self.empId=empId
    self.empName=empName
    self.empDept=empDept
    self.salary=salary
    self.role=role
  def calculateIncentive(self,emp,roleIncentivePercent):
    for k,v in roleIncentivePercent.items():
      if(k.lower()==emp.role.lower()):
        incentive=emp.salary*(v/100)
        return incentive
    return None
T=int(input())
roleIncentivePercent={}
for test in range(T):
  role=input()
  incentivePercent=int(input())
  roleIncentivePercent[role]=incentivePercent
N=int(input())
employees=[]
for test in range(N):
  empId=int(input())
  empName=input()
  empDept=input()
  salary=int(input())
  role=input()
  E=Employee(empId,empName,empDept,salary,role)
  employees.append(E)
role=input()
def calcEmpSal(role,employees,roleIncentivePercent):
  ans=[]
  for emp in employees:
    if(emp.role.lower()==role.lower()):
      incentive=E.calculateIncentive(emp,roleIncentivePercent)
      if incentive is not None:
        emp.salary+=incentive
      ans.append(emp)
  return ans
for role in roleIncentivePercent:
  flag=0
  if(role.lower()==employees[0].role.lower()):
    incentive=employees[0].salary*roleIncentivePercent[role]/100
    flag=1
    break
if flag==1:
  print(incentive)
else:
  print("Employee Not Found")
answer=calcEmpSal(role,employees,roleIncentivePercent)
if not answer:
  print("Employee Not Found")
else:
  for j in answer:
    print(j.empId,j.empName,j.salary)

        
