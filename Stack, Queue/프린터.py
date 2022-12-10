from collections import deque

def solution(priorities, location):

    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    answer = []

    while queue:
        
        if queue[0][0] == max(queue)[0]:
            # temp = queue[0]
            # queue.popleft()
            temp = queue.popleft()
            answer.append(temp)

        else:
            # temp = queue[0]
            # queue.popleft()
            temp = queue.popleft()
            queue.append(temp)


    for i in range(len(answer)):
        if answer[i][1] == location:
            return i+1
        
print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))