def zeros_to_the_end(numbers):
    zeros = 0
    for value in numbers:
        if value == 0:
            zeros += 1
        else:
            yield value

    for _ in range(zeros):
        yield 0


print(list(zeros_to_the_end([1, 0, 2, 0, 0, 3, 6])))


def reverse_numbers(number):
    rev = 0
    while number > 0:
        remainder = number % 10
        rev = rev * 10 + remainder
        number = number // 10
    print(rev)


print(reverse_numbers(12345))


def hasArrayTwoCandidates(A, arr_size, sum):

    # sort the array
    quickSort(A, 0, arr_size-1)
    l = 0
    r = arr_size-1

    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0

# Implementation of Quick Sort
# A[] --> Array to be sorted
# si  --> Starting index
# ei  --> Ending index
def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi-1)
        quickSort(A, pi + 1, ei)

# Utility function for partitioning
# the array(used in quick sort)
def partition(A, si, ei):
    x = A[ei]
    i = (si-1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1

            # This operation is used to swap
            # two variables is python
            A[i], A[j] = A[j], A[i]

        A[i + 1], A[ei] = A[ei], A[i + 1]

    return i + 1

# Driver program to test the functions
# A = [1, 4, 45, 6, 10, -8]
# n = 16
# if (hasArrayTwoCandidates(A, len(A), n)):
#     print("Array has two elements with the given sum")
# else:
#     print("Array doesn't have two elements with the given sum")


def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]

    for i in range( 0, arr_size ):
        for j in range( i+1, arr_size ):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]

    return max_diff
