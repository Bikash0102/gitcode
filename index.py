print("bikash")
a=b=[1,2]
print(a)
print(b)
a,b,c="abc"
print(a)
print(b)
print(c)
def bikash():
    print('bikash coder')

bikash()
b=[1,2,3,4,5,6]
for i in range (len(b)):
    print(b[i],end=" ")

c=[2,3,4,5,6,7]
c[1]=0
for i in c:
    print(i)



def evenodd(b):
    odd=[]
    even=[]
    for i in b:
        if(i%2==0):
            odd.append(i)
        else:
            even.append(i)
    return {'odd':odd,'even':even}

d={}
d=evenodd(c)
print(type(d))
print(d)

b=(2,2,3,4,5,6)
for i in b:
    print(i)

