n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# dp[0][row][col] = 가로 파이프에 대한 dp
# dp[1][row][col] = 대각선 파이프에 대한 dp
# dp[2][row][col] = 세로 파이프에 대한 dp

# 1행에 가로 파이프 넣기
dp[0][0][1] = 1
for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]    # 왼쪽 칸의 가로 파이프


# 1행과 1열 제외 후 나머지 칸에 파이프 넣기
for r in range(1, n):
    for c in range(1, n):
        
        # 대각선 파이프 추가  
        if arr[r][c] == 0 and arr[r][c-1] == 0 and arr[r-1][c] == 0:
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r- 1][c-1]   # 위쪽 칸의 가로 파이프 + 위쪽 칸의 대각선 파이프 + 위쪽 칸의 세로 파이프
            
        # 가로, 세로 파이프 추가   
        if arr[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]    # 가로: 왼쪽 칸의 가로 파이프 + 왼쪽 칸의 대각선 파이프
            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]    # 세로: 위쪽 칸의 세로 파이프 + 위쪽 칸의 대각선 파이프

answer = 0
for i in range(3):
    answer += dp[i][n-1][n-1]

print(answer)
   
