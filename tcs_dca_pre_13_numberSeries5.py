def product(arr):
    prod=1
    for i in arr:
        prod*=i
    return prod
def sumexceptself(arr):
    newArr=[]
    for i in range(len(arr)):
        newArr.append(sum(arr[:i])+sum(arr[i+1:]))
    print(newArr)
def productexceptself(arr):
    newArr=[]
    for i in range(len(arr)):
        newArr.append(product(arr[:i])*product(arr[i+1:]))
    print(newArr)
arr=[1,2,3,4,5]
def prefixSum(arr):
    newArr=[arr[0]]
    for i in range(1,len(arr)):
        newArr.append(newArr[-1]+arr[i])
    print(newArr)
def suffixSum(arr):
    newArr=[]
    for i in range(len(arr)):
        newArr.append(sum(arr[i:]))
    print(newArr)
sumexceptself(arr)
prefixSum(arr)
suffixSum(arr)
productexceptself(arr)
