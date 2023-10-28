N=int(input("Enter the dimention of matrix: "))
a=[]
for i in range(N):
    k=(input(f"Enter vale of row {i+1} of matrix 1: ")).split()
    a.append(k)
#1st one
c,d=0,0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j]==a[j][i]:
            c+=1
        else:
            d+=1
if c==N*N:
    print("The matirx is symmetric.")
else:
    print('Matrix is not symmetric.')

#2nd one
t1=0
t2=0
for i in range(N):
    t1+=int(a[i][i])
    t2+=int(a[i][N-1])
    N-=1
print("Sum of principle diagonal elements: ",t1)
print("Sum of non-principle diagonal elements: ",t2)
#3rd one
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(j)
        if a[i][j]!=0:
            print("Upper triangular matrix.")
        