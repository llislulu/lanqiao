def removeElement(nums, val):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow +=1
        fast +=1
    return slow
a=[3,2,2,3]

print(removeElement(a,3))