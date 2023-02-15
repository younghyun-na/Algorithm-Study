from itertools import permutations

def solution(numbers):
    num_list = []
    decimals = []
    answer = 0

    for i in range(1, len(numbers)+1):
      decimals += list(permutations(numbers, i))
    
    for decimal in decimals:
      num_list.append(int(("".join(decimal))))
    
    num_list = list(set(num_list))

    for num in num_list:
      if num < 2:
        continue
      check = True
      for i in range(2, num):
        if num % i == 0:
          check = False
          break
      if check:
        answer += 1
    
    return answer

