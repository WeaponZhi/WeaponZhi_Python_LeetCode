# -*- coding: utf-8 -*-
def twoSum(nums, target):
	map = {}
	for i in range(len(nums)):
		complement = target - nums[i]
		if complement in map:
			return [map[complement],i]
		else:
			map[nums[i]] = i

print(twoSum([3,2,4],6))