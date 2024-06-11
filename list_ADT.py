nums = [1, 2, 3, 4, 5, 6, 6, 12, 35, 7, 85]
nums.append(96)
for i in range(len(nums)):
    print(nums[i])


nums.insert(4, 827)
print(nums)

nums.remove(6)
print(nums)

nums.pop(2)
print(nums)

nums.pop()
print(nums)

nums.remove()
print(nums)