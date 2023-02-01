def solution(participant, completion):
    data = dict()

    for person in set(participant):
        data[person] = 0
    
    for person in participant:
        data[person] += 1
    
    for person in completion:
        data[person] -= 1
    
    for key in data.keys():
        if data[key] == 1:
            return key

