# Input from the user
N = int(input("Enter the dimension N of the square matrix: "))
a=[]
for i in range(N):
    k = list(map(int, input().split()))
    a.append(k)
# print(N)
# Find the sum of diagonal elements
c=0 #principal_sum 
d=0 #non_principal_sum 
for i in range(N):
    c += a[i][i]
    #d += a[i][N-1]
    #N=N-1
    d += a[i][N - 1 - i]
# print(N)

print(f"Sum of principal diagonal elements: {c}")
print(f"Sum of non-principal diagonal elements: {d}")

#3rd one 
# Check if the matrix is upper triangular
is_upper = True
for i in range(N):
    # print(N)
    for j in range(0, i):
        if a[i][j] != 0:
            is_upper = False
            break

# Check if the matrix is lower triangular
is_lower = True
for i in range(N):
    for j in range(i + 1, N):
        if a[i][j] != 0:
            is_lower = False
            break

if is_upper and is_lower:
    print("The matrix is both upper and lower triangular.")
elif is_upper:
    print("The matrix is upper triangular.")
elif is_lower:
    print("The matrix is lower triangular.")
else:
    print("The matrix is neither upper triangular nor lower triangular.")