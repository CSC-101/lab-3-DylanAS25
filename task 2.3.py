def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)

    return new_list
#value = 4 new_list = [5], value = 9 new_list = [5,10], value = 2 new_list = [5,10,3],
#value = 1 new_list = [5,10,3,2]


result = increment_all([4,9,2,1])