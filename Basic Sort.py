class BasicSort:
    def bubble_sort(self, array):
        for i in range(len(array)-1,0,-1):
            for j in range(i):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array 

    def selection_sort(self, array):
        for i in range(len(array)-1):
            min_index = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            # if i != min_index:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
        return array

    def insertion_sort(self, array):
        for i in range(1, len(array)):
            temp = array[i]
            j=i-1
            while temp < array[j] and j > -1:
                array[j+1] = array[j]
                array[j] = temp
                j-=1
        return array

    def custom_sort(self, array):
        sorts = []
        min_index = min(array)
        for i in range(len(array)):
            sorts.append(min(array))
            min_index = min(array)
            array.pop(array.index(min_index))
        return sorts

array = [7,7,7,1,4,1,0,-2,-1,-45,7,0]

basic_sort = BasicSort()
print(basic_sort.bubble_sort(array))
print(basic_sort.selection_sort(array))
print(basic_sort.custom_sort(array))
print(basic_sort.insertion_sort(array))