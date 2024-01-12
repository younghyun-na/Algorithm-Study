N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []
visited = [False for _ in range(N)]

def dfs(perm):
  if len(perm) == M:
    answer.append(perm.copy())
    return
  
  for i, val in enumerate(arr):
    if visited[i] == True:
      continue
    perm.append(val)
    visited[i] = True
    dfs(perm)
    perm.pop()
    visited[i] = False

dfs([])
for i in range(len(answer)):
  print(' '.join(map(str, answer[i]))) 