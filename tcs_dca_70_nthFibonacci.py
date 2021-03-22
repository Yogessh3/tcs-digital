#[0,1,1,2,3,5,8,13,18]
def nthFibonacci(num):
    fibonacci=[0,1]
    for i in range(2,num):
        fibonacci.append(fibonacci[-2]+fibonacci[-1])
    return fibonacci[num-1]
print(nthFibonacci(3))
print(nthFibonacci(5))
print(nthFibonacci(7))
print(nthFibonacci(8))