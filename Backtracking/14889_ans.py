n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

people = []    # 조합을 생각하기 (0부터 n-1까지 or 1부터 n까지)
for i in range(n):
  people.append(i)

answer = float('inf')

def is_promising(team1):
  result1 = 0     # 한 팀의 능력치의 합
  for i in team1: 
    for j in team1:  
      result1 += board[i][j]
  result2 = 0

  team2 = [x for x in people if x not in team1]
  for i in team2: 
    for j in team2: 
      result2 += board[i][j]
  return abs(result2 - result1)

def dfs(idx, team):
  global answer

  if len(team) == n//2:
    answer = min(answer, is_promising(team))
    return

  elif idx == n:
    return
  
  dfs(idx+1, team + [idx])
  dfs(idx+1, team)
  
dfs(0, [])   
print(answer)