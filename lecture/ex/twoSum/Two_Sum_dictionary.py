def two_sum(nums, target):
    dic = {}
    for v in nums:
        dic[v] = 1

    for v in nums:
        n = target - v
        if n == v:
            continue
        if n in dic:
            return True
    return False

print(two_sum([4,1,9,7,5,3,16], 14))
print(two_sum([2,1,5,7], 4))