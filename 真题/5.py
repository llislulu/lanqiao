import os
import sys


def gcd_of_list(nums, g):
    if len(nums) < 2:
        return False
    sum = 0
    for i in nums:
        if i % g == 0:
            sum += 1
    if sum >= len(nums) - 1:
        return True


l = 0
n, g = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = 2
while left < (len(nums)):
    if gcd_of_list(nums[left:right], g):
        l += 1
        print(nums[left:right])
    right += 1
    if right >= len(nums):
        left += 1
        right = 2
print(l)