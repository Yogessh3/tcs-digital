#1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, 64, 729, 128, 2187
def numSeries(N):
    series=[1,1]
    ft=1
    st=1
    for i in range(N):
        if(i%2==0):
            series.append(ft*2)
            ft=ft*2
        else:
            series.append(st*3)
            st=st*3
    print(series)
    return series[N-1]
N=int(input())
print(numSeries(N))
