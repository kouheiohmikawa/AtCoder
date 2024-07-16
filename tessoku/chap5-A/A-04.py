N = int(input())


for i in range(9, -1, -1):
  div = int(N / 2**i)
  rem = div % 2
  print(rem, end="")
