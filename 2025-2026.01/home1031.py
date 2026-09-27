'''
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
input_str = input("请输入一个字符串：")
upper, lower = count_case(input_str)
print(f"大写字母个数：{upper}")
print(f"小写字母个数：{lower}")
'''
def min_max(a, b, *rest):
    values = (a, b) + rest
    return min(values), max(values)
if __name__ == "__main__":
    min_value, max_value = min_max(3, 1, 4, 1, 5, 9, 2, 6)
    print(f"最小值: {min_value}, 最大值: {max_value}")