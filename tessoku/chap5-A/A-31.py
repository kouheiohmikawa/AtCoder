N = int(input())

A1 = N // 3
A2 = N // 5
A3 = N // 15

ans = A1 + A2 - A3
print(ans)