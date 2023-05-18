def MaxOnes(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

n = int(input())
nums = list(map(int, input().split()))

res = MaxOnes(nums)
print(res)
