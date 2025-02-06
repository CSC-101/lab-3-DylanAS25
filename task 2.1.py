def tally(nums: list [int]) -> int:
    total = 0
    for num in nums:
        total = total + num

    return total
#num = 4 total = 3, num = 9 total = 13, num = 2 total = 15, num = 1 total = 16


result = tally([4,9,2,1])
print(result)