def solution(genres, plays):
    dic1 = {}    
    dic2 = {}    
    answer = []

    for i, (g, p) in enumerate(zip(genres, plays)):
        dic1[g] = dic1.get(g, 0) + p

        if g not in dic2:
            dic2[g] = [(i, p)]
        else:
            dic2[g].append((i, p))

    for (k, v) in sorted(dic1.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic2[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer
