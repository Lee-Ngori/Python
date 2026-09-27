def selection_sort_report(nums):
    for i in range(len(nums)):
        min_index = i 
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
                print(nums)
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
nums = [29, 10, 14, 37, 13]
print(selection_sort_report(nums))