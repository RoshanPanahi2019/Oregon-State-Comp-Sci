

import random
from time import time


# test cases:4
# Number of items:2
# P,W:77 7
# P,W:66 6
# people:2
# max weight:5
# max weight:5
#--------------------- DP ------------------------

def knapSack_DM(W, wt, val, n): 
    V = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    # We populate the table in V[][] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            # when no object is included the weight our knapsack is 0
            if i == 0 or w == 0: 
                V[i][w] = 0
            elif wt[i-1] <= w: 
                # Here we store the values. Equivalent to case 2 in recursvie method 
                # despite the fact that we are storing instead of recursing 
                V[i][w] = max(val[i-1] + V[i-1][w-wt[i-1]],  V[i-1][w]) 
            else: 
                # This is where the weight of the item i is equal to the w 
                # in which case the previous solution is chosen
                
                V[i][w] = V[i-1][w] 
  
    #return V[n][W] 
    return V 

def load(path):
    list=[]
    with open(path) as f:
        for i in range(78):
            w = [int(x) for x in next(f).split()] 
            list.append(w)
    
    n=1
    case=0
    weight_list=[[],[],[],[]]
    Price_list=[[],[],[],[]]
    W=[[],[],[],[]]

    n=1
    case=0  
    while n<78:
        item_count=list[n][0]
        family_size=list[n+item_count+1][0]
        for i in range(item_count):
            #print(item_count)
            
            Price_list[case].append(list[n+i+1][0])
            weight_list[case].append(list[n+i+1][1])
        for j in range(family_size):    
            W[case].append(list[n+j+item_count+2][0])
        n=n+i+family_size+3
        case+=1
    return(Price_list,weight_list,W)  
#------------main---------------
if __name__ == "__main__":
    path="./shopping-1.txt"
    Input=load(path)
    Price_list,weight_list,WW=Input
    #Data Structure:
        # WW[Case Number][Person Number in the family]
    
    
    # To reduce complexity, we will callculate the table of values for each familiy once based on the maximum capacity
    
       
    
    Family_Value_list=[]
    Result_elements=[[],[],[],[]]
    Results_price=[[],[],[],[]]
    
    
    for case in range(4):
        Family_Value=0
        W=WW[case][1]
        W_Max=max(WW[case])
        wt=weight_list[case]
        val=Price_list[case]
        n=len(Price_list[case])
        Values=knapSack_DM(W_Max, wt, val, n)
    
        for capacity in WW[case]:
            Person_Value=Values[n][capacity] 
            Family_Value+=Person_Value
            
            i=n
            j=capacity
            Result=[]
            while (i>0 and j>0):
                
                if Values[i][j]==Values[i-1][j]:
                    #print("{} = 0 ".format(i))
                   
                    i-=1
                else:
                    #print("{} = 1 ".format(i))
                    Result.append(i)
                    i-=1
                    j=j-wt[i]
            
            Result_elements[case].append(Result)
        Family_Value_list.append(Family_Value)
     
  
    f = open("results.txt", "a")   
    for case in range(4):    
        
        f.write("Test Case {}\n".format(case+1))
        f.write("Total Price {}\n".format(Family_Value_list[case]))
        f.write("Member Items \n")
        for i in range(len(Result_elements[case])):
            f.write("{}:{}\n".format(i+1,Result_elements[case][i]))
  
       
      
    f.close()
    
    #print(Family_Value_list)
    #print(Result_elements)
            
    
    
    
    
    
    
    
    
    
