x, nums = input(), input().split()
print(all(map(lambda x: int(x) > -1, nums))
      and any(map(lambda x: x == x[::-1], nums)))
