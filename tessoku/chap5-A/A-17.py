N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


dp = [None]*(N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
  a = dp[i-1] + A[i-2]
  b = dp[i-2] + B[i-3]
  dp[i] = min(a,b)

place = N
Answer = []

while True:
  Answer.append(place)
  if place == 1:
    break
  
  if dp[place-1] + A[place-2] == dp[place]:
    place -= 1
  else:
    place-=2
    
# print(Answer)
K = len(Answer)
print(K)

Answer.reverse()

for i in range(K):
  print(Answer[i], end=" ")