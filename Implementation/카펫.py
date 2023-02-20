def solution(brown, yellow):
    s = brown + yellow
    yellow_estimated = -1

    for width in range(1, s+1):
        height = s // width

        if s % width == 0 and width >= height:
            if (height < 3):
                yellow_estimated = 0
            else:
                yellow_estimated = (height - 2) * (width - 2)
                
        if yellow_estimated == yellow:
            return [width, height]
            
