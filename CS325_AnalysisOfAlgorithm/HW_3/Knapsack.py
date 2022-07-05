

import random
from time import time


val=[1,2,3,4,5]
wt=[10,20,15,12,25]
W=50


#--------------------- recursion  ------------------------

def knapSack_recursive(W,wt,val,n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
    
    #First Case:
    # wt[n-1] is too big so it can not be part of the solution 
    # So we look at n-1 items

    if (wt[n-1] > W): 
        return knapSack_recursive(W,wt,val,n-1) 
        
    # Second Case:
    # we compare two things:
        # if we use the item n-1 and add it's value and look at previsoue items with left over weight
        # or if the iterm fits but We dont want to use the item n-1 and we use the previouse best solution

    else: 
        return max(val[n-1] + knapSack_recursive(W-wt[n-1], wt, val, n-1), 
                   knapSack_recursive(W, wt, val, n-1)) 
                   
#--------------------- DP ------------------------

def knapSack_DM(W, wt, val, n): 
    V = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    # We populate the table in V[][] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                V[i][w] = 0
            elif wt[i-1] <= w: 
                # Here we store the values. Equivalent to case 2 in reusvie method 
                # despite the fact that we are storing instead of recursing 
                V[i][w] = max(val[i-1] + V[i-1][w-wt[i-1]],  V[i-1][w]) 
            else: 
                # This is where the weight of the item i is equal to the w 
                # in which case the previous solution is chosen
                
                V[i][w] = V[i-1][w] 
  
    return V[n][W] 
  
def random_generate(W,LowerBound,UperBound):
    Weights_list=[]
    Values_list=[]
    n_list=[]
    step=5
    for n in range(LowerBound,UperBound,step):
        Values  =[random.randrange(0,30) for i in range(n)]
        Weights = [random.randrange(0,40) for i in range(n)]
        Weights_list.append(Weights) 
        Values_list.append(Values)
        n_list.append(n)
    return(n_list,Values_list,Weights_list) 
#------------main---------------
if __name__ == "__main__":

    W = 100
    LowerBound=5
    UperBound=50
    n_list,val_list,wt_list=random_generate(W,LowerBound,UperBound)
    
    
    for i in range(len(val_list)):
        val=val_list[i]
        wt=wt_list[i]
        #print(wt,val)
        n = len(val) 
        t0 = time()
        knapSack_recursive(W, wt, val, n)
        t1=time()
        time_rec=t1-t0
        
        t0 = time()
        knapSack_DM(W, wt, val, n)
        t1=time()
        time_DP=t1-t0
        time_rec_max=0
        time_DP_max=0
        print("N={} W={} Rec time= {} DP time {} max Rec{} max DP {}".format(n_list[i],W,time_rec,time_DP,time_rec_max,time_DP_max))
        #print(knapSack_recursive(W, wt, val, n))
        

  
