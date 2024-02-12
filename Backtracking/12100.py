# 1. 모든 경우의 수를 비교(조건을 만족하는)해서 최댓값 찾기 -> DFS(백트래킹)
# 시작 노드: depth (종료조건에 필요)
# 이동 조건: 상하좌우
# 종료 조건: 5번 이동하면 종료
# 정답 찾기: 종료시 현재 보드 중에 가장 큰 값을 비교하여 최댓값으로 갱신

# 2. 이동 과정: 절차가 복잡 -> 시뮬레이션
# input: idx (상하좌우) return: 바뀐 board

# 위로: y는 고정, x는 작은 수부터
# 아래로: y는 고정, x는 큰 수부터
# 오른쪽으로: x는 고정, y는 큰 수부터
# 왼쪽으로: x는 고정, y는 작은 수부터

# 직전의 숫자와 현재 숫자를 비교하는 방법: pointer로 직전 인덱스 표시
# 직전 숫자가 0일 때, 현재 숫자가 0이 아니면 직전 인덱스에 현재 수 넣기
# 직전 숫자가 현재 숫자와 같을 때, 현재 숫자 x 2를 한 값을 직전 인덱스에 넣고, 현재 숫자는 0으로 만들고, 직전 인덱스와 현재 인덱스를 옮긴다.
# 직전 숫자가 현재 숫자와 다를 때, 현재 인덱스를 옮긴다.

import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def move(dir, board):
  if dir == 0:    # 위
    for j in range(n):   # 고정된 y별로
      pointer = 0
      for i in range(1, n):  # x는 작은 순서대로
        if board[i][j]:      # 현재 보드의 값이 0이 아닐 때 (결론 보드 값에는 윗부분에는 0이 없어야 함)
          current = board[i][j]  
          board[i][j] = 0   
          # 포인터가 가리키는 수가 0일 때
          if board[pointer][j] == 0:     
            board[pointer][j] = current  
          # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
          elif board[pointer][j] == current: 
            board[pointer][j] *= 2
            pointer += 1
          # 포인터가 가리키는 수와 현재 위치의 수가 다를 때  
          else: 
            pointer += 1
            board[pointer][j] = current
  elif dir == 1:    # 아래
    for j in range(n):
      pointer = n-1
      for i in reversed(range(n)):
        if board[i][j]:
          current = board[i][j]
          board[i][j] = 0
          if board[pointer][j] == 0:
            board[pointer][j] = current
          elif board[pointer][j] == current:
            board[pointer][j] *= 2
            pointer -= 1
          else:
            pointer -= 1
            board[pointer][j] = current
  elif dir == 2: # 오른쪽
    for i in range(n):   # 고정된 x별로
      pointer = n-1
      for j in reversed(range(n)):   # y는 큰 순서대로
        if board[i][j]:
          current = board[i][j]
          board[i][j]=0
          if board[i][pointer] == 0:
            board[i][pointer] = current
          elif board[i][pointer] == current:
            board[i][pointer] = current*2
            pointer -= 1
          else:
            pointer -= 1
            board[i][pointer] = current
  else: # 왼쪽
    for i in range(n):
      pointer = 0
      for j in range(1,n):
        if board[i][j]:
          current = board[i][j]
          board[i][j] = 0
          if board[i][pointer] == 0:
            board[i][pointer] = current
          elif board[i][pointer] == current:
            board[i][pointer] = current*2
            pointer += 1
          else:
            pointer += 1
            board[i][pointer] = current
  return board


# board를 각 dfs마다 분리하고 싶은데 어떻게 해? 인자로 이동시켜
def dfs(board, depth):
  global answer

  if depth == 5:
    for row in board:
      answer = max(answer, *row)
    return
  
  for i in range(4):   # 상하좌우
    tmp_board = move(i, copy.deepcopy(board))
    dfs(tmp_board, depth+1)

dfs(board, 0)
print(answer)