def checkEnglish(sentence):
    alpha=set()
    for letter in sentence:
        if letter.isalpha():
            letter=letter.lower()
            if (ord(letter)>=97 and ord(letter)<=122):
                alpha.add(letter)
    return len(alpha)==26
sentence=input()
if checkEnglish(sentence):
    print("YES")
else:
    print("NO")