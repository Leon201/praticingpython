data = [9, 5, 7, 4, 2, 8, 10, 6, 3]
# data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]


def mergeSort(list):
    # Determine whethre the list is broken into
    #  individual pieces
    if len(list) < 2:
        return list

    # Find the middle of the list
    middle = len(list) // 2

    # 除号需要用两个// 因为一个是换行把

    # Break the list into two pieces.
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    # Merge the two sorted pieces into a larger piece.
    print("left side: ", left)
    print("Right side: ", right)
    merged = merge(left, right)
    print("Merged ", merged)
    return merged


def merge(left, right):
    # When the left side or the right side is empty.
    # it meas that this is an individual item and is
    # already sorted.
    # 这里不是很理解，如果是空的不是应该返回另外一步分吗，直接返回是什么意思
    # 只要一个是空的，那和其他的部分是哟过merge函数的时候，永远返回的都是空的

    if not len(left):
        return left
    if not len(right):
        return right

    # Define variables used to merge the two pieces.
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # Keep working until all of the items are merged.
    while (len(result) < totalLen):

        # Perform the required comparisons and merge
        # the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        # When the left side r the right is longer,
        # add the remaining elements to the result.
        if leftIndex == len(left) or \
                rightIndex == len(right):
            result.extend(left[leftIndex:]
                          or right[rightIndex:])
            break
    return result

mergeSort(data)