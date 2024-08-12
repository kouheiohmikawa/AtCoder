H, W = map(int, input().split())

X = [None]*(H+2)

for i in range(H):
  X[i] = list(map(int, input().split()))



Q = int(input())
A = [None]*(Q+2)
B = [None]*(Q+2)
C = [None]*(Q+2)
D = [None]*(Q+2)


for i in range(Q):
  A[i], B[i], C[i], D[i] = map(int, input().split())
  

Z = [ [ 0 ] * (W + 2) for i in range(H + 2) ]


for h in range(0, H):
  for w in range(0, W):
    Z[h][w] = Z[h][w-1] + X[h][w]
    

for w in range(W):
  for h in range(H):
    Z[h][w] = Z[h-1][w] + Z[h][w]
    

for q in range(Q):
  ans = Z[C[q]-1][D[q]-1] + Z[A[q]-2][B[q]-2] - Z[A[q]-2][D[q]-1] - Z[C[q]-1][B[q]-2]
  print(ans)