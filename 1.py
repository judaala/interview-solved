a=[1,8,-3,0,1,3,-2,4,5]
n=6
b = [[i,j] for i in a for j in a if i+j==n]
print(b)
c,d=list(),list()
d=list()
for i,j in b:
    c=[i,j]
    if c not in d:
        d.append(c)
print(d)
