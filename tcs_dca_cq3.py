def product(number):
    product=1
    for i in range(len(number)):
        product*=int(number[i])
    return product
number=int(input())
if number < 0:
    print("Invalid Input")
else:
    number=str(number)
    print(product(number))