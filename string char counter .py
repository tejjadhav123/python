s='aaaabbbbbcccccdddddd'
k=''
for i in set(s):
    k=k+i+str(s.count(i))
print(k)
d={i:s.count(i) for i in s}
print(d)