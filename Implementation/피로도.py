from itertools import permutations

def solution(k, dungeons):
    answer = 0
    sequences = []

    for i in permutations(dungeons, len(dungeons)):
        sequences = list(i)
        current_k = k
        explored = 0

        for sequence in sequences:
            if sequence[0] > current_k:
                break
            else:
                current_k -= sequence[1]
                explored += 1

        answer = max(answer, explored)
    
    return answer

    
    
