def powCheck(num):
    if(num<0):
        print("Wrong Input")
    else:
        powNum=num**4
        powNum=str(powNum)
        num=str(num)
        powNum=str(powNum)
        len1=len(num)
        len2=len(powNum)
        if(num==powNum[-len1:]):
            print("YES")
        else:
            print("False")            
n=int(input())
powCheck(n)