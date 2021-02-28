def calcMaxSum(array):
    sum=0
    for i in range(len(array)-2):
        for j in range(len(array)-1):
            newSum=array[i]+array[j]+array[j+1]
            if newSum>sum:
                sum=newSum
    return sum
array=[int(x) for x in input().split()]
print(calcMaxSum(array))
