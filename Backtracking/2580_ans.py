board = [list(map(int, input().split())) for _ in range(9)]

blanks = []  # 빈 칸의 좌표를 저장할 리스트
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blanks.append((i, j))

def is_promising(x, y, num):
    # 같은 행에 중복되는 숫자가 없는지 확인
    if num in board[x]:
      return False
    
    # 같은 열에 중복되는 숫자가 없는지 확인
    if num in [board[i][y] for i in range(9)]:
      return False
    
    # 3x3 칸에 중복되는 숫자가 없는지 확인
    start_row = (x // 3) * 3
    start_col = (y // 3) * 3

    for i in range(start_row, start_row + 3):
      for j in range(start_col, start_col + 3):
        if board[i][j] == num:
          return False
        
    return True

def dfs(idx):
  if idx == len(blanks):  # 모든 빈 칸을 채웠을 때
    for row in board:
      print(*row)
    exit(0)  # 정답을 찾았으면 프로그램 종료
  
  x, y = blanks[idx]  # 다음 빈 칸의 좌표
  for num in range(1, 10):
    if is_promising(x, y, num):
      board[x][y] = num  # 빈 칸에 숫자를 채우고
      dfs(idx + 1)  # 다음 빈 칸을 탐색
      board[x][y] = 0  # 원상태 복구

dfs(0)


