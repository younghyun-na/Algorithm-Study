def solution(answers):
    result = []

    person1 = []
    person2 = []
    person3 = []

    scores = [[1,0],[2,0],[3,0]]

    person1_answer = [1, 2, 3, 4, 5]
    person2_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    person3_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        person1.append(person1_answer[i%5])
        person2.append(person2_answer[i%8])
        person3.append(person3_answer[i%10])
    
    for i in range(len(answers)):
        if (person1[i] == answers[i]):
            scores[0][1] += 1
        if (person2[i] == answers[i]):
            scores[1][1] += 1
        if (person3[i] == answers[i]):
            scores[2][1] += 1    

    scores.sort(key=lambda x:x[1], reverse=True)
    
    for score in scores:
        if score[1] == scores[0][1]:
            result.append(score[0])

    return result
