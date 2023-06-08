from functools import lru_cache

village = []  

@lru_cache
def dp(i, j):
    
    global village

    if i == 0 and j == 0:  # 시작 좌표
        return 1

    if i < 0 or j < 0 or village[i][j] == -1:   # 물에 잠긴 곳
        return 0
    
    village[i][j] = dp(i-1, j) + dp(i, j-1)
   
    return village[i][j] % 1000000007

def solution(m, n, puddles):

    global village
    village = [[0 for _ in range(m)] for _ in range(n)]   # 0으로 초기화

    for j, i in puddles:   # 웅덩이는 -1로 표시
        village[i-1][j-1] = -1

    answer = dp(n-1, m-1)
    return answer