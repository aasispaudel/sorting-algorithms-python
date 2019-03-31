'''
@Reference: Mohit Kumra
https://www.geeksforgeeks.org/heap-sort/

'''


class Heapsort:
    def __init__(self, arr):
        self.arr = arr;
        self.n = len(arr)

    def heap_sort(self, variant=False):
        #Build the max
        for i in range(self.n, -1, -1):
            self.heapify(self.n, i)

        for i in range(self.n-1, 0, -1):
            #Swap the last leaf and root
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            # heapify again since we change our heap
            if not variant:
                self.heapify(i, 0)
            else:
                self.heapify_alternative(i, 0)


    def heapify(self, k, i):
        largest = i
        left = 2*i +1
        right = 2*i + 2

        # SWAP left child and root if existing left child is bigger
        if left < k and self.arr[i] < self.arr[left]:
            largest = left

        # SWAP right child and root if existing right child is bigger
        if right < k and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i] # SWAP
            # Call heapify recursively
            self.heapify(k, largest)

            
    def heapify_alternative(self, k, i):
        self.fall(k, i)
        self.climb(i)

    def climb(self, i):
        # If parent smaller than child: Well! swap them check further
        if self.arr[i//2] < self.arr[i]:
            self.arr[i], self.arr[i//2]= self.arr[i//2], self.arr[i]
            climb(self.arr, parent(i))

    def fall(self, k, i):
        left= 2*i +1
        right= 2*i +2

        # We are at the end
        if left >= k:
            return

        # Only one child! SWAP with it
        elif right >= k:
            self.arr[i], self.arr[left] = self.arr[left], self.arr[i]

        largest = i
        # else both are smaller? SWAP with the bigger one
        if left < k and right < k: 
            if self.arr[left]>self.arr[right]:
                self.arr[i],self.arr[left]=self.arr[left],self.arr[i]
                largest=left
                
            else:
                self.arr[i],self.arr[right]=self.arr[right],self.arr[i]
                largest=right

    
        # Like in heapify try to go to bottom
        if largest != i:
            self.fall(k, largest)


            
def main():
    arr = list(range(45))[::-1]
    
    h1 = Heapsort(arr)

    print(h1.heap_sort())

    print(h1.heap_sort(variant=True))
            
main()
