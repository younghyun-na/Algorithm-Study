from collections import deque

def solution(begin, target, words):

    if target not in words:   
        return 0

    def bfs(start): 
        queue = deque()
        queue.append([start, 0])   
        
        while queue:

            start, cnt = queue.popleft()
            
            if start == target:
                return cnt
            
            for word in words:
                difference = 0
                for i in range(len(word)):
                    if start[i] != word[i]:
                        difference += 1
                    
                if difference == 1:
                    queue.append([word, cnt+1])

        return 0   

    answer = bfs(begin)   
    return answer 
