
# coding: utf-8

# In[165]:


import matplotlib.pyplot as plt
from math import log


# In[194]:


#The function for selection sort algorithm
def selection_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        min = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min]:
                min = j

        lst[i] = lst[min]
        lst[min] = key

    return lst

# To test the function
print(selection_sort([5, 4, 3, 2, 1]))

# import random

# This code is for qn no: 1.2.c. It is commented because we do not need it for final plot
# We do it different way
# NO_SEQ = 1
# RANDOM_SEQ = []
# for i in range(NO_SEQ):
#     RANDOM_SEQ.append([random.randrange(100) for n in range(45)])

# best_case = list(range(15))
# worst_case = best_case[::-1]


# In[230]:


# This may take few seconds to run
# Here, we compute the time taken to sort elements with diffrent n's 
# see(n_lists) 
# As said, we take 20 average cases and find the average time taken by them to run
# For best and worst cases we take single entry

from time import time

time_slot_worst = []
time_slot_best = []
time_slot_average = []
n_lists = list(range(1, 650, 15))
length_avg_figures = 20
for n in n_lists:
    average_case = []
    for i in range(length_avg_figures):
        average_case.append([random.randrange(10000) for i in range(n)])
    
    best_case = list(range(n))
    worst_case = best_case[::-1]
    
    start = time()
    _ = selection_sort(worst_case)
    check_pt1 = time()
    _ = selection_sort(best_case)
    check_pt2 = time()
    
    for i in average_case:
        _ = selection_sort(i)
        
    check_pt3 = time()
    
    time_slot_worst.append(check_pt2-start)
    time_slot_best.append(check_pt2-check_pt1)
    time_slot_average.append((check_pt3-check_pt2)/length_avg_figures)


# In[277]:


# Graph time
# Comment the plt.savefig and uncomment plt.show if you 
# want to show the figure temporarily instead of saving it directly
# in you drive

plt.figure(1)

plt.subplot(221)
plt.title('Worst Case')
plt.xlabel('n---->')
plt.ylabel('time---->')
plt.plot(n_lists, time_slot_worst, 'r-')
plt.plot(n_lists, [0.0000002 * (n**2) for n in n_lists], 'b--')
plt.plot(n_lists, [0.00000009 * (n**2) for n in n_lists], 'b--')
plt.savefig('worst_case_time_plot.pdf')
#plt.show()

plt.subplot(222)
plt.title('Best case')
plt.xlabel('n---->')
plt.ylabel('time---->')
plt.plot(n_lists, time_slot_best, 'r-')
plt.plot(n_lists, [0.000000095 * (n**2) for n in n_lists], 'b--')
plt.plot(n_lists, [0.00000002 * (n**2) for n in n_lists], 'b--')
plt.savefig('best_case_time_plot.pdf')
#plt.show()

plt.subplot(223)
plt.title('Average case')
plt.xlabel('n--->')
plt.ylabel('time--->')
plt.plot(n_lists, time_slot_average, 'r-')
plt.plot(n_lists, [0.0000001 * (n**2) for n in n_lists], 'b--')
plt.plot(n_lists, [0.00000004 * (n**2) for n in n_lists], 'b--')

plt.subplots_adjust(wspace=0.45, hspace=0.5)

plt.savefig('average_case_time_plot.pdf')
#plt.show()

