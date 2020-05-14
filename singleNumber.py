from collections import defaultdict

class Solution(object):
    def singleNumber_checkList(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checkList = []

        for i in nums:
            if i in checkList:
                checkList.remove(i)
            else:
                checkList.append(i)

        return checkList.pop()

    def singleNumber_dict(self, nums):
        checkDict = defaultdict(int)
        for i in nums:
            checkDict[i] += 1
        for j in checkDict:
            if checkDict[j] == 1:
                return j

    def singleNumber_math(self, nums):
        # 2∗(a+b+c)−(a+a+b+b+c)=c
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_bit_manipulation(self, nums):
        # a⊕0=a
        # a⊕a=0
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        result = 0
        for i in nums:
            result ^= i
        return result

s = Solution()
print(s.singleNumber_bit_manipulation([1,1,2,2,3]))