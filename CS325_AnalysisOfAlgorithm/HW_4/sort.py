
# This is a sort algorithm I used. It is iterative but easier to find the index of the sorted lists

def Sort(array): 
    l = len(array) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (array[j][1] > array[j + 1][1]): 
                void = array[j] 
                array[j]= array[j + 1] 
                array[j + 1]= void 
    return array 
  