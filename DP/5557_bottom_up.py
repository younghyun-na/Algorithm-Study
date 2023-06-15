n = int(input())
arr = list(map(int, input().split()))
target = arr[-1]
dp =[[0 for _ in range(21)] for _ in range(n+1)]

# 처음 숫자 셋팅
dp[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
        	# 덧셈일 경우
            if 0 <= j+arr[i] <=20:
                dp[i][j+arr[i]] += dp[i-1][j]
                
            # 뺄셈일 경우
            if 0 <= j-arr[i] <= 20:
                dp[i][j-arr[i]] += dp[i-1][j]

# 입력받았던 숫자 중 마지막 숫자와 일치하는 경우의 수가 얼마인지 출력
print(dp[n-2][target])