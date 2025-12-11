def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

user_input = input("Enter numbers separated by spaces: ")

arr = list(map(int, user_input.split()))

sorted_arr = bubble_sort(arr)

print("Sorted array: ", sorted_arr)