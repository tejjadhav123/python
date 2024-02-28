l=[i for i in [3,4,5,6,7,8,9] if all( i%x!=0 for x in range(2,i))]

print(l)