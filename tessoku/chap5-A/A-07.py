D = int(input())
N = int(input())

L = [None]*N
R = [None]*N

s = [0]*(D+2)
S = [0]*(D+2)

for i in range(N):
  L[i], R[i] = map(int, input().split())

for i in range(N):
  s[L[i]] += 1
  s[R[i]+1] -= 1


for i in range(1,D+1):
  S[i] = S[i-1] + s[i]
  
for i in range(1,D+1):
  print(S[i])