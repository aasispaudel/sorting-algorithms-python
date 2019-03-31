'''
The variant of quicksort algorithm
Splits into 3 arrays using 2 pivots!
'''

'''
Class
(
@param arr: array to sort
       randomize: selects randomly two pivots if True
                  selects first two elements as pivots if False

@functions quick_sort() sorts the array
           partition runs the partition algorithm
)

'''

from random import randrange

class Quicksort:
    def __init__(self, arr, randomize=False):
        self.arr = arr.copy()
        self.size = len(arr)
        self.randomize = randomize

        
    '''
    This function calls itself recursively until the
    array is sorted
     '''
    def __quicksort(self, p, r):
        if p < r:
            q1, q2 = self.partition(p, r)
            
            self.__quicksort(p, q1-1)
            self.__quicksort(q1+1, q2-1)
            self.__quicksort(q2+1, r)

    def partition(self, p, r):
        if self.arr[p] > self.arr[p+1]:
            self.arr[p], self.arr[p+1] = self.arr[p+1], self.arr[p]

        self.arr[p+1], self.arr[r] = self.arr[r], self.arr[p+1]

        q1 = self.arr[p]
        q2 = self.arr[r]

        x = p+1
        y = r-1

        i = p+1
        
        while not (i > y):
            if self.arr[i] <= q1:
                self.arr[i], self.arr[x] = self.arr[x], self.arr[i]
                x += 1

            elif self.arr[i] >= q2:
                self.arr[i], self.arr[y] = self.arr[y], self.arr[i]
                y -= 1
                continue

            i += 1

        self.arr[x-1], self.arr[p] = self.arr[p], self.arr[x-1]
        self.arr[y+1], self.arr[r] = self.arr[r], self.arr[y+1]

        return x-1, y+1

            
            
    
    def quick_sort(self):
        self.__quicksort(0, self.size-1)
        return self.arr

def main():
    arr = list(range(45))[::-1]

    sorter = Quicksort(arr)
    print(sorter.quick_sort())

if __name__=='__main__':
    main()
