def chunk_generator(lis,size):
    start = 0
    while start < len(lis):
        yield lis[start:start + size]
        start = start +size
lis = [1,2,3,4,5,6,7]
size = int(input('你要怎样的数据？  ：'))
for num in chunk_generator(lis,size):
    print(num)