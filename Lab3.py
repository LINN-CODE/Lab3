print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if not all(isinstance(item, int) for item in arr):
        arr_result = 2
    elif n < 10 and n != 0:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    elif n == 0:
        arr_result = 0
    else:
        arr_result = 1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr_2 = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
    arr_3 = []
    arr_4 = ['ET0735', 1, 2, 3, 4, 5, 'DevOPs']

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    # If >= 10 numbers are entered
    print("If >= 10 numbers are entered ")
    result = bubble_sort(arr_2, SORT_ASCENDING)
    print(result)

    # If 0 numbers are entered
    print("If 0 numbers are entered")
    result = bubble_sort(arr_3, SORT_ASCENDING)
    print(result)

    # If any of the values entered are not integers 
    print("If any of the value entered are not integers ")
    result = bubble_sort(arr_4, SORT_ASCENDING)
    print(result)
if __name__ == "__main__":
    main()


