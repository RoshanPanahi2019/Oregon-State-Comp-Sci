import math

def calc_weight(list_of_Graph_Coordinates):
    adj_matrix=[[],[],[],[]]
    
    for case in range(4):
        a=len(list_of_Graph_Coordinates[case])
        b=len(list_of_Graph_Coordinates[case])
        Matrix = [[0 for x in range(a)] for y in range(b)] 
        for m in range(a):
            for n in range(b):
                w=(list_of_Graph_Coordinates[case][m][0]-list_of_Graph_Coordinates[case][n][0])**2
                s=(list_of_Graph_Coordinates[case][m][1]-list_of_Graph_Coordinates[case][n][1])**2
                Matrix[m][n]=round(math.sqrt(w+s))

        adj_matrix[case].append(Matrix)
    return(adj_matrix)
def prims(adj_matrix,V_count,list_of_Graph_Coordinates,case):
    infinity = 1000000000
    V_count = V_count
    Graph= adj_matrix       
    weight_of_tree=[]
    chosen = [0 for x in range(V_count)]
    zeroEdges = 0
    chosen[0] = True
    print("  Test Case {} \n  Edge in MST \n  Point (x,y)    Distance".format(case))
    while (zeroEdges < V_count - 1):
        minimum = infinity
        x = 0
        y = 0
        for i in range(V_count):
            if chosen[i]:
                for j in range(V_count):
                    if ((not chosen[j]) and Graph[i][j]):  
                        if minimum > Graph[i][j]:
                            minimum = Graph[i][j]
                            x = i
                            y = j
        print(str(list_of_Graph_Coordinates[case][x]) + "-" + str(list_of_Graph_Coordinates[case][y]) + ":     " + str(Graph[x][y]))
        weight_of_tree.append((Graph[x][y]))
        chosen[y] = True
        zeroEdges += 1
    print("   total distance {} \n".format(sum(weight_of_tree)))
def load(path):
    list=[]
    
    with open(path) as f:
        for j in range(35):
            w = [int(x) for x in next(f).split()] 
            list.append(w)
    list_of_Graph_Coordinates=[[],[],[],[],[]]
    n=1
    case=0    
    while n<34:
        item_count=list[n][0]
        for i in range(item_count):
            a=[]
            n+=1
            a.append(list[n][0])
            a.append(list[n][1])
            list_of_Graph_Coordinates[case].append(a)      
        n+=1
        case+=1    
    return(list_of_Graph_Coordinates)      
#---------------------------
if __name__ == "__main__":
    path="./graph.txt"
    list_of_Graph_Coordinates=load(path)
    adj_matrix=calc_weight(list_of_Graph_Coordinates)
    for case in range(4): 
        V_count=len(adj_matrix[case][0]) 
        prims(adj_matrix[case][0], V_count,list_of_Graph_Coordinates,case)
        
    