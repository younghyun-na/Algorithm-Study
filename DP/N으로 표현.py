from collections import defaultdict

def solution(N, number):
	# dp[i]: N을 i번 사용해서 만들 수 있는 수들의 집합
    dp = defaultdict(set)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # NNN...N
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0: 
                        dp[i].add(n1 // n2)  # 0으로 나눌 수 없음
        print(dp)

        if number in dp[i]: 
            return i         # N을 i번 사용해서 number를 만들 수 있음
    
    return -1   # 최솟값이 8번보다 클 경우