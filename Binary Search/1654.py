# O(N)만 가능
# 가장 작은 랜선의 길이부터 시작해서 점점 줄여나가기

k, n = map(int, input().split())
arr = []
for _ in range(k):
  arr.append(int(input()))

s = 1        # 정답이 가능한 범위 중 가장 작은 값
e = max(arr)   # 정답이 가능한 범위 중 가장 큰 값

while s <= e:
  mid = (s + e) // 2
  result = 0
  for num in arr:
    result += num // mid
  if result >= n:   # n개 이상 만든 경우
    s = mid + 1
  else:             # n개 이상 못 만든 경우
    e = mid - 1

print(e)




  