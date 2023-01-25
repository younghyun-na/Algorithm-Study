import heapq

def solution(jobs):
    sum = 0
    start = -1
    now = 0
    heap = []
    i = 0

    while i < len(jobs):

        for j in jobs:
 
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:
            perform = heapq.heappop(heap)
            start = now
            now += perform[0]
            sum += now - perform[1]
            i += 1
            
        else:
            now += 1

    return sum // len(jobs)

