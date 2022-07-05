import numpy as np
import pandas as pd
import random

def myplot_1(mylist):
    plt.plot(tree,mylist,'-ro',color='red',markersize=2)   
    
def Leaf_Node(input):  
    Y = input[:, -1]
    cls, cls_u = np.unique(Y, return_counts=True)
    i = cls_u.argmax()
    leaf = cls[i]   
    return leaf

def splits(input, sample):
    spl = {}
    _, n_columns = input.shape
    c_i = list(range(n_columns - 1))  
    if sample and sample <= len(c_i):       
        c_i = random.sample(c_i, k=sample)
    for c in c_i:     
        v = input[:, c]
        v_u = np.unique(v)      
        spl[c] = v_u  
    return spl

def Entropy(Input):    
    Y = Input[:, -1]
    _, n = np.unique(Y, return_counts=True)
    p = n / n.sum()
    E = sum(p * -np.log2(p))    
    return E

def best(Input, splits_all):
    i = True
    for c in splits_all:
        for input in splits_all[c]:
            zero, one = split_data(Input, column=c, s_value=input)                     
            n = len(zero) + len(one)
            p_zero = len(zero) / n
            p_one = len(one) / n
            H = (p_zero * Entropy(zero) + p_one * Entropy(one))
            if i or H <= best:
                i = False                
                best = H
                best_c = c
                best_v = input    
    return best_c, best_v

def split_data(Input, column, s_value):  
    c_value = Input[:, column]
    zero = Input[c_value == s_value]
    one = Input[c_value != s_value]    
    return zero, one

def Pure(input):    
    Y = input[:, -1]
    cls = np.unique(Y)
    if len(cls) == 1:
        return True
    else:
        return False
        
def DT(df, i=0, s_min=2, max_depth=5, sample=None):
    
    if i == 0:
        global features
        features = df.columns
        input = df.values
    else:
        input = df              
    if (Pure(input)) or (len(input) < 2) or (i == max_depth):
        leaf = Leaf_Node(input)        
        return leaf
    else:    
        i += 1
        spl = splits(input, sample)
        column, s_value = best(input, spl)
        zero, one = split_data(input, column, s_value)
        if len(zero) == 0 or len(one) == 0:
            leaf = Leaf_Node(input)
            return leaf          
        feature = features[column]      
        test_q = "{} = {}".format(feature, s_value)
        tree_i = {test_q: []}
        Pos = DT(zero, i, s_min, max_depth, sample)
        Neg = DT(one, i, s_min, max_depth, sample)
        if Pos == Neg:
            tree_i = Pos
        else:
            tree_i[test_q].append(Pos)
            tree_i[test_q].append(Neg)       
        return tree_i

def predict(row, hypothesis):
    if not isinstance(hypothesis, dict):
        return hypothesis
    test_q = list(hypothesis.keys())[0]
    feature, compare, value = test_q.split(" ")
   
    if str(row[feature]) == value:
        response = hypothesis[test_q][0]
    else:
        response = hypothesis[test_q][1]
    if not isinstance(response, dict):
        return response   
    else:
        r_tree = response
        return predict(row, r_tree)
        
def pred(dev, hypothesis):
    predictions = dev.apply(predict, args=(hypothesis,), axis=1)
    return predictions
    
    
   
def bootstrap(Input, n):
    np.random.seed(1)
    index = np.random.randint(low=0, high=len(Input), size=n)
    result = Input.iloc[index]   
    return result

def Random_Forest(Input, trees, n, n_f, d_max):
    forest = []
    for i in range(trees):
        result = bootstrap(Input, n)
        tree = DT(result, max_depth=d_max, sample=n_f)
        forest.append(tree)
    return forest

def Forest_pred(dev, forest):
    output = {}
    for i in range(len(forest)):
        column = "tree_{}".format(i)
        predictions = pred(dev, hypothesis=forest[i])
        output[column] = predictions

    output = pd.DataFrame(output)
    Prediction = output.mode(axis=1)[0]   
    return Prediction
   
def calculate_accuracy(predictions, labels):
    predictions_correct = predictions == labels
    accuracy = predictions_correct.mean()
    
    return accuracy
#-------------------------
if __name__ == "__main__": 

    Train_dir_X = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_train_X.csv"
    Train_dir_Y = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_train_y.csv"
    Val_dir_X = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_dev_X.csv"
    Val_dir_Y = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_dev_y.csv"
    
    data_train_dir = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/data.csv"
    data_dev_dir = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/data_dev.csv"

    accuracy_train=[]
    accuracy_dev=[]
    
    X_train = pd.read_csv(Train_dir_X)
    A=X_train.to_numpy()
    Y_train=pd.read_csv(Train_dir_Y)
    B=Y_train
    data_train=pd.read_csv(data_train_dir)
    data_dev=pd.read_csv(data_dev_dir)

    
    X_Val=pd.read_csv(Val_dir_X)
    Y_Val=pd.read_csv(Val_dir_Y, header=None).values.astype(int)
    
    depth=[2,10,25]
    feature=[5,25,50,100]
    tree=[10,20,30 ,40 ,50 ,60 ,70, 80 ,90 ,100]   
    acc=[]
    acc_train_t=[]
    acc_dev_t=[]
    
    acc_train_m=[]
    acc_dev_m=[]
     
    acc_train_d=[]
    acc_dev_d=[]  
    
    for d in depth: 
        acc_train_m=[]
        acc_dev_m=[]
        for m in feature:   
            acc_train_t=[]
            acc_dev_t=[]
            for t in tree:
                forest = Random_Forest(data_train, trees=t, n=10049, n_f=m, d_max=d)
                
                Y_Output= Forest_pred(data_train, forest)
                predictions = Forest_pred(data_dev, forest)
                                
                accuracy_train=calculate_accuracy(Y_Output, data_train.label)
                accuracy_dev = calculate_accuracy(predictions, data_dev.label)
                print(accuracy_train)
                print(accuracy_dev)
                
                acc_train_t.append(accuracy_train)
                acc_dev_t.append(accuracy_dev)
                
            acc_train_m.append(acc_train_t)
            acc_dev_m.append(acc_dev_t)
            
        acc_train_d.append(acc_train_m)
        acc_dev_d.append(acc_dev_m)        
            
                
    print(acc_train_d)
    print(acc_dev_d)
     
  
    color=["red","blue","green","black"]
        
        
    
    #Plot train
    for  j in range(4):
        mylist=acc_train_d[0][j]
        
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Training Accuracy', fontsize=10)   
   # plt.show() 
    
    #Plot train
    for  j in range(4):
        mylist=acc_train_d[1][j]
   
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Training Accuracy', fontsize=10)   
    #plt.show() 
    
    #Plot train
    for  j in range(4):
        mylist=acc_train_d[2][j]
        
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Training Accuracy', fontsize=10)   
    #plt.show() 
    
    
    #plot dev
    
    
    for  j in range(4):
        mylist=acc_dev_d[0][j]
        
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Validation Accuracy', fontsize=10)   
    #plt.show() 
    
    #Plot train
    for  j in range(4):
        mylist=acc_dev_d[1][j]
   
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Validation Accuracy', fontsize=10)   
    #plt.show() 
    
    #Plot train
    for  j in range(4):
        mylist=acc_dev_d[2][j]
        
        plt.plot(tree,mylist,'-ro',color=color[j],markersize=2)
    plt.xlabel('tree', fontsize=10)
    plt.ylabel('Validation Accuracy', fontsize=10)   
    #plt.show() 
      
    
    
    
    
    
    
    

  
    