words=['hello','active','book','ikigai','vwrtyp','swrtUI']
filter_words=[]
vow="aeiouAEIOU"
for word in words:
    flag=0
    for j in word:
        if j in vow:
            flag=1
            break
    if flag==0:
        filter_words.append(word)
print(filter_words)
