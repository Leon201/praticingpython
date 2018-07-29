import heapq
# 是不是堆队列的意思


data = {3: 'White', 2: 'Red', 1: 'Green', 5: 'Orange'
    , 4: 'Yellow', 7: 'Purple', 0: 'Magentan'}

heap = []
for key, value in data.items():
    heapq.heappush(heap, (key, value))
heapq.heappush(heap, (6, 'Teal'))
heap.sort()

for item in heap:
    print('Key: ', item[0], 'Value: ', item[1])

print('Item 3 contains: ', heap[3][1])
print('The maximum item is: ', heapq.nlargest(1, heap))
print('The maximum item is: ', heapq.nlargest(2, heap))
# 这里的n是代表输出的个数

# 如果数据是个map，.items()的方法直接可以得到key和value
# 括号，然后用逗号，怎么直接就变成数组了，push到了堆里
