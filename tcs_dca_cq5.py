def calcSum(array):
    sum=0
    newSum=[]
    for i in range(1,len(array)):
        if array[i-1]<array[i]:
            sum+=array[i-1]
        else:
            if sum!=0:
                sum+=array[i-1]
                newSum.append(sum)
                sum=0
    if array[-2]<array[-1]:
        sum+=array[-1]
        newSum.append(sum)
    return ' '.join(map(str,newSum))
array=[int(x) for x in input().split()]
if len(array)>1:
    print(calcSum(array))
else:
    print("Invalid Input")
