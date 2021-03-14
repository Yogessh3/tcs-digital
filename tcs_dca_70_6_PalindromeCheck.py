T=int(input())
for test in range(T):
  string=input().split()
  numbers=[]
  for st in string:
    if st.isdigit():
      numbers.append(int(st))
  if(len(numbers)):
    print(max(numbers))
  else:
    print(-1)

    