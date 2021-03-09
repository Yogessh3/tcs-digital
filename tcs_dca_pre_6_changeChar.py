s1=list(input())
s2=list(input())
s3=list(input())
vow='aeiouAEIOU'
for i in range(len(s1)):
    if s1[i] in vow:
        s1[i]="%"
for i in range(len(s2)):
    if s2[i].isalpha() and s2[i] not in vow:
        s2[i]="#"
for i in range(len(s3)):
    s3[i]=s3[i].upper()
newStr=[]
for i in s1:
    newStr.append(i)
for i in s2:
    newStr.append(i)
for i in s3:
    newStr.append(i)
print(*newStr,sep='')

