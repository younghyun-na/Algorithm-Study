from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque()
    sum = 0
    time = 0
    while (truck_weights):

        if queue :
            sum = 0
            for i in range(len(queue)):
                sum += queue[i][0]

            if queue[0][1] == bridge_length:
                sum -= queue[0][0]
                queue.popleft()

            if (sum + truck_weights[0] <= weight) & (len(queue) < bridge_length):
                queue.append([truck_weights[0],0])
                truck_weights.pop(0)

            for i in range(len(queue)):
                queue[i][1] += 1

        else:
            queue.append([truck_weights[0], 1]) 
            truck_weights.pop(0)
        
        time += 1

    return time + bridge_length

