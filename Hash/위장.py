import collections

def solution(clothes):
    clothes_type = []
    
    for cloth in clothes:
        clothes_type.append(cloth[1])
    clothes_dic = collections.Counter(clothes_type)
    
    answer = 1
    for value in clothes_dic.values():
        answer *= (value + 1)
    
    return answer - 1