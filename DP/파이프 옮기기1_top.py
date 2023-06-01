from functools import cache

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

@cache   # 특정 인풋에 대한 함수의 결과값을 저장한다.
# (i, j) = 파이프 끝 좌표, k = 방향 (0: 가로, 1: 세로, 2: 대각선)
def dp(i, j, k):
    # 종료 조건 
    if (i, j, k) == (0, 1, 0):   # 첫번째 좌표 
        return 1
    if not (0 <= i < n) or not (0 <= j < n):   # 인덱스 벗어남
        return 0
    if arr[i][j] == 1:   # 벽
        return 0
    
    answer = 0

    # 전 파이프의 끝 좌표 = 현재 파이프의 시작 좌표

    if k == 0:   # 현재 방향이 가로인 경우의 수: 전 방향이 가로 or 대각선
        answer += dp(i, j-1, 0)     
        answer += dp(i, j-1, 2)   

    elif k == 1:   # 현재 방향이 세로인 경우의 수: 전 방향이 세로 or 대각선
        answer += dp(i-1, j, 1)
        answer += dp(i-1, j, 2)

    else:   # 현재 방향이 대각선인 경우의 수: 전 방향이 가로 or 세로 or 대각선
        if arr[i-1][j] == 1:   # 대각선인 경우는 주위 칸이 모두 비어있지 않으면 불가능
            return 0
        if arr[i][j-1] == 1:
            return 0
        
        answer += dp(i-1, j-1, 0)
        answer += dp(i-1, j-1, 1)
        answer += dp(i-1, j-1, 2)

    return answer

a1 = dp(n-1, n-1, 0)
a2 = dp(n-1, n-1, 1)
a3 = dp(n-1, n-1, 2)

print(a1 + a2 + a3)