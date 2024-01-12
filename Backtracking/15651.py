N, M = map(int, input().split())
arr = list(i for i in range(1, N+1))  
answer = []

def dfs(perm):
  if len(perm) == M:
    answer.append(perm.copy())
    return 
  
  for val in arr:   
    perm.append(val)
    dfs(perm)
    perm.pop()

dfs([])
for i in range(len(answer)):
  print(' '.join(map(str, answer[i])))