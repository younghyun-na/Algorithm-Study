# 이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램

# 전위 순회: root -> 왼쪽 -> 오른쪽
# 중위 순회: 왼쪽 -> root -> 오른쪽
# 후위 순회: 왼쪽 -> 오른쪽 -> root

# dfs를 이용해서 원하는 순서대로 방문하도록
# --order(tree[root][0]) 재귀함수는 왼쪽으로 끝까지 탐색한다는 의미
# --order(tree[root][1]) 재귀함수는 오른쪽으로 끝까지 탐색한다는 의미

# 그래프 입력
n = int(input())
graph = {}
for _ in range(n):
  a, b, c = map(str, input().split())
  graph[a] = [b, c]

# 전위 순회
def preorder(x):  
  if x != ".":
    print(x, end = "")     # root
    preorder(graph[x][0])  # 왼쪽
    preorder(graph[x][1])  # 오른쪽

# 중위 순회
def inorder(x):
  if x != ".":
    inorder(graph[x][0])   # 왼쪽
    print(x, end = "")     # root
    inorder(graph[x][1])   # 오른쪽

# 후위 순회
def postorder(x):
  if x != ".":
    postorder(graph[x][0])  # 왼쪽
    postorder(graph[x][1])  # 오른쪽
    print(x, end = "")      # root

preorder('A')
print("")
inorder('A')
print("")
postorder('A')