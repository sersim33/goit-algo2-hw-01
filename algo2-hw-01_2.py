def quickselect(arr, k):
    if not arr:
        raise ValueError("Порожній список")

    pivot = sorted(arr)[len(arr) // 2]  # обираємо медіану як pivot
    print(pivot)
    print("____")

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

arr = [38, 113, 43, 29, 9, 82, 44]
k = 4
print(quickselect(arr, k))
