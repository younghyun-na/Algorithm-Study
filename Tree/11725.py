# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램

from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = defaultdict(list)
answer = list(0 for _ in range(n+1))
answer[1] = 1

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(x):
  for node in graph[x]:
    if answer[node] == 0:
      answer[node] = x
      dfs(node)

dfs(1)

for i in range(2, n+1):
  print(answer[i])

