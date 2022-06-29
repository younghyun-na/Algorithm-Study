N = int(input())
data = dict()
x = N

for i in range(N):
    nums = list(map(int, str(i)))
    bunhae = i + sum(nums)
    data[i] = bunhae

value_list = data.values()

if N in value_list:
    for i in range(N):
      if (data[i] == N):
        x = min(x, i)
else:
    x = 0

print(x)
