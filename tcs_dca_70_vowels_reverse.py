def vowelsReverse(word):
    word=list(word)
    vowels='aeiouAEIOU'
    rev=[]
    for i in range(len(word)):
        if(word[i] in vowels):
            rev.append(word[i])
            word[i]=float("inf")
    rev.reverse()
    j=0
    for i in range(len(word)):
        if(word[i]==float("inf")):
            word[i]=rev[j]
            j+=1
    return ''.join(word)
word=input().strip()
print(vowelsReverse(word))