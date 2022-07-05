


import random
from time import time

def mergeSort(arr):
    if len(arr) > 1:
    
        mid = len(arr)//2
        L = arr[:mid]       
        R = arr[mid:]     
        mergeSort(L)     
        mergeSort(R) 
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def load(path):
    list=[]
    with open(path) as f:
        for i in range(3):
            w = [int(x) for x in next(f).split()] 
            list.append(w)
    return(list)

def random_generate(sequence_count):
    
    n_list=[]
    input_list=[]
    for i in range(sequence_count):
        n_list.append(15000*(i+1))
        l = [random.randrange(0,10000) for i in range(n_list[i])]
        input_list.append(l) 
    return(input_list)
 
 
#----------main----------------

if __name__ == '__main__':
    sequence_count=12
    list=random_generate(sequence_count)

    for i in range(sequence_count):
        arr=list[i]
        t0 = time()
        mergeSort(arr)
        t1 = time()
        print('array size n = {}'.format(len(arr)), 'Time taken to sort = {}'.format(t1-t0))
        #printList(arr)
       
 




