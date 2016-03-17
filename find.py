import collections

with open ("find.txt")as f:
    content=f.read()
"".join(content)
y=list(content)
l= collections.Counter(y)

print (l)

