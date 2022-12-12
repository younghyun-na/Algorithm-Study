from collections import deque

def solution(priorities, location):

    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    answer = []

    while queue:
        
        if queue[0][0] == max(queue)[0]:
            temp = queue.popleft()
            answer.append(temp)

        else:
            temp = queue.popleft()
            queue.append(temp)


    for index in range(len(answer)):
        if answer[index][1] == location:
            return index+1
        