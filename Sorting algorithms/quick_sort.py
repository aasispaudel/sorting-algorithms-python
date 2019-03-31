'''
@reference https://en.wikipedia.org/wiki/Quicksort
'''

class Quicksort:
    def __init__(self, arr, partition='LOMOTO', mid_pivot=False):
        self.arr = arr.copy()
        self.size = len(arr)
        self.partition = partition
        self.mid_pivot = mid_pivot


    def __find_mid_pivot(self, p, q):
        mid = (p+q) // 2

        if self.arr[mid] <  self.arr[p]:
            self.arr[p], self.arr[mid] = self.arr[mid], self.arr[p]
        if self.arr[q] < self.arr[p]:
            self.arr[p], self.arr[q] = self.arr[q], self.arr[p]
        if self.arr[mid] < self.arr[q]:
            self.arr[mid], self.arr[q] = self.arr[q], self.arr[mid]

        self.arr[p], self.arr[q] = self.arr[q], self.arr[p]
        
        return self.arr[p]
        
    def l_partition(self, p, q):
        if not self.mid_pivot:
            x = self.arr[p]
        elif self.mid_pivot:
            x = self.__find_mid_pivot(p, q)
            
        i = p + 1
        for j in range(p+1, q+1):
            if self.arr[j] <= x:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1

        self.arr[p], self.arr[i-1] = self.arr[i-1], self.arr[p]

        return i-1

    def __quicksort(self, p, r):
        if p < r:
        
            if (self.partition == 'LOMOTO'):
                q = self.l_partition(p, r)
            elif (self.partition == 'HOARE'):
                q = self.h_partition(p, r)

            self.__quicksort(p, q-1)
            self.__quicksort(q+1, r)

    def quick_sort(self):
        self.__quicksort(0, self.size-1)
        return self.arr

    def h_partition(self, p, q):
        if not self.mid_pivot:
            x = self.arr[p]
        elif self.mid_pivot:
            x = self.__find_mid_pivot(p, q)

        i = p - 1
        j = q + 1

        while True:
            i += 1
            while self.arr[i] < x:
                i += 1

            j -= 1
            while self.arr[j] > x:
                j -= 1
            
            if i >= j:
                return j

            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

def main():
    arr = [1, 1, 4, 3, 2, 7, 6, 5]
    sort1 = Quicksort(arr)
    sort2 = Quicksort(arr, partition='HOARE')
    sort3 = Quicksort(arr, mid_pivot=True)
    sort4 = Quicksort(arr, mid_pivot=True, partition='HOARE')

    print('lomuto:', sort1.quick_sort())
    print('hoare: ', sort2.quick_sort())
    print('lomuto with median_pivot', sort3.quick_sort())
    print('hoare with median_pivot', sort4.quick_sort())
    
if __name__=='__main__':
    main()
