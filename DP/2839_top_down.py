n = int(input())
cache = {3: 1, 5: 1}

def dp(x):

  if x < 3:
    return -1

  elif x not in cache:
    if x % 5 == 0:       # 5의 배수면 5로만 사용하기
      cache[x] = dp(x-5)+1
    elif x % 3 == 0:     # 5의 배수가 아니면서 3의 배수면 일단 3하나 사용 
      cache[x] = dp(x-3)+1
    elif dp(x-5) > 0 and dp(x-3) > 0:
      cache[x] = min(dp(x-5)+1, dp(x-3)+1)
    else:
      cache[x] = -1
  
  return cache[x]

print(dp(n))



