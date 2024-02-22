# dp(1) = 1
# dp(2) = 1
# dp(3) = 1

# dp(10) = dp(1) + dp(3) + dp(3) 
# dp(9) = dp(3) + dp(3)
# dp(6) = dp(3) + dp(2)

# 점화식: dp(x) = min(dp(1) + dp(x-1) , dp(x//3))
# 점화식: dp(x) = min(dp(1) + dp(x-1) , dp(x//2))

n = int(input())
cache = {1:0, 2:1, 3:1}

def dp(x):

  if x in cache:
    return cache[x]
  
  elif x % 3 == 0 and x % 2 == 0:
    cache[x] = min(dp(x//2) + 1, dp(x//3) + 1)
  
  elif x % 3 == 0:
    cache[x] = min(dp(x-1) + 1 , dp(x//3) + 1)

  elif x % 2 == 0:
    cache[x] = min(dp(x-1) + 1 , dp(x//2) + 1)
  
  else:
    cache[x] = dp(x-1) + 1

  return cache[x]

print(dp(n))

  
  

