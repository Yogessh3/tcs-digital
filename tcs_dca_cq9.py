def uniqueDigits(num1,num2):
    numSet={}
    unique=[]
    for number in range(num1,num2+1):
        number=str(number)
        for num in number:
            if num in numSet:
                numSet[num]=False
            else:
                numSet[num]=True
    for key in numSet:
        if numSet[key]:
            unique.append(key)
    return unique
range1,range2=map(int,input().split())
solution=uniqueDigits(range1,range2)
print(*solution,sep=" ")
        
