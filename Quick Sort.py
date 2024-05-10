def main():
    arr= read_file("numbers-4.txt")
    arr = quick_sort(arr)
    print(binary_search(arr, 90262))
    print(binary_search(arr, 11559))
    print(arr)


def quick_sort(array):
    if len(array) <= 1: # base case, array broken down into 1 or less elements
        return array

    pivot_index = len(array) // 2 # pivot is middle index
    pivot_value = array[pivot_index] # save pivots value

    left = [x for x in array if x < pivot_value] # create an array of all values less than pivot
    right = [x for x in array if x > pivot_value] # array of all values greater
    middle = [x for x in array if x == pivot_value] # all values equal to pivot

    return quick_sort(left) + middle + quick_sort(right) # recursive case

# copy file to array
def read_file(file):
    array = []
    with open(file, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    operations = 0

    while left <= right:
        operations += 1
        mid = (left + right) // 2

        if array[mid] == target:
            return mid, operations
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, operations

main()