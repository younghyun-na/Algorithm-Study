# 구현 8분, 에러 해결 5분

# n을 어떻게 채우는지에 대한 문제 -> 1짜리로 n번, 2짜리로 2//n번
# 마지막 타일을 1로 채울지 2로 채울지

# dp(1) = 1
# dp(2) = 2
# dp(3) = dp(1) + dp(2) = 3
# dp(4) = dp(2) + dp(3) = 5

# dp(x) = dp(x-2) + dp(x-1)

n = int(input())
cache = {1: 1, 2: 2}

def dp(x):

  if x in cache:
    return cache[x] 
  
  cache[x] = (dp(x-2) + dp(x-1)) % 10007

  return cache[x]

answer = dp(n) 

print(answer)
