def isKey(words):
    keys=['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']
    if key.lower() in keys:
        return True
    return False
key=input()
if isKey(key):
    print(key,"is a keyword") 
else:
    print(key,"is not a keyword")