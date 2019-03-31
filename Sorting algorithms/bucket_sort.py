from insertion_sort import insertion_sort as sort
from math import floor

def bucket_sort(arr_):
    arr = arr_.copy()
    
    C = []
    n = len(arr)
    
    B = [[] for _ in range(n)]

    for i in range(n):
        B[floor(n * arr[i])].append(arr[i])

    for i in  range(n):
        temp_arr = sort(B[i])
        C += temp_arr
    return C

if __name__=='__main__':
    sorted_arr = bucket_sort([0.9, 0.1, 0.6, 0.7, 0.6, 0.3, 0.1])
    print(sorted_arr)
