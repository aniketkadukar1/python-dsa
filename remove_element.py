def removeElement(nums, val: int) -> int:
    result = 0
    start = 0
    end = len(nums) - 1
    
    while start < end :
        if nums[start] == val and nums[end] != val:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1 
        
        if nums[start] != val and nums[end] == val:
            start += 1
        
        if nums[start] == val and nums[end] == val:
            end -= 1
        
        if nums[start] != val and nums[end] != val:
            start += 1
    
    for i in range(len(nums)):
        if nums[i] != val:
            result += 1
    print(nums)
    
    return result


nums = [4, 5]
val = 5
print(removeElement(nums, val))