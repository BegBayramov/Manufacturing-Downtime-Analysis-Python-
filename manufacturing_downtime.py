# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 17:19:36 2026

@author: Beg
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading data
data_dictionary = pd.read_csv("C:\\Users\\Beg\\Desktop\\proiecti\\Manufacturing_Downtime_python\\data_dictionary.csv")  

line_productivity = pd.read_csv("C:\\Users\\Beg\\Desktop\\proiecti\\Manufacturing_Downtime_python\\line_productivity.csv",delimiter = ";")  

products = pd.read_csv("C:\\Users\\Beg\\Desktop\\proiecti\\Manufacturing_Downtime_python\\products.csv",delimiter = ";")  

downtime_factors = pd.read_csv("C:\\Users\\Beg\\Desktop\\proiecti\\Manufacturing_Downtime_python\\dowtime_factors.csv",delimiter = ";")   

line_downtime = pd.read_csv("C:\\Users\\Beg\\Desktop\\proiecti\\Manufacturing_Downtime_python\\line_downtime.csv",delimiter = ";",header = 1)

#%%
#clean data 

print(line_productivity.head())
print(line_productivity.shape)
print(line_productivity.info())
print(line_productivity.isna().sum())
print(line_productivity.isna().any())
print(line_productivity.describe())

#change type column start_time and end_time to datetype and 
# change columns name 

cols = ["Date","Start Time","End Time"]

line_productivity[cols] = line_productivity[cols].apply(pd.to_datetime)

line_productivity.columns = line_productivity.columns.str.replace(" ","_")

line_downtime.columns = line_downtime.columns.str.replace(" ","_")

products.columns = products.columns.str.replace(" ","_")
downtime_factors.columns = downtime_factors.columns.str.replace(" ","_") 
#%%

#%%
#1 - What's the current line efficiency? (total time / min time)

line_productivity['total_time'] = (line_productivity["End_Time"] - line_productivity["Start_Time"]).dt.total_seconds()/60 #time in minut
line_productivity.iloc[37,6] = 130

dw = ["1","2","3","4","5","6","7","8","9","10","11","12"]
line_downtime["total_downtime"] = line_downtime[dw].sum(axis = 1,skipna = True)

produc_downtime = line_productivity.merge(line_downtime, on = "Batch",how = "left" )

produc_downtime["productiv_time"] = produc_downtime["total_time"] - produc_downtime["total_downtime"]



line_efficiency = round((produc_downtime["productiv_time"].sum()/produc_downtime["total_time"].sum())*100,2)

print("Line Efficiency: ", line_efficiency,"%")
#%%

#2 - Are any operators underperforming? 

produc_downtime["efficiency_%"] = round((produc_downtime["productiv_time"] / produc_downtime["total_time"]) * 100, 2) 

operator_efficiency = produc_downtime.groupby("Operator").agg( 
    avg_efficiency = ("efficiency","mean"),
    total_batches = ("Batch","count")
    ).reset_index() 

overall_avg = operator_efficiency["avg_efficiency"].mean()

underperforming = operator_efficiency[operator_efficiency["avg_efficiency"] < overall_avg] 

print(underperforming)

operator_efficiency.plot(x = "Operator",y = "avg_efficiency",kind = "bar",rot = 0,color = "limegreen",title="Average Line Efficiency by Operator")

#%%


# 3 - Manufacturing Downtime 

line_downtime_factor = line_downtime.iloc[:,1:].sum(skipna = True).reset_index(name="total_minut").rename(columns={"index":"Factor"}).iloc[:-1]

line_downtime_factor["Factor"] = line_downtime_factor["Factor"].astype("Int64")


factor_total = line_downtime_factor.merge(downtime_factors,on = "Factor")

factor_total.plot(x = "Description",y = "total_minut",kind = "bar",rot = 45,title = "Total Downtime by Factor")

#sns.barplot(x = "Description",y = "total_minut",data = factor_total,)

#%%


# 4- 





