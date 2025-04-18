# 이 코드는 잘못된 코드다.
# 예제에선 단순히 boolean 값으로 리턴했기때문에 배열을 정렬해서 투포인터 방식으로 할 수 있었지만,
# 지금 이 문제는 조건을 만족하는 값의 인덱스를 반환해야하기때문에 정렬을 사용하면 인덱스가 바뀌어서 인덱스를 사용해선 안된다.


# Bad Case
class Solution:
    def twoSum(self, nums, target):
        result = []
        nums = sorted(nums)

        for i in range(len(nums)):
            for k in range(len(nums),0, -1):
                if nums[i] + nums[k] == target:
                    result.append(i)
                    result.append(k)
                    return result

sol = Solution()

print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))

