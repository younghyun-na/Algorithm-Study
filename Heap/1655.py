import sys
import heapq

N = int(input())
left_heap = []
right_heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left_max = heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)

        heapq.heappush(right_heap, -left_max)
        heapq.heappush(left_heap, -right_min)
        
    print(-left_heap[0])
