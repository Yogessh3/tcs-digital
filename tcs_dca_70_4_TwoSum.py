def twoSum(array,targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        currSum=array[left]+array[right]
        if(currSum<targetSum):
            left+=1
        elif(currSum>targetSum):
            right-=1
        else:
            return array[left],array[right]
array=[int(x) for x in input().split()]
targetSum=int(input())
a,b=twoSum(array,targetSum)
print(a,b)
