N, M = map(int, input().split())
arr = list(i for i in range(1, N+1))  
visited = [False for _ in range(len(arr))]
answer = []

def dfs(perm):
  if len(perm) == M:   # 종료 조건: M개 골랐을 때
    answer.append(perm.copy())
    return
  
  for i, val in enumerate(arr):   # 리스트 for문 처음부터 돌기
    if visited[i] == True:    # 방문했다면 건너뛰기
      continue

    perm.append(val)
    visited[i] = True
    dfs(perm)   
    perm.pop()
    visited[i] = False


dfs([])
for i in range(len(answer)):
  print(' '.join(map(str, answer[i])))


