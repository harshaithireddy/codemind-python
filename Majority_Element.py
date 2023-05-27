def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


n = int(input())
nums = list(map(int, input().split()))

print(majority_element(nums))
