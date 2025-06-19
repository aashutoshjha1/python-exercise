#!/usr/bin/env python3

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                print(seen)
                return [seen[complement], i]
            seen[num] = i
            print(seen)


list2 = [2,4,5,6,7,9]
target = 9
class_obj = Solution()
print(class_obj.twoSum(list2,target))


