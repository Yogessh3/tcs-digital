def func(variable):
    vow="aeiou"
    if variable in vow:
        return False
    return True
sequence=["a","e","p","o","g","i","%"]
filtered = filter(func,sequence)
for i in filtered:
    print(i)
