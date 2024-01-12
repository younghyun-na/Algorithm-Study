N, M = map(int, input().split())
arr = list(i for i in range(1, N+1))  
answer = []

def dfs(perm, depth):
  if len(perm) == M:     
    answer.append(perm.copy())   
    return
  elif depth == N:    
    return

  for i, val in enumerate(arr):   
    if i < depth:
      continue
    perm.append(val)
    dfs(perm, i)
    perm.pop()

dfs([], 0)
for i in range(len(answer)):
  print(' '.join(map(str, answer[i]))) 