def sort(arr):
    left=0
    right=len(arr)-1
    while left<right:
        if(arr[left]==0):
            left+=1
        elif(arr[right]==1):
            right-=1
        else:
            swap(arr,left,right)
            left+=1
            right-=1
    return arr
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
arr=[int(x) for x in input().split()]
sort(arr)
print(*arr)
        
