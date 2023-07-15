m= int(input("Type a number that represents M:"))
n = int(input("Type a number that represents N:"))

arr = [ [1]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        if not(i==0 or j==0):
            arr[i][j]= arr[i-1][j] + arr[i][j-1]

if (2*(10**9) < arr[m-1][n-1]):
    print("too big")
print(arr[m-1][n-1])
