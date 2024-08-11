N = int(input())
A = list(map(int,input().split()))
Q = int(input())

L = [ None ] * Q
R = [ None ] * Q
for j in range(Q):
	L[j], R[j] = map(int, input().split())

S = [None]* N
S[0] = A[0]
for i in range(1, N):
  S[i] = S[i-1] + A[i]

S.insert(0,0)

for i in range(Q):
  x = R[i] - L[i] + 1
  s = S[R[i]] - S[L[i]-1]
  z = s / x
  if z > 0.5:
    print("win")
  elif z == 0.5:
    print("draw")
  elif z < 0.5:
    print("lose")