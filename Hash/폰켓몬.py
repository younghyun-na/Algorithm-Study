def solution(nums):
    n = len(nums) // 2
    nums = set(nums)

    if len(nums) >= n:
        return n
    else:
        return len(nums)
    



