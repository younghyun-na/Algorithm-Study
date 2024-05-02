N = int(input())
answer = 0
row = [0] * N

# 해당 노드가 유망한지 판단하는 함수 (x = 행)
def is_promising(x):
  # 지금의 전 행까지 모두 고려해서 현재 행과 비교 판단
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
  return True

def dfs(x):
  global answer

  if x == N:
    answer += 1
    return
        
  # 열 번호 0부터 N까지 돌면서 유망한 곳 찾기
  for i in range(N):
    # [x, i]에 퀸을 놓아보기
    row[x] = i
    if is_promising(x):   # [x, i]가 유망하다면 그대로 진행
      dfs(x+1)       
      # 배열에 추가하는 형식이 아니고 0을 다른 값으로 바꾸는 형태이므로 pop할 필요 없음

dfs(0)
print(answer)