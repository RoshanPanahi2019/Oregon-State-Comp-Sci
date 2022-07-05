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
import time

start_time = time.time()

def Perceptron_Kernel(X,Y,K,K_val,maxiter):
    iter=0
    u=0
    u_val=0

    alpha_example=[]
    alpha_iter=[]

    while (iter<maxiter):
        correct=0
        correct_val=0
        for i in range(m): 
            u=0
            for j in range(m):  
                a=alpha[0,j]*(K[i,j])*Y[j,0]
                u=u+a

            if (u*Y[i,0]<=0) :
                alpha[0,i]=alpha[0,i]+1 
            else:
                correct+=1  
            #Validation     # Check if the i and j are put in the right positions, seems like its in the feature 
        for i in range(m_val):   
            u_val=0                
            for j in range(m):      
                a_val=alpha[0,j]*(K_val[j,i])*Y[j,0]
                u_val=u_val+a_val
            if (u_val*Y_Val[i,0]>0):
                correct_val+=1      
                
        accuracy.append(correct/m) 
        accuracy_val.append(correct_val/m_val)
        iter+=1    
    print(accuracy)
    print(accuracy_val)
    
    return(0)      


def Kapa(x_1,x_2,p):
    result=(1+np.dot(np.transpose(x_1),x_2))**p
    return(result)
    
    
def gram(X,p):
    K=np.zeros((m,m))    
    for i in range(m):
        for j in range(m):
            K[i,j]=Kapa(X[i,:],X[j,:],p)
    return(K)
    
    
def gram_val(X,X_val,p):

    K=np.zeros((m,m_val))
    for i in range(m):
        for j in range(m_val):
            K[i,j]=Kapa(X[i,:],X_val[j,:],p)
    return(K)
    
def myplot_1(mylist):

    if plot==True:
        
        plt.plot(list(range(0,maxiter)),mylist,'-ro',color='red',markersize=2)
        
        #red_patch = mpatches.Patch(color='blue', label='Lamda= {}'.format(lamda))
        
        #plt.legend(handles=[red_patch])
        
        plt.xlabel('iteration', fontsize=10)
        plt.ylabel('Accuracy', fontsize=10)
        plt.show()
        
def myplot_2(mylist1,mylist2,X_Label):
    if plot==True:
        
        plt.plot(mylist2,mylist1,'-ro',color='red',markersize=2)
        #plt.plot(list(range(0,maxiter)),mylist2,'ro',color='blue',markersize=2)
        
        
        
        plt.xlabel(X_Label, fontsize=10)
        plt.ylabel("Accuracy", fontsize=10)
        plt.show()
            
def Predict(weights,X):
    accuracy_iter=[]
    iterations=maxiter


    for iter in range(iterations):
        correct=0
        for i in range(m): 
            u=0
            for j in range(m):  
                a=weights[iter][0,j]*(K[i,j])*Y[j,0]
                u=u+a
            if (u*Y[i,0]>0):
                correct+=1
        accuracy_iter.append(correct/m)
    #print(accuracy_iter)
    return(accuracy_iter)
          
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
   
   
    X=pd.DataFrame.to_numpy(X_train)
    Y=pd.DataFrame.to_numpy(Y_train)
    
    X_Val=pd.DataFrame.to_numpy(X_Val)
    Y_Val=pd.DataFrame.to_numpy(Y_Val)
  
    plot=True

    maxiter=10
    iter=0
    m,n=X.shape
    m=500
    m_val,n_val=X_Val.shape
    m_val=250
    alpha=np.zeros((1,m))
    accuracy_list=[]
    acc_list=[]
    accuracy=[]
    accuracy_val=[]
    alpha_list=[] #alpha_list[which p][which iteration][which example]
    
    Result_best_train=[]
    Result_best_val=[]
    P_list=[]
    
    p=4
    


    K=gram(X,p)
    K_val=gram_val(X,X_Val,p)
    alphas=Perceptron_Kernel(X,Y,K,K_val,maxiter)

    Result_best_train=[.768,.856,.886,.912,.908]
    Result_best_val=[.73,.76,.73,.878,.872]
    P_list=[1,2,3,4,5]
    
    myplot_1(accuracy)
    myplot_1(accuracy_val)
    
    myplot_2(Result_best_val,P_list,"kernel")
    
    # print(np.argmax(accuracy))
    # print(np.argmax(accuracy_val))
    print(accuracy[np.argmax(accuracy)])
    print(accuracy[np.argmax(accuracy_val)])
    print("--- %s seconds ---" % (time.time() - start_time))




   