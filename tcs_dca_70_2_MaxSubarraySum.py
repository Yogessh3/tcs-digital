def maxSubarraySum(array):
    maxEndingHere=array[0]
    maxSoFar=array[0]
    for i in range(1,len(array)):
        maxEndingHere=max(array[i],maxEndingHere+array[i])
        maxSoFar=max(maxSoFar,maxEndingHere)
    return maxSoFar
array=[int(x) for x in input().split()]
print(maxSubarraySum(array))

    