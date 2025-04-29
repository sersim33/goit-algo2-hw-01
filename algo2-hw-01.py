def max_min_search(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) > 1:
        max_left, min_left = max_min_search(arr[:len(arr) // 2])
        max_right, min_right = max_min_search(arr[len(arr) // 2:])

        return max(max_left, max_right), min(min_left, min_right)


arr = [3, 9, 10, -22, 27, 38, 43, 82,112]
search = max_min_search(arr)
print(search) 
