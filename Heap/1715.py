import heapq

N = int(input())
cards = []
result = 0

for i in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    plus = heapq.heappop(cards) + heapq.heappop(cards)
    result += plus
    heapq.heappush(cards, plus)

print(result)
