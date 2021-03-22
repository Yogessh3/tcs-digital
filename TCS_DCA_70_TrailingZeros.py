def findTrailingZeros(n):
    count=0
    while(n>=5):
        n=n//5
        print(n)
        count+=n
    return count
n = 100
print("Count of trailing 0s " +
	"in 100! is", findTrailingZeros(n))
