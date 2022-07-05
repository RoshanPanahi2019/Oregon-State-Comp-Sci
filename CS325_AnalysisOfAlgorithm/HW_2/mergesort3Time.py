


import random
from time import time


def mergeSort3(arr):
    if len(arr) < 2:
        return
    if len(arr) > 1:
    
        mid_left = len(arr)//3

        mid_right=(len(arr)//3)*2 +1
        L = arr[:mid_left] 
        mid=arr[mid_left : mid_right] 
        R = arr[mid_right:]  
        mergeSort3(L)      
        mergeSort3(mid)
        mergeSort3(R) 
        i = j = m= k = 0
  


        while i < len(L) and j < len(mid) and m < len(R):
            #Compare the elements of each first second two lists if the minimum was in the first list
            if  L[i] < mid[j]:
                min=L[i]        
                            
                if R[m] <min :
                    arr[k]=R[m] 
                    m+=1
                else:  
                    arr[k] = L[i]
                    i += 1

            else:
               
                min=mid[j]
                if R[m] <min :
                    arr[k]=R[m] 
                    m+=1
                else:  
                    arr[k] = mid[j]
                    j += 1
                   
            k += 1
                 
        #Handling the case where we went through all the elements in Right and they were minimums   
        while i < len(L) and j < len(mid):
            if L[i] < mid[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = mid[j]
                j += 1
            k += 1
        #Handling the case where we went through all the elements in middle and they were minimums        
        while i < len(L) and m < len(R):
            if L[i] < R[m]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[m]
                m += 1
            k += 1
        #Handling the case where we went through all the elements in Left and they were minimums   
        while j < len(mid) and m < len(R):
            if mid[j] < R[m]:
                arr[k] = mid[j]
                j += 1
            else:
                arr[k] = R[m]
                m += 1
            k += 1



                 
     # Handling the case where the minimum was in the two other sub arrays, therefore assigning what is left //to the mergedarray
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(mid):
            arr[k] = mid[j]
            j += 1
            k += 1   
            
        while m < len(R):
            arr[k] = R[m]
            m += 1
            k += 1
       


def load(path):
    list=[]
    with open(path) as f:
        for i in range(1):
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
        mergeSort3(arr)
        t1 = time()
        print('array size n = {}'.format(len(arr)), 'Time taken to sort = {}'.format(t1-t0))
        #printList(arr)
       
 
 


                
            
            
            
            
            
            
            
            
            
            
            
            