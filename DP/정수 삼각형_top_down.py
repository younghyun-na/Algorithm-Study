def solution(triangle):
    global N, T, cache
    T = triangle
    N = len(triangle)
    cache = [[None for _ in range(N)] for _ in range(N)]

    answer = dp(0,0)
    return answer

def dp(i, j):   # (i, j) 까지의 합
    if i == N-1:
        return T[i][j]
    if cache[i][j] is not None:
        return cache[i][j]

    cache[i][j] = max(dp(i+1, j), dp(i+1, j+1)) + T[i][j]
    
    return cache[i][j]