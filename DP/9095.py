# dp(1) = 1
# dp(2) = 2
# dp(3) = 4

# dp(4) = dp(3) + dp(2) + dp(1) =  7

T = int(input())

for _ in range(1, T+1):
  n = int(input())

  cache = {1: 1, 2: 2, 3: 4}

  def dp(x):

    if x in cache:
      return cache[x]
    
    cache[x] = dp(x-3) + dp(x-2) + dp(x-1)

    return cache[x]

  print(dp(n))