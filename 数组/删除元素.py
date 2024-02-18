def removeElement(nums, val):
    for i in nums:
        if i  == val:
            nums.remove(val)
    return len(nums)
a=[3,2,2,3]

print(removeElement(a,3))