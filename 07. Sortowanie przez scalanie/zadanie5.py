def scal(T, start, mid, end):
    i = start
    j = mid + 1
    # Przesuwamy elementy do odpowiednich miejsc
    while i <= mid and j <= end:
        if T[i] <= T[j]:
            i += 1
        else:
            # Jeśli element z prawej części jest mniejszy, przenosimy go do lewej
            temp = T[j]
            for k in range(j, i, -1):
                T[k] = T[k - 1]
            T[i] = temp 

            # Aktualizacja indeksów
            i += 1
            mid += 1
            j += 1

def merge_sort_in_place(T, start, end):
    # Rekurencyjne dzielenie listy na połowy
    if start < end:
        mid = (start + end) // 2
        merge_sort_in_place(T, start, mid)
        merge_sort_in_place(T, mid + 1, end)
        scal(T, start, mid, end)