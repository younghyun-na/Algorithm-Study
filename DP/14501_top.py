n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

d = [0] * (n+1)

# 끝에서부터 내려오기
for i in reversed(range(n-1)):
    # i일에 상담을 하면 퇴사일이 넘긴다면 상담을 하지 않는다.
    if i + schedule[i][0] > n:
        d[i] = d[i+1]
    # i일에 상담을 했을 때의 금액과 안했을 때의 금액을 비교하여 큰 것을 선택한다.
    else:
        d[i] = max(d[i+1], schedule[i][1] + d[i + schedule[i][0]])

print(max(d))
