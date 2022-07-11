N = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum_arr = [0] * N

total = 0

for i in range(N):  
    total += arr[i]
    sum_arr[i] += total

print(sum(sum_arr))