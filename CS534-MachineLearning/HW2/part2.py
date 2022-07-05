#Import the packages
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


def logisticregression(X_train,alpha,lamda):
    i=0
    m,n=X_train.shape  
    w=np.random.rand(1,n)
    while i<max_epoch:
             
        grad=(alpha/m)*(np.dot(np.transpose(X_train),(Y_train-sigmoid(np.dot(X_train,np.transpose(w))))))
        w=w+np.transpose(grad)
                        
        if Regularization==True:
            #w=w-alpha*lamda*w
            s,t=w.shape
            for d in range(t):
            
                w[0,d]=np.sign(w[0,d])*max(abs(w[0,d])-alpha*lamda,0)
            #print(w[0,i])
        grad = norm(grad, 1)
        grad_list.append(abs((grad)))
        
        i+=1
        weight_List.append(w)
        weight_List_Sum.append(np.sum(w))
    return(weight_List)
    
def myPredict(X, weight_List,threshold):
    Y_Predict_List=[]
    for i in range(max_epoch):
        Y_Predict=sigmoid(np.dot(X,np.transpose(weight_List[i])))  
        Y_Predict[np.abs(Y_Predict) < threshold] = 0
        Y_Predict[np.abs(Y_Predict) > threshold] = 1
        Y_Predict_List.append(Y_Predict)
    return(Y_Predict_List)
        
    
def sigmoid(f):
    sig=1/(1+np.exp(-f))
    return(sig)
   
    
def myAccuracy(Y,Y_Predict_List):
    acc_list=[]
    Y_dif_list=[]
    d_list=[]
    
    m,n=Y.shape
    for i in range(max_epoch):
        Y_dif=Y-Y_Predict_List[i]
        x=0.
        d=Counter(Y_dif['Response'])
        d_list.append(d[x])
        acc=d_list[i]/m
        acc_list.append(acc)
    return(acc_list)
        
def myplot_2(mylist1,mylist2,Y_Label):
    if plot==True:
        
        plt.plot(list(range(0,max_epoch)),mylist1,'ro',color='red',markersize=2)
        plt.plot(list(range(0,max_epoch)),mylist2,'ro',color='blue',markersize=2)
        
        red_patch = mpatches.Patch(color='blue', label='Lamda= {}'.format(lamda))
        
        plt.legend(handles=[red_patch])
        
        plt.xlabel('iteration', fontsize=10)
        plt.ylabel(Y_Label, fontsize=10)
        plt.show()


def myplot_1(mylist):
    if plot==True:
        
        plt.plot(list(range(0,max_epoch)),mylist,'ro',color='red',markersize=2)
        
        red_patch = mpatches.Patch(color='blue', label='Lamda= {}'.format(lamda))
        
        plt.legend(handles=[red_patch])
        
        plt.xlabel('iteration', fontsize=10)
        plt.ylabel('L-1 Weights', fontsize=10)
        plt.show()
    
    
def Cost(X,w,Y):
    loss_list=[]
    grad_list=[]
    m,n=X.shape  
    for i in range(max_epoch):        
        if Regularization==True:
            a=lamda*norm(w[i], 1)
        else:
            a=0
        SigWtX=sigmoid(np.dot(X,np.transpose(w[i])))      
        Loss=(1/m)*(np.dot(-np.transpose(Y),np.log(SigWtX))-(np.dot((1-np.transpose(Y)),np.log(1-(SigWtX)))))+a    
        loss_list.append(Loss[0][0])
    # if grad<threshold_grad:
        # Y_Predict_List.clear()
        # Y_Predict_List.append((SigWtX))   
    return(loss_list)


#----------------------------------
if __name__ == "__main__": 
  #Import the data
   #Import the data
    base_dir = os.getcwd()
    Train_dir_X = os.path.join(base_dir, "PA2v1_data/pa2_train_X.csv")
    Train_dir_Y = os.path.join(base_dir, "PA2v1_data/pa2_train_y.csv")
    Val_dir_X = os.path.join(base_dir, "PA2v1_data/pa2_dev_X.csv")
    Val_dir_Y = os.path.join(base_dir, "PA2v1_data/pa2_dev_y.csv")
 
    X_train = pd.read_csv(Train_dir_X)
    Y_train=pd.read_csv(Train_dir_Y)
    X_Val=pd.read_csv(Val_dir_X)
    Y_Val=pd.read_csv(Val_dir_Y)
    
    X_train[['Age', 'Annual_Premium', 'Vintage']]=(X_train[['Age', 'Annual_Premium', 'Vintage']]-X_train[['Age', 'Annual_Premium', 'Vintage']].min())/(X_train[['Age', 'Annual_Premium', 'Vintage']].max()-X_train[['Age', 'Annual_Premium', 'Vintage']].min())  
    X_Val[['Age', 'Annual_Premium', 'Vintage']]=(X_Val[['Age', 'Annual_Premium', 'Vintage']]-X_Val[['Age', 'Annual_Premium', 'Vintage']].min())/(X_Val[['Age', 'Annual_Premium', 'Vintage']].max()-X_Val[['Age', 'Annual_Premium', 'Vintage']].min())
   
    
    
    grad_list=[]
    loss_list=[]
    Y_Predict_List=[]
    weight_List=[]
    weight_List_Sum=[]
    acc_list=[]
    grad=0
    plot=False
    Regularization=True


   # Set the ML Parameteres:
    alpha=1
    lamda=.001
    max_epoch=10
    threshold_grad=1

      
    weight=logisticregression(X_train,alpha,lamda)
    prediction_train=myPredict(X_train,weight,threshold=.5)
    accuracy_train=myAccuracy(Y_train,prediction_train)
    loss_list_train= Cost(X_train,weight,Y_train)
    #print(len(loss_list_train))
        
    prediction_val=myPredict(X_Val,weight,threshold=.5)
    accuracy_val=myAccuracy(Y_Val,prediction_val)
    loss_list_val= Cost(X_Val,weight,Y_Val)
    #myplot(accuracy_val)
    #print(len(loss_list_val))
    
    myplot_2(accuracy_train,accuracy_val,"Accuracy")
    myplot_2(loss_list_train,loss_list_val,"Loss")
    myplot_1(weight_List_Sum)

    N=5
    top_weights = sorted(range(len(weight[max_epoch-1][0])), key = lambda sub: weight[max_epoch-1][0][sub])[-N:] 
    number_of_none_zeroz=np.count_nonzero(weight[max_epoch-1][0])
    #print(accuracy_train[len(accuracy_train)-1])
    #print(accuracy_val[len(accuracy_val)-1])
    #print(top_weights)
    #print(number_of_none_zeroz)
   # print((np.sum(abs(weight[max_epoch-1][0]))))
    #print(X_train.iloc[165, 0])
   # print(heapq.nlargest(5, (weight[max_epoch-1][0])) )
    
    
    
    print("Accuracy Train")
    print(accuracy_train[len(accuracy_train)-1])
    print("Accuracy Validation")
    print(accuracy_val[len(accuracy_val)-1])
    print("Number of none zero weights")
    print(number_of_none_zeroz)

   # print((np.sum(abs(weight[max_epoch-1][0]))))
    #print(X_train.iloc[165, 0])
    print("Top 5 weights:")

    print(heapq.nlargest(5, (weight[max_epoch-1][0])) )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    