import numpy as np
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import linalg as LA
import xlsxwriter
#import sklearn

root="C:/Users/Roshan/Box/Courses/Fall-2020/CS534/Assignment/Implementation_1/PA1_train.csv"
df = read_csv(root)
df_Statistics=df
mean=[]
Std=[]
range=[]
waterfront_Percentage=[]
view_Percentage=[]
condition_Percentage=[]
grade_Percentage=[]

df_Numerical=df_Statistics.drop(columns=['dummy','id','date','waterfront','view','condition','grade','zipcode','lat','long','price'])

mindex=pd.MultiIndex(levels=[['mean','Std']],codes=[[0,1]])



#Part 0-a
df=df.drop(columns=['id'])
#Part 0-b
df[["day", "mm", "year"]] = df["date"].str.split("/", expand=True)
df=df.drop(columns=['date'])
print(df)

# Part 0-C
mean.append(df_Numerical.mean())
Std.append(df_Numerical.std())
range.append(df_Numerical.max()-df_Numerical.min())
df_Statistics=df_Numerical
df_Statistics=df_Statistics.append(mean, ignore_index=True)
df_Statistics=df_Statistics.append(Std, ignore_index=True)
df_Statistics=df_Statistics.append(range, ignore_index=True)
df_Statistics=df_Statistics.tail(3)

df_Statistics.to_excel("output.xlsx") 
    
waterfront_Percentage.append(df.waterfront.value_counts(normalize=True)*100)
view_Percentage.append(df.view.value_counts(normalize=True)*100)
condition_Percentage.append(df.condition.value_counts(normalize=True)*100)
grade_Percentage.append(df.grade.value_counts(normalize=True)*100)
print(waterfront_Percentage)
print(view_Percentage)
print(condition_Percentage)
print(grade_Percentage)
print(df_Statistics)




# with xlsxwriter.Workbook('test.xlsx') as workbook:
    # worksheet = workbook.add_worksheet()

    # for row_num, data in enumerate(waterfront_Percentage):
        # worksheet.write_row(row_num+1, 0, data)
    # for row_num, data in enumerate(view_Percentage):
        # worksheet.write_row(row_num+4, 0, data)    
    # for row_num, data in enumerate(condition_Percentage):
        # worksheet.write_row(row_num+8, 0, data)
    # for row_num, data in enumerate(grade_Percentage):
        # worksheet.write_row(row_num+12, 0, data)         
        
        
        
    
        
        
        
        
        
        
        




