def binary_search(nums,target):
    low = 0 
    high =len(nums)-1
    count = 0
    while low <= high:
        count += 1 
        mid = (low+high)//2
        if nums[mid] > target:
            high = mid - 1 
        elif nums[mid] < target:
            low = mid + 1 
        else:   
            print('查找次数:',count)
            print('目标元素索引:',mid)
            return mid
    print('查找次数:',count)
    return '未找到'
def test():
    nums = [2,4,6,8,10,12,14]
    target = 10
    result = binary_search(nums,target)
    print(result)
test()