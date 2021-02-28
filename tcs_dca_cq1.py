def simplifyStringUsingBuiltIn(string):
    string=string.replace('8',"")
    string=string.replace('53',"")
    return ''.join(string).lower()
def simplifyStringWithoutBuiltIn(string):
    newString=[]
    i=0
    while i<len(string):
        if string[i]=='8':
            i+=1
        elif i+1<len(string) and string[i]=='5' and string[i+1]=='3':
            i+=2
        else:
            newString.append(string[i])
            i+=1
    return ''.join(newString).lower()
string=input()
if string.isalnum():
    str1=simplifyStringUsingBuiltIn(string)
    str2=simplifyStringWithoutBuiltIn(string)
    print(str1)
    print(str2)
else:
    print("Invalid Input")

