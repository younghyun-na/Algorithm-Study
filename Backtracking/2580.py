# 10:54 ~ 11:03 ~ 11:27(구현 끝) ~ 

# 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성
# 스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

# 스도쿠 규칙에 맞는 숫자만 채워서 순열 구하기: 백트래킹(DFS)
# 시작 노드: start   ->  (x, y)
# 방문 조건: board에서 빈칸인 곳, 1부터 9까지 방문 가능
# 유망한 조건: 해당 노드가 들어감으로서, 가로줄에 1부터 9까지 있어야 함 
#             세로줄에 1부터 9까지 있어야 함 
#             3x3 정사각형 안에 1부터 9까지의 숫자가 있어야 함
# 종료 조건: 빈칸이 모두 채워졌을 때             
# 정답 찾기: board에 빈칸이 없을 때 해당 board 리턴

board = [list(map(int, input().split())) for _ in range(9)]

blanks = []   # 에러2(시간 초과): 빈 노드를 따로 보관하자
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blanks.append((i, j))

def is_promising(x, y, num):
  for i in range(9):
    if num == board[x][i]:
      return False
    if num == board[i][y]:
      return False
  
  start_square_x = (x // 3)  * 3
  start_square_y = (y // 3)  * 3

  for i in range(start_square_x, start_square_x + 3):
    for j in range(start_square_y, start_square_y + 3):
      if num == board[i][j]:
        return False
      
  return True

def dfs(idx):

  if idx == len(blanks):  # 에러1(실패): 빈 칸을 다 돌면 종료
    return    # 에러4(실패): 정답을 찾았으면 프로그램 종료 exit(0) 이 맞음
  
  nx = blanks[idx][0]
  ny = blanks[idx][1]

  for num in range(1, 10):
    if is_promising(nx, ny, num):
      board[nx][ny] = num
      dfs(idx+1)
      board[nx][ny] = 0   # 에러3(실패): 원상태 복구 (방문 취소 처리)를 해주지 않았다. 
        
dfs(0)

for i in range(9):
  for j in range(9):
    print(board[i][j], end=' ')
  print()

# for i in range(9):
#   print(*board[i])
