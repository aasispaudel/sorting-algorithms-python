'''
HERMAN HOLLERITH VERSION OF RADIX SORT
COUTNS FROM MOST SIGNIFICANT DIGIT
'''

class Sort:
    def __init__(self, arr):
      self.arr = arr
   
    # Length of longest integer
    def __ml(self):
      f = max(map(lambda x: len(str(x)), self.arr))
      return f

    def __radix_sort(self, bucket_arr, i):
      # If no element in bucket or 1 element
      if len(bucket_arr) <= 1:
        return bucket_arr

      # After we have checked all the digits, if
      # the numbers are in same bucket they are same numbers
      if i < 0:
        return bucket_arr

      # Initialize the bucket
      # Time complexity: \theta(n)
      bucket = [[] for _ in range(10)]

      # add elements in the bucket
      # Time complexity: \theta(n)
      for arr in bucket_arr:
        index = (int)(arr // (10**(i))) % 10
        bucket[index].append(arr)

      # Call again to check for another index
      # T(n) = \theta(n) + \theta(n) + .... (k times)
      for b in range(len(bucket)):
        bucket[b] = self.__radix_sort(bucket[b], i-1)

      # flatten the bucket and return
      # T(n) <=  \theta(10n) = \theta(n) [Outer loop is
      #                               is independent of n]
      return [elem for b in bucket for elem in b]
        
        
    def radix_sort(self):
      return self.__radix_sort(self.arr, self.__ml()-1)

if __name__=='__main__':
  arr =  [6, 7, 4, 333, 22, 23, 21, 444, 123, 1233, 1123, 1, 0, 12, 440, 11, 1233]
  sorter = Sort(arr)
  print("Holerith sort", sorter.radix_sort())
