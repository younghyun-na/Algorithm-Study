N, M = map(int, input().split())
arr = list(i for i in range(1, N+1))  # [1,...,N] 길이가 M인 수열 조합
answer = []

def dfs(comb, depth):
  if len(comb) == M:
    answer.append(comb.copy())
    return
  elif depth == N:  
    return

  comb.append(arr[depth])
  dfs(comb, depth + 1)

  comb.pop()
  dfs(comb, depth + 1)

dfs([], 0)
for i in range(len(answer)):
  # for ans in answer[i]:
  #   print(ans, end=' ')
  # print()
  print(' '.join(map(str, answer[i])))