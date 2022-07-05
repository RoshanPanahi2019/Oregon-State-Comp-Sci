



def mergeSort3(arr):
    if len(arr) < 2:
        return
    if len(arr) > 1:
    
        mid_left = len(arr)//3

        mid_right=(len(arr)//3)*2 +1
        L = arr[:mid_left] 
        mid=arr[mid_left : mid_right] 
        R = arr[mid_right:]  
        # print(L)
        # print(mid)
        # print(R)
        # exit()
        mergeSort3(L)      
        mergeSort3(mid)
        mergeSort3(R) 
        i = j = m= k = 0
  


        while i < len(L) and j < len(mid) and m < len(R):
            # print(L)
            # print(mid)
            # print(R)
            # exit()
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
                 

        while i < len(L) and j < len(mid):
            if L[i] < mid[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = mid[j]
                j += 1
            k += 1

        while i < len(L) and m < len(R):
            if L[i] < R[m]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[m]
                m += 1
            k += 1

        while j < len(mid) and m < len(R):
            if mid[j] < R[m]:
                arr[k] = mid[j]
                j += 1
            else:
                arr[k] = R[m]
                m += 1
            k += 1



                 
     
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
       
    #exit()


def load(path):
    list=[]
    with open(path) as f:
        for i in range(2):
            w = [int(x) for x in next(f).split()] 
            list.append(w)
    return(list)
    

 
 
#----------main----------------

if __name__ == '__main__':
    path="./data.txt"
    list=load(path)
    del list[0][0]
    del list[1][0]
    # del list[2][0]

    for i in range(2):
        arr=list[i]
        mergeSort3(arr)
        print(arr)
 


                
            
            
            
            
            
            
            
            
            
            
            
            