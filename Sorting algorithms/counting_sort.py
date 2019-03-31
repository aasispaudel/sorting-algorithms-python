def counting_sort(arr_):
    arr = arr_.copy()
    k = max(arr) + 1
    n = len(arr)
    
    C = [0 for _ in range(k)]

    for j in range(n):
        C[arr[j]] = C[arr[j]] + 1

    for j in range(1, k):
        C[j] += C[j-1]
    
    B = [0 for _ in range(n)]
    
    for j in range(n-1, -1, -1):
        B[C[arr[j]]-1] = arr[j]
        C[arr[j]] -= 1

    return B

if __name__=='__main__':
    print(counting_sort([9, 1, 6, 7, 6, 2, 1]))
        

    
