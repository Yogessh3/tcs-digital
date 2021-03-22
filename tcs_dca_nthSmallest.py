def check(numbers):
    for num in numbers:
        if numbers.count(num)>0:
            return False
    return True
def nthSmallest(arr,k):
    arr.sort()
    print(arr[-k])
numbers=[]
n=int(input())
for i in range(n):
    numbers.append(int(input()))
k=int(input())
if check(numbers):
    nthSmallest(numbers,k)
else:
    print("INVALID INPUT")

