def subarraySum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        currentSum = 0
        for j in range(i, n):
            currentSum += nums[j]
            if currentSum == k:
                count += 1

    return count

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(subarraySum(nums, k))