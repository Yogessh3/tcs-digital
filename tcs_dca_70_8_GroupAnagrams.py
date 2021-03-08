def groupAnagrams(words):
    sortedWords={}
    ans=[]
    for word in words:
        sortedWord=''.join(sorted(word))
        if sortedWord not in sortedWords:
            sortedWords[sortedWord]=[word]
        else:
            sortedWords[sortedWord].append(word)
    for word in sortedWords.values():
        ans.append(word)
    return ans
words=input().split()
print(words)
answers=groupAnagrams(words)
print(*answers)
    