s = input()
l = len(s)

ans = 0
for i in range(l):
  if s[i] == "1":
    ans += 1

print(ans)