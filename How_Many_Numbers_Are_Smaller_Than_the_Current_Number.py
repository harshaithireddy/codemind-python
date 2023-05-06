def smaller_numbers_than_current(nums):
    return [sum(num > n for n in nums) for num in nums]
    
    
n = int(input())
nums = list(map(int, input().split()))
for i in smaller_numbers_than_current(nums):
    print(i, end = " ")