N = int(input())
result = 0

for i in range(N):
    arr = list(map(int, str(i)))
    bunhae = i + sum(arr)
    
    if (bunhae == N):
        result = i
        break

print(result)

