#prime number logic
def isprimeNumber(num):
    if(num>=2):
        for i in range(2,(num//2+1)):
            if(num%i==0):
                return False
        return True
    else:
        return False
print(isprimeNumber(2))
print(isprimeNumber(455))
print(isprimeNumber(3))
print(isprimeNumber(9))
print(isprimeNumber(17))