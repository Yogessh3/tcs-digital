def numSeries(n):
    firstTerm=0
    secondTerm=0
    d1=7
    d2=6
    val1=n//2
    val2=n//2
    if(n%2!=0):
        val1+=1
        val2+=1
    if(n%2!=0):
        n1=firstTerm+(val1-1)*d1
        return n1
    else:
        n2=secondTerm+(val2-1)*d2
        return n2
N=int(input())
print(numSeries(N))