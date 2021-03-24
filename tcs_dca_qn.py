import re
def countWays(a,b):
  n=len(a)
  m=len(b)
  dp=[[0 for j in range(n)] for i in range(m)]
  for i in range(m):
    for j in range(i,n):
      if(i==0):
        if(j==0):
          if(a[j]==b[i]):
            dp[i][j]=1
          else: 
            dp[i][j]=0
        elif(a[j]==b[i]):
          dp[i][j]=dp[i][j-1]+1
        else:
          dp[i][j]=dp[i][j-1]
      else:
        if(a[j]==b[i]):
          dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])
        else:
          dp[i][j]=dp[i][j-1]
  return dp[m-1][n-1]
s1=input()
s2=input()
a="".join(re.findall("[a-zA-Z]*",s1))
b="".join(re.findall("[a-zA-Z]*",s2))
if(s1==s2):
  print(0)
else:
  noofWays=countWays(s1,s2)
  print(noofWays)
