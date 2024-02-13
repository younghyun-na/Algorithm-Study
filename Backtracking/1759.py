# 18분

# 가능한 모든 조합: DFS (조합을 구한 후 정렬한 것이 답)
# 시작 노드: idx
# 방문 조건: X 방문할 때 안할 때 나눠서 모든 조합 구하기
# 방문 처리: 필요 X
# 종료 조건: comb 길이가 l인 경우, idx가 c인 경우
# 암호인 경우: 종료 조건 만족하면서 모음이 한 개 이상, 자음이 두 개 이상
# 정답 찾기: 배열 answer에 가능성 있는 암호 넣기

l, c = map(int, input().split())    # l = 암호 길이 c = 문자 종류
alphabets = list(map(str, input().split()))
alphabets.sort()
answer = []

def is_promising(code):
  m, z = 0, 0
  for x in code:
    if x in ['a', 'e', 'i', 'o', 'u']:
      m += 1
    else:
      z += 1
  if m >= 1 and z >= 2:
    return True
  else:
    return False

def dfs(idx, code):

  if len(code) == l:
    if is_promising(code):
      answer.append(code)
    return

  elif idx == c:
    return

  dfs(idx+1, code + alphabets[idx])
  dfs(idx+1, code)

dfs(0, '')

for code in answer:
  print(code)


