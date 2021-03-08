def oddlyEven(num):
    odd_digit=0
    even_digit=0
    for i in range(len(num)):
        if(i%2==0):
            odd_digit+=int(num[i])
        else:
            even_digit+=int(num[i])
    return abs(odd_digit-even_digit)
num=input().strip()
print(oddlyEven(num))
