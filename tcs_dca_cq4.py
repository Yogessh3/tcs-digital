def commonCharacters(str1,str2):
    common=set()
    for i in range(len(str1)):
        for j in range(i,len(str2)):
            if str1[i]!=" " and str1[i]==str2[j]:
                common.add(str1[i])
    return list(common)
str1=input()
str2=input()
output=commonCharacters(str1,str2)
output.sort()
print("Normal - ",output)
output.reverse()
print("Reverse - ",output)

