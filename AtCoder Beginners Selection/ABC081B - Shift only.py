N = int(input())
A = list(map(int, input().split()))
ans = 0


def all_even(lst):
    return all(x % 2 == 0 for x in lst)

while all_even(A):
    ans += 1
    A = [x // 2 for x in A]

print(ans)