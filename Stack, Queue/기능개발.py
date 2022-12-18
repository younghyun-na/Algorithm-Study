import math

def solution(progresses, speeds):
    stack = []
    days = []
    answer = [0] * len(progresses)
    i = 0

    for j in range(len(progresses)):
        days.append(math.ceil((100-progresses[j])/speeds[j]))

    for day in days:

        if stack:

            if day > stack[-1]:
                stack.pop()
                stack.append(day)
                i += 1

        else:
            stack.append(day)
            
        answer[i] += 1
        
    return answer[0:i+1]
