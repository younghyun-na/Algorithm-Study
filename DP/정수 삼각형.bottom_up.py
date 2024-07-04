def solution(triangle):
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):

            if i == 0:
                continue
 
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]

            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]

            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])


