N = int(input())
A = list(map(int, input().split()))


ans = False
l = len(A)

for i in range(l):
  for j in range(i+1, l):
    for k in range(j+1, l):
      if A[i] + A[j] + A[k] == 1000:
        ans = True


if ans:
  print("Yes")
else:
  print("No")
