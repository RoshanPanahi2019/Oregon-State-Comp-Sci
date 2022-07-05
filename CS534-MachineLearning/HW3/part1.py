import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy.linalg import norm
from scipy import stats, optimize, interpolate
from collections import Counter 
import scipy
import heapq
import os
import statistics

def Perceptron(X,Y,maxiter):
    m,n=X.shape
    w=np.zeros((1,n))
    w_avg=np.zeros((1,n))
    iter=0
    X=pd.DataFrame.to_numpy(X)
    Y=pd.DataFrame.to_numpy(Y)
    
    while iter<maxiter:
        for i in range(m):
            a=np.dot(X[i,:],np.transpose(w))
            b=Y[i]*a
            if b<=0:   
                c=Y[i]*X[i,:]
                w=w+c
            w_avg=((i+1)*w_avg+w)/((i+1)+1)
            
            
        Prediction_train_w=myPredict(X_train,w) 
        Prediction_val_w=myPredict(X_Val,w) 
        accuracy_list_w_train.append(myAccuracy(Prediction_train_w,Y_train))
        accuracy_list_w_Val.append(myAccuracy(Prediction_val_w,Y_Val))
        
        Prediction_train_w_avg=myPredict(X_train,w_avg)  
        Prediction_val_w_avg = myPredict(X_Val,w_avg)       
        accuracy_list_w_avg_train.append(myAccuracy(Prediction_train_w_avg,Y_train))
        accuracy_list_w_avg_Val.append(myAccuracy(Prediction_val_w_avg,Y_Val))
        iter+=1   
    return(w,w_avg)

def myAccuracy(Y_Predict,Y):
    m,n=Y.shape
    accuracy=1-(np.count_nonzero(Y_Predict-Y))/m
    return(accuracy)


def Loss(X,Y,w,w_avg):
    loss_list=[]
    #X=pd.DataFrame.to_numpy(X)
    #Y=pd.DataFrame.to_numpy(Y)
    m,n=X.shape
    for i in range(m):
        Y_Predict=np.dot(X[i,:],np.transpose(w))
        loss=Y[i]-Y_Predict
        loss_list.append(loss)
    return(sum(np.abs(loss_list)))
        
def myplot_1(mylist):

    if plot==True:
        
        plt.plot(list(range(0,maxiter)),mylist,'-ro',color='red',markersize=2)
        
        #red_patch = mpatches.Patch(color='blue', label='Lamda= {}'.format(lamda))
        
        #plt.legend(handles=[red_patch])
        
        plt.xlabel('iteration', fontsize=10)
        plt.ylabel('Accuracy', fontsize=10)
        plt.show()

def myPredict(X, weight):

    Y_Predict=np.sign(np.dot(X,np.transpose(weight)))
    return(Y_Predict)



#----------------------------------
if __name__ == "__main__": 

    base_dir = os.getcwd()
    Train_dir_X = os.path.join(base_dir, "PA3_data/pa3_train_X.csv")
    Train_dir_Y = os.path.join(base_dir, "PA3_data/pa3_train_y.csv")
    Val_dir_X = os.path.join(base_dir, "PA3_data/pa3_dev_X.csv")
    Val_dir_Y = os.path.join(base_dir, "PA3_data/pa3_dev_y.csv")
 
    X_train = pd.read_csv(Train_dir_X)
    Y_train=pd.read_csv(Train_dir_Y)
    X_Val=pd.read_csv(Val_dir_X)
    Y_Val=pd.read_csv(Val_dir_Y)
    
    X_train[['Age', 'Annual_Premium', 'Vintage']]=(X_train[['Age', 'Annual_Premium', 'Vintage']]-X_train[['Age', 'Annual_Premium', 'Vintage']].min())/(X_train[['Age', 'Annual_Premium', 'Vintage']].max()-X_train[['Age', 'Annual_Premium', 'Vintage']].min())  
    X_Val[['Age', 'Annual_Premium', 'Vintage']]=(X_Val[['Age', 'Annual_Premium', 'Vintage']]-X_Val[['Age', 'Annual_Premium', 'Vintage']].min())/(X_Val[['Age', 'Annual_Premium', 'Vintage']].max()-X_Val[['Age', 'Annual_Premium', 'Vintage']].min())
   
   
   
    plot=True
    maxiter=100
    accuracy_list_w=[]
    accuracy_list_w_avg=[]
    
    accuracy_list_w_avg_train=[]
    accuracy_list_w_avg_Val=[]
    accuracy_list_w_train=[]
    accuracy_list_w_Val=[]
    X=X_train
    Y=Y_train
    
    
    w,w_avg=Perceptron(X,Y,maxiter)
    
    Prediction=myPredict(X,w)
    #print(myAccuracy(Prediction))

    #myplot_1(accuracy_list_w)
    #myplot_1(accuracy_list_w_train)
    myplot_1(accuracy_list_w_avg_Val)
    
    print(statistics.stdev(accuracy_list_w_train))
    print(statistics.stdev(accuracy_list_w_avg_train))
    print(statistics.stdev(accuracy_list_w_Val))
    print(statistics.stdev(accuracy_list_w_avg_Val))
    
    
    print(statistics.mean(accuracy_list_w_train))
    print(statistics.mean(accuracy_list_w_avg_train))
    print(statistics.mean(accuracy_list_w_Val))
    print(statistics.mean(accuracy_list_w_avg_Val))
    
    a=np.argmax(accuracy_list_w_avg_Val)
    print((accuracy_list_w_avg_Val[a]))















