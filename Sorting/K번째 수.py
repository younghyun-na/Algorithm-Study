def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0] - 1
        j = command[1] - 1
        k = command[2]

        sliced = array[i : j+1]
        sliced.sort()
        answer.append(sliced[k-1])

    return answer    
