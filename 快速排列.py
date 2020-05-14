def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smallest = [i for i in array[1:] if i < pivot]
        biggest = [i for i in array[1:] if i >= pivot]
        return quicksort(smallest) + [pivot] + quicksort(biggest)

print(quicksort([2,1,3,5,1,5,6]))

