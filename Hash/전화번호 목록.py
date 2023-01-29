def solution(phone_book): 

    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    for nums in phone_book: 
        prefix = "" 
        for num in nums: 
            prefix += num
        
            if prefix in hash_map and prefix != nums:       
                return False 
                
    return True
