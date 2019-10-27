def sort(Arr, L, R):
    if L >= R:
        return

    M = L + ((R - L) >> 1)
    sort(Arr, L, M)
    sort(Arr, M+1, R)
    merge(Arr, L, M, R)

def merge(Arr, L, M, R):
    tmp = []
    i = L
    j = M+1

    while i <= M and j <= R and j < len(Arr):
        if Arr[i] < Arr[j]:
            tmp.append(Arr[i])
            i += 1
        else:
            tmp.append(Arr[j])
            j += 1

    while i <= M:
        tmp.append(Arr[i])
        i += 1

    while j <= R and j < len(Arr):
        tmp.append(Arr[j])
        j += 1

    Arr[L: R+1] = tmp[0: len(tmp)]


if __name__ == "__main__":
    arrTest = [0,-2, 0, 3, 4, 7,-10, -11, 2, 3, 3.1]
    sort(arrTest, 0, len(arrTest))
    print(arrTest)