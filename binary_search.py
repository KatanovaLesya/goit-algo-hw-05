def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return iterations, arr[mid]

    if high >= 0 and arr[high] >= target:
        return iterations, arr[high]
    elif low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, None

# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
target = 1.2

iterations, upper_bound = binary_search(sorted_array, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
