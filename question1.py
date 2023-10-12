op=list()
op2=list()
while True:
    n=int(input("enter: "))
    if n==-1:
        break
    op.append(n)
#1st one
for i in op:
    if i not in op2:
        op2.append(i)
print(op2)
#2nd one
op2=set(op2)
print(op2)