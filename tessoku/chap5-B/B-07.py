# 入力
T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

s = [0]*(T+2)
S = [0]*(T+2)

for i in range(N):
  s[L[i]+1] += 1
  s[R[i]+1] -= 1

# print(s)
for i in range(1, T+1):
  S[i] = S[i-1] + s[i]
  
# print(S)
for i in range(1, T+1):
  print(S[i])