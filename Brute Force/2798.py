N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
result = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range (j+1, N):
            sum = arr[i] + arr[j] + arr[k]
            if sum > M:
                continue
            else:
                result = max(result, sum)
print(result)

