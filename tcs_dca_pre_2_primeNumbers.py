def isPrime(num):
    if(num>1):
        for i in range(2,num//2+1):
            if(num%i==0):
                return False
        return True
    else:
        return False
num=int(input())
if num>0:
    if isPrime(num):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
else:
    print("Please enter a positive number")
