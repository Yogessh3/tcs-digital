from collections import Counter
s=list('14553345')
string = ''
for key,count in Counter(s).most_common():
    string += key*count
print(string)
