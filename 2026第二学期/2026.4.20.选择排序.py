def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j 
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
def test():
    nums = [29,10,14,37,13]
    sorted_num = selection_sort(nums)
    print(sorted_num)
test()