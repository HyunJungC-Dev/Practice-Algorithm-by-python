def solution(array, target_value):
    array.sort()
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        if array[mid] == target_value:
            return mid
        elif target_value < array[mid]:
            right = mid
        else:
            left = mid+1
    return -1
