n=int(input())
sq=n*n
str_n=str(n)
str_sq=str(sq)
length=len(str_n)
if(int(n)<0):
  print("Wrong Input")
else:
  if(str_n==str_sq[-length:]):
    print("Correct Number")
  else:
    print("Incorrect Number")