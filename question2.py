o=list()
o2=list()
while True:
    n=int(input("enter for A: "))
    if n==-1:
        break
    o.append(n)
while True:
    N=int(input("enter for B: "))
    if N==-1:
        break
    o2.append(N)
#1st one 
op=set(o)
op2=set(o2)
#2nd one
print(op)
print(op2)
print("Union is: ",op|op2)
print("Intersection is: ",op&op2)
print("Difference is: ",op2-op)
print("Symmetric difference is: ",(op-op2)|(op2-op))
#3rd one
k=[]
for i in o:
    for j in o2:
        if i==j:
            k.append(i)
print("Intersection of two initial lists is: ",k)
#4th one
l=[]
nn=o+o2
for i in nn:
    if i not in l:
        l.append(i)
print("Union os two initial lists is: ",l)