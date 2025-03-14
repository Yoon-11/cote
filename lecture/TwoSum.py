class Solution(object):
    def twoSum(self, nums, target):
        output = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                   output.append(i)
                   output.append(j)
                   return output
        return False


sol = Solution()
print(sol.twoSum([4, 1, 9, 7, 5, 3, 16], 14))
print(sol.twoSum(nums=[3, 2, 4], target=6))
print(sol.twoSum(nums=[3, 3], target=6))

