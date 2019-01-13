class Solution(object):
    def twoSum_orig(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for n in range(len(nums)):
            hashMap[nums[n]] = 1

        for n in range(len(nums)):
            diff = target-nums[n] 
            if diff in hashMap:
                idx2 = nums.index(diff)
                if idx2 != n:
                    return [n, idx2] 
                else:
                    return None
        return None

    def twoSum(self, nums, target):
        """
        Add num:index to a dict
        Check if target-num is in the dict
            If yes, return index of target-num and index of num

        Example:
        for 7, check if (5-7) in dict, not, put 7:0 into dict
        for 2, check (5-2) in dict, not, put 2:1 into dict
        11:2, 15:3, 
        for 3, check if (5-3) in nums, so return 3's index and saved (5-3)'s index
        """
        dictMap = {}
        for index, value in enumerate(nums):
            if target - value in dictMap:
                return dictMap[target - value], index
            dictMap[value] = index

s = Solution()
ret = s.twoSum([7,2,11,15,3], 5)
print(ret)

