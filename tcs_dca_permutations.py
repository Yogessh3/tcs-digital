def permutations(array):
    perms=[]
    getPermutationsHelper(0,array,perms)
    return perms
def getPermutationsHelper(i,arr,perms):
    if(i==len(arr)-1):
        perms.append(arr[:])
    else:
        for j in range(i,len(arr)):
            swap(i,j,arr)
            getPermutationsHelper(i+1,arr,perms)
            swap(i,j,arr)
def swap(i,j,arr):
    arr[i],arr[j]=arr[j],arr[i]
print(permutations([1,2,3]))
