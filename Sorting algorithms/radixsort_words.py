'''
We use radix sort to sort the arrays wrt certain index
We come sorting from last

If word does not contain the respective index\
eg- cat category (index = 4) cat -> cat00
'''

'''Returns the ascii valueof word'''
def ascii(word, index):
    if len(word) > index:
        return ord(word[index])
    else:
        return 0

'''Sort the words wrt given index'''
def radix_sort(arr, index):
    k = max([ascii(word, index) for word in arr]) + 1
    n = len(arr)
    
    C = [0 for _ in range(k)]
    
    for j in range(n):
        i = ascii(arr[j], index)
        C[i] = C[i] + 1

    for j in range(1, k):
        C[j] += C[j-1]
    
    B = ['' for _ in range(n)]
    
    for j in range(n-1, -1, -1):
        i = ascii(arr[j], index)
        B[C[i]-1] = arr[j]
        C[i] -= 1

    return B

'''Sort the words step by step from last to first'''
def word_sort(words_):
    words = words_.copy()
    
    k = max([len(word) for word in words])
    n = len(words)

    for j in range(k-1, -1, -1):
        words = radix_sort(words, j)

    return words


if __name__=='__main__':
    words = ["word", "category", "cat", "new", "news", "world", "bear", "at", "work", "time"]

    print(word_sort(words))
