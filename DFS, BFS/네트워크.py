def dfs(n, computers, start, visited):
    visited[start] = True
    for i in range(n):
        if computers[start][i] == 1 and visited[i] == False:
            dfs(n, computers, i, visited) 

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
          dfs(n, computers, i, visited)
          answer += 1
    return answer
