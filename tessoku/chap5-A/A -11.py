N, X = map(int, input().split())
A = list(map(int, input().split()))
# print(A)

def search(x,A):
  L = 0
  R = N-1
  while L <= R:
    M = (L + R)//2
    if x < A[M]:
      R = M - 1
    elif x == A[M]:
      return M
    elif x > A[M]:
      L = M + 1
    
ans = search(X, A)
ans +=  1
print(ans)
    