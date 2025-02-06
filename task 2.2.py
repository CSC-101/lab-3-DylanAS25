def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])

    return new_list
#idx=0 new_list =[], idx=1 new_list=[4,9], idx=2 new_list=[4,9,1]


result = copy([4,9,1])
print(result)

#the previous loop directly iterates through the list values. This loop iterates though the
#indecis and then uses them to access the list values. 