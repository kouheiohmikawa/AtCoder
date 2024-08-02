import bisect

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
Q = int(input())

X = [None]*Q
for q in range(Q):
  X[q] = int(input())
  
for q in range(Q):
  m = bisect.bisect_left(A, X[q])
  #m += 1
  print(m)