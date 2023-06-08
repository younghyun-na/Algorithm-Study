def solution(m, n, puddles):

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j, i] in puddles:
                dp[i-1][j-1] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

    return dp[n-1][m-1] % 1000000007

