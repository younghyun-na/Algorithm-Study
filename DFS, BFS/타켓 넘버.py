def dfs(numbers, sum, target):
    if numbers == []:
        if sum == target:
            return 1
        else:
            return 0
    return dfs(numbers[1:], sum + numbers[0], target) + dfs(numbers[1:], sum - numbers[0], target)

def solution(numbers, target):
    return dfs(numbers, 0, target)
    