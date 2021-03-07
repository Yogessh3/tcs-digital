def isAnagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
str1,str2=input().split()
print(isAnagram(str1,str2))