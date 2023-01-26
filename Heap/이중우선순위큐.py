import heapq

def solution(operations):
    heap = []
    answer = []

    for op in operations:
        command, number = op.split(" ")

        if command == "I":
            heapq.heappush(heap, int(number))
        elif command == "D":
            if heap:
                if number == "-1":
                    heapq.heappop(heap)
                elif number == "1":
                    max_heap = heapq.nlargest(len(heap), heap)   
                    heap = max_heap[1:]    
                    heapq.heapify(heap)    

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)

    return answer

