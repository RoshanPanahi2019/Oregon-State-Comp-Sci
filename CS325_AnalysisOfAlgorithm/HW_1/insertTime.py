
import random
from time import time

def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i]   
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
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
        n_list.append(500*(i+1))
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
        insertionSort(arr)
        t1 = time()
        print('array size n = {}'.format(len(arr)), 'Time taken to sort = {}'.format(t1-t0))
