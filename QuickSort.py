def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def pivot(array, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if array[i] < array[pivot_index]:
            swap_index +=1
        swap(array, pivot_index, swap_index)
    return swap_index

def quick_sort(array, left, right):
    if left<right:
        pivot_index = pivot(array, left, right)
        quick_sort(array, left, pivot_index-1)
        quick_sort(array, pivot_index+1, right)
    return array

def quickie(array):
    return quick_sort(array, 0, len(array)-1)
array = [0,3,5,2,6,7]
print(quickie(array))