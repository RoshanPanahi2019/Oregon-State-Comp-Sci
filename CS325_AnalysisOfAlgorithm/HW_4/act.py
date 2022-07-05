
from sort import Sort # This is a sort algorithm I used. It is iterative but easier to find the index of the sorted lists


def Scheduler(activities_sorted,case):

    n = len(activities_sorted)
 
    # We first select the last activity since it is the last to start
    i = n-1
    # Consider rest of the activities
    j=n-2
    results[case].append(activities_sorted[n-1][0])
    while j>-1:
        # here we just check the next activities' finish time to be less than the start time of the 
        # the chosen one, to avoid conflicts
        
        if activities_sorted[j][2] <= activities_sorted[i][1]:            
            results[case].append((activities_sorted[j][0]))
                        
            i = j
        j -=1
    return(results)

def load(path):
    list=[]
    
    with open(path) as f:
        for j in range(23):
            w = [int(x) for x in next(f).split()] 
            list.append(w)
    list_activity=[[],[],[]]
    start_list=[[],[],[]]
    finish_list=[[],[],[]]

    n=0
    activity=0  
    while n<23:
        item_count=list[n][0]
        for i in range(item_count):
            n+=1
            start_list[activity].append(list[n][1])
            finish_list[activity].append(list[n][2]) 
            list_activity[activity].append([list[n][0],list[n][1],list[n][2]])           
        n+=1
        activity+=1
    
    return(start_list,finish_list,list_activity)  

#-----------------------------
if __name__ == "__main__":
    path="./act.txt"
    Input=load(path)
    start_list,finish_list,list_activity=Input
    results=[[],[],[]]
    
    for case in range(3):  
        activities_sorted=Sort(list_activity[case])
        Scheduler(activities_sorted,case)
        n = len(results[case])
        print("Set{}\n Number of activities selected = {}\n Activities:{} \n ".format(case,n,results[case]))
        
    
    
    
    
    
    
    
    