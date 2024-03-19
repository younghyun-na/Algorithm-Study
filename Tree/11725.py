# 1:03 ~ 
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램

# 1: 4 6
# 2: 4
# 3: 5 6 
# 4: 1 2 7
# 5: 3
# 6: 1 3
# 7: 4

# 4 -> 2 7
# 6 -> 3

from collections import defaultdict

n = int(input())
graph = defaultdict(list)
answer = list(0 for _ in range(n+1))
answer[1] = 1

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# for node in graph[1]:
#   answer[node] = 1

# 시작 노드: 1
# 방문 조건: graph[root], 이미 들린 노드 제외
  
def dfs(x):
  for node in graph[x]:
    if answer[node] == 0:
      answer[node] = x
      dfs(node)

dfs(1)

for i in range(2, n+1):
  print(answer[i])

