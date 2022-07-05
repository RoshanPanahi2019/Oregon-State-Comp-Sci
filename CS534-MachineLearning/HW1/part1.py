
import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
np.set_printoptions(suppress=True) 



#train = np.genfromtxt("PA1_train_norm.csv",delimiter=",")
#dev = np.genfromtxt("PA1_dev_norm.csv",delimiter=",")

root="C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_1/PA1_train.csv"
train = read_csv(root)


Y=train['price']
Y=Y.to_numpy()
Y=Y.reshape((10000,1))

#Normalize
X_df=train.drop(columns=['dummy','id','date','price','zipcode','lat','long','condition','grade','view','waterfront'])
X_norm=(X_df-X_df.min())/(X_df.max()-X_df.min())
#X_norm=X_df
dummy=np.ones((10000,), dtype=int)
X_norm.insert(0, "dummy", dummy, True) 
X_norm=X_norm.to_numpy()
m,n=X_norm.shape
#initialize Weight

w=np.random.rand(1,n)


#


#define function to find cost
def cost(X,Y,W):
    np.seterr(over='raise')
    m,n=X_norm.shape
    hypothesis = X.dot(W.transpose())
    MSE=(1/m)*((np.square(hypothesis-Y)).sum(axis=0))
    return MSE

#function gradient descent algorithm from minimizing theta
def gradientDescent(X,Y,W,lr,iterations):
    count = 1
    cost_log = np.array([])
    while(count <= iterations):
        hypothesis = X.dot(W.transpose())
        #print((hypothesis-Y))
        grad=(2.0/m)*((hypothesis-Y)*X).sum(axis=0)
        W = W - lr*grad

        cost_log = np.append(cost_log,cost(X,Y,W))
        count = count + 1
        #print(LA.norm(grad))
        
    #print(cost_log)
    plt.plot(np.linspace(1,iterations,iterations,endpoint=True),cost_log)
    plt.title("Iteration vs Cost graph ")
    plt.xlabel("Number of iteration")
    plt.ylabel("MSE")
    #plt.show()
    print('cost_log')
    print(cost_log)
    return W


Weight=gradientDescent(X_norm,Y,w,.0001,10000)



#Validation set
root="C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_1/PA1_dev.csv"
train = read_csv(root)


Y=train['price']
Y=Y.to_numpy()
Y=Y.reshape((5597,1))

#Normalize
X_df=train.drop(columns=['dummy','id','date','price','zipcode','lat','long','condition','grade','view','waterfront'])
X_norm=(X_df-X_df.min())/(X_df.max()-X_df.min())
#X_norm=X_df
dummy=np.ones((5597,), dtype=int)
X_norm.insert(0, "dummy", dummy, True) 
X_norm=X_norm.to_numpy()
#print(Weight)







# In[9]: