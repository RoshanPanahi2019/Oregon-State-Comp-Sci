
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

 
#----------main----------------

if __name__ == '__main__':
    path="./data.txt"
    list=load(path)
    del list[0][0]
    del list[1][0]
    del list[2][0]
    
    for i in range(3):
        arr=list[i]
        mergeSort(arr)
        print(arr)
 




