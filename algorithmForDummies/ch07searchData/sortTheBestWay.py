data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def partition(data, left, right):
    pivot = data[left]
    lIndex = left + 1
    rIndex = right

    # 先左边开始，一直找到比左边第一个要大的那个值
    # 然后从右边开始找，找到比右边第一个要大的那个值
    # 然后交换左右的位置
    # 然后继续向左，继续向右，一直到扫描完第一遍
    # 然后把最左边的和右边的index互换位置
    # 返回右边的index

    # 配合快速排序
    # 通过右边的index重新分区
    # 每次都使用左边的值作为分区条件，然后把比这个值大的放到右边
    #   比这个值小的放到左边，然后用个值分成两个区，然后继续做同样的事情
    while True:
        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
        if rIndex <= lIndex:
            break
        data[lIndex], data[rIndex] = \
            data[rIndex], data[lIndex]
        print(data)

    data[left], data[rIndex] = data[rIndex], data[left]
    print(data)
    return rIndex

def quickSort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quickSort(data, left, pivot - 1)
        quickSort(data, pivot + 1, right)

    return data

quickSort(data, 0, len(data) - 1)