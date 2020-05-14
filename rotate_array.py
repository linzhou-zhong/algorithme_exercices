class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        return nums[-k:] + nums[:-k]

    def rotate_jump(self, nums, k):
        head = 0
        k %= len(nums)
        start = 0
        while start != len(nums):
            tmp_value = 
            

s = Solution()
print(s.rotate([1,2,3,4,5,6], 2))