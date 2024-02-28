s=[1,2,3,4,5]
k=[]
m=[]
l=[]
for i in range(len(s)):
    k.append(s[-(i+1)])
print(k)
print('****************************************')
for i in s:
    m=[i]+m
print(m)