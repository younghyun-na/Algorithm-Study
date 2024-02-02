# 점화식
# 해당 좌표까지 쌓아올린 최댓값 = 해당 좌표 전까지 쌓아올린 최댓값 + 해당 좌표 값
# dp(3, 0) = max(dp(4, 0), dp(4,1)) + 2

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cache = {}
for i in range(n):
  cache[(n-1, i)] = board[n-1][i]

def dp(x, y):

  if (x, y) in cache:
    return cache[(x, y)]
  
  cache[(x, y)] = max(dp(x+1, y), dp(x+1, y+1)) + board[x][y]

  return cache[(x, y)]

print(dp(0, 0))
