def isPrime(N):
  limit = int(N**0.5)
  for i in range(2, limit+1):
    if N % i == 0:
      return False
  return True
      

Q = int(input())
X = [None]*(Q)

for i in range(Q):
  X[i] = int(input())
  
for i in range(Q):
  ans = isPrime(X[i])
  if ans==True:
    print("Yes")
  else:
    print("No")

