n = int(input())
arr = list(map(int, input().split()))
target = arr[-1]

cache = {}

def dp(i, partial_sum):
    if i == n-1:
        if partial_sum == target:
            return 1
        return 0
    
    if (i, partial_sum) in cache:
        return cache[(i, partial_sum)]
    
    ret = 0
    if partial_sum - arr[i] >= 0:
        ret += dp(i+1, partial_sum-arr[i])
    
    if partial_sum + arr[i] <= 20:
        ret += dp(i+1, partial_sum+arr[i])

    cache[(i, partial_sum)] = ret

    return ret

answer = dp(1, arr[0])
print(answer)