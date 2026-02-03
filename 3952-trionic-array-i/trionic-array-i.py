class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False

        i = 1

       
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False

       
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        if i == n:
            return False


        while i < n and nums[i] > nums[i - 1]:
            i += 1

        return i == n

        