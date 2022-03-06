
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1

    while i < len(list1):
        combined.append(list1[1])
        i+=1

    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined

def merge_sort(array):
    if len(array) == 1:
        return array
    
    middle = int(len(array)/2)
    left = array[:middle]
    right = array[middle:]
    return merge(merge_sort(left), merge_sort(right))


array1 = [7,6,7,1,4,1]
array2 = [0,-2,6,9,8,1,-45,7,0]

print(merge_sort(array1))