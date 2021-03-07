def isMonotonic(array):
    isNonIncreasing=True
    isNonDecreasing=True
    for i in range(1,len(array)):
        if(array[i-1]<array[i]):
            isNonIncreasing=False
        elif(array[i-1]>array[i]):
            isNonDecreasing=False
    return isNonIncreasing or isNonDecreasing
array=[int(x) for x in input().split()] 
print(isMonotonic(array))