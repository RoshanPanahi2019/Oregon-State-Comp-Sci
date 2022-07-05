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
    
    
    
#----------main----------------

if __name__ == '__main__':
    path="./data.txt"
    list=load(path)
    del list[0][0]
    del list[1][0]
    del list[2][0]    
    

    for i in range(3):
        arr=list[i]
        insertionSort(arr)  
        print(arr)
