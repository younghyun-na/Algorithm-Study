# fib(3) = fib(2), fib(1)
# fib(2) = fib(1), fib(0)

T = int(input())

for _ in range(T):
  n = int(input())

  cache = {0: 0, 1: 1, 2: 1}

  def f(x):
    if x not in cache:
      cache[x] = f(x-1) + f(x-2)   # 계산한 적 없는 문제라면 피보나치 결과 반환하여 cache에 저장
    return cache[x]
  
  if n == 0:
    print('1 0')
  else:
    f(n)
    print(cache[n-1], cache[n])
