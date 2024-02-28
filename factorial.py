l=[1,2,3,4,5,6]
def f(n):
    if n==1:
        return 1
    return n*f(n-1)

print(f(5))
print('*********************************')
m=5
x=1
for i in range(m):
    x=x*(i+1)
print(x)



