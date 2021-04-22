class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        self.bmi=round(weight/(height*height))
        self.bmiStatus=""
class Society:
    def __init__(self,bmi_status,persons):
        self.bmi_status=bmi_status
        self.persons=persons
    def calcBmiStatus(self,name):
        flag=0
        for person in self.persons:
            if(person.name.lower()==name.lower()):
                flag=1
                for bmis in self.bmi_status.keys():
                    low=self.bmi_status[bmis][0]
                    up=self.bmi_status[bmis][1]
                    if(person.bmi<=low and person.bmi>=up):
                        person.bmiStatus=bmis
                        break
                print(person.bmi,person.bmiStatus)
        if(flag==1):
            return True
        else:
            return False             
    def invalid(self,number):
        ans=[]
        for person in self.persons:
            if(person.bmi<number):
                ans.append(person)
        return ans
N=int(input())
persons=[]
bmiStatus={}
for i in range(N):
    name=input().strip()
    height=int(input())
    weight=int(input())
    persons.append(Person(name,height,weight))
T=int(input())
for test in range(T):
    bmiStatusString=input().strip()
    low=int(input())
    up=int(input())
    bmiStatus[bmiStatusString]=(max(up,low),min(up,low))
S=Society(bmiStatus,persons)
personName=input()
bmival=int(input())
fans1=S.calcBmiStatus(personName)
fans2=S.invalid(bmival)
if not fans1:
    print("No Person Exists")
for fn in fans2:
    print(fn.name,fn.bmi)



'''
5
Rajesh
5
50
Suman
4
89
Gopi 
5
99
Radhika
6
120
Rajesh
5
120
4
Normal
2
3
Overweight
4
6
Underweight
0
1
Abnormal
7
10
Rajesh
5
'''



                

    