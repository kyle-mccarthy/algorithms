def insertion_sort(a):
    j = 1
    while j < len(a):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
        j += 1
