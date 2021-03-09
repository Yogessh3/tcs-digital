def numSeries(n):
    series=[]
    ft=0
    st=0
    for i in range(n):
        if(i%2==0):
            series.append(ft)
            ft+=2
        else:
            series.append(st)
            st+=1
    print(series)
    return series[n-1]
N=int(input())
print(numSeries(N))

