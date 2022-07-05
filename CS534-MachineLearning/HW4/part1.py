

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def myplot_1(mylist):

    plt.plot(depth,mylist,'-ro',color='red',markersize=2)
    
    plt.xlabel('iteration', fontsize=10)
    plt.ylabel('Accuracy', fontsize=10)
    plt.show()
    
     
def Leaf_Node(Input):   
    Y = Input[:, -1]
    myClass, myClass_i = np.unique(Y, return_counts=True)
    i = myClass_i.argmax()
    cls = myClass[i]
    return cls

def Entropy(Input):    
    Y = Input[:, -1]
    _, n = np.unique(Y, return_counts=True)
    p = n / n.sum()
    E = sum(p * -np.log2(p))    
    return E

def split_best(Input, splits_all):
    i = True
    for c in splits_all:
        for data in splits_all[c]:
            zero, one = split_data(Input, split_column=c, split_value=data)                     
            n = len(zero) + len(one)
            p_zero = len(zero) / n
            p_one = len(one) / n
            H = (p_zero * Entropy(zero) + p_one * Entropy(one))
            if i or H <= best:
                i = False                
                best = H
                best_c = c
                best_v = data    
    return best_c, best_v

def split_data(Input, split_column, split_value):  
    split_column_values = Input[:, split_column]
    zero = Input[split_column_values == split_value]
    one = Input[split_column_values != split_value]    
    return zero, one

def DT(df, i=0, max_depth=2):
    if i == 0:
        global features
        features = df.columns
        Input = df.values
    else:
        Input = df                 
    Y = Input[:, -1]
    my_cls = np.unique(Y)
    if len(my_cls) == 1:
        Pure=True
    else:
        Pure= False
 
    if (Pure) or (len(Input) < 2) or (i == max_depth):
        leaf = Leaf_Node(Input)
        return leaf
    else:    
        i += 1   
        
        splits_all = {}
        _, n_c = Input.shape
        for c in range(n_c - 1):    
            splits_all[c] = np.unique(Input[:, c])
        
        column, value = split_best(Input, splits_all)
        zero, one = split_data(Input, column, value)
           
        if len(zero) == 0 or len(one) == 0:
            leaf = Leaf_Node(Input)
            return leaf       
        feature = features[column]
        test_q = "{} = {}".format(feature, value)
        tree_i = {test_q: []}
        Pos = DT(zero, i,  max_depth)
        Neg = DT(one, i,  max_depth)
        tree_i[test_q].append(Pos)
        tree_i[test_q].append(Neg)
    
        return tree_i

def predict(row, hypothesis):
        
    test_q = list(hypothesis.keys())[0]
    feature, _, data = test_q.split(" ")


    if str(row[feature]) == data:
        response = hypothesis[test_q][0]
    else:
        response = hypothesis[test_q][1]
    if not isinstance(response, dict):
        return response
    else:
        r_tree = response
        return predict(row, r_tree)    
def pred(data, hypothesis):   
    predictions = data.apply(predict, args=(hypothesis,), axis=1)       
    return predictions
    
def acc(data, hypothesis):
    predictions = pred(data, hypothesis)
    correct = predictions == data.label
    accuracy = correct.mean()    
    return accuracy
#----------------------------

if __name__ == "__main__": 

    Train_dir_X = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_train_X.csv"
    Train_dir_Y = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_train_y.csv"
    Val_dir_X = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_dev_X.csv"
    Val_dir_Y = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/pa4_dev_y.csv"
    
    data_train_dir = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/data.csv"
    data_dev_dir = "C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_4/pa4_data/data_dev.csv"

 
    X_train = pd.read_csv(Train_dir_X)
    A=X_train.to_numpy()
    Y_train=pd.read_csv(Train_dir_Y)
    B=Y_train
    #data=np.concatenate((A,B),1)
    data_train=pd.read_csv(data_train_dir)
    data_dev=pd.read_csv(data_dev_dir)

    
    X_Val=pd.read_csv(Val_dir_X)
    Y_Val=pd.read_csv(Val_dir_Y, header=None).values.astype(int)
    
   
    acc_train=[]
    acc_dev=[]
    depth=[2,5,10,20,25,30,35,40,50]
 
    #for i in iteration:
    hypothesis=DT(data_train, max_depth=2)
    accuracy_train = acc(data_train, hypothesis)
    accuracy_dev = acc(data_dev, hypothesis)

    acc_train.append(accuracy_train)
    acc_dev.append(accuracy_dev)
        
    print(acc_train)
    print(acc_dev)
        
    # myplot_1(acc_train)
    # myplot_1(acc_dev)
    
    