data={"a":5,"b":8,"c":11}
y=dict(sorted(data.items(), key=lambda x:x[1]))
print(y)