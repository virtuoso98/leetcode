def selection_sort(arr):
    l = len(arr)
    for i in range(0, l - 1):
        min = i
        for j in range(i + 1, l):
            if arr[j] < arr[min]:
                min = j
        if min != i :
            arr[i], arr[min] = arr[min], arr[i]
    return arr


