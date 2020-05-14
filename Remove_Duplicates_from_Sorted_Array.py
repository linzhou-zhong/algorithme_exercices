class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        
        head = 0
        tail = 1
        while (tail < len(nums)):
            if(nums[head] == nums[tail]):
                nums.pop(tail)
            else:
                head = tail
                tail += 1
            
        print(nums)
    
s = Solution()
s.removeDuplicates([1,1,2,2,3,4,4,5,6])