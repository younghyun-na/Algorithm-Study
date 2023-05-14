n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# i번째까지 일했을 때의 최대 수익
d = [0] * (n+1)

for i in range(n):
    # i번째 날에 상담을 진행했을 때 얻을 수 있는 최대 수익
    # 모든 날에 i번째 날 상담 진행 여부와 관련해서 갱신을 시도
    for j in range(i + schedule[i][0], n+1):
        if d[j] < d[i] + schedule[i][1]:
            d[j] = d[i] + schedule[i][1]

print(d[-1])