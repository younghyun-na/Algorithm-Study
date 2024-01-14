N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
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
  print(' '.join(map(str, answer[i])))