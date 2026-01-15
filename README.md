🏭 Manufacturing Downtime Analysis
📌 Project Overview

This project analyzes productivity and downtime data from a soda bottling production line.
The main goal is to understand production efficiency, identify downtime drivers, and evaluate operator performance using exploratory data analysis. 

📂 Dataset Description
Fact Tables

- Line Productivity
   Batch-level production data:
    Date
    Batch ID
    Product ID
    Operator
    Start Time
    End Time
  Line Downtime
    Downtime in minutes by factor for each batch.

 - Dimension Tables
    Products
      Product ID
      Flavor
      Size
      Minimum Batch Time
   Downtime Factors
      Factor ID
      Description
      Operator Error (Yes / No)

🎯 Business Questions

1. What is the current production line efficiency?
2. Are any operators underperforming?
3. What are the leading causes of downtime?

🔍 Analysis Steps
1️⃣ Data Cleaning

Renamed columns for consistency
Converted date and time columns to datetime format
Handled missing values
Merged fact and dimension tables 

2️⃣ Feature Engineering

Batch duration (minutes)
Total downtime per batch
Operator-related downtime
Efficiency metric

3️⃣ Exploratory Data Analysis (EDA)

Downtime distribution across batches
Average downtime per operator
Efficiency comparison between operators
Downtime breakdown by factor
Share of operator-related downtime  

📊 Key Insights

A small number of downtime factors account for most of the lost production time
Some operators show consistently higher average downtime
Operator-related downtime represents a significant portion of total downtime
Production efficiency varies by product and operator 

🛠️ Tools & Technologies

Python
pandas
numpy
matplotlib
seaborn 

🚀 Next Steps

Improve feature engineering
Add machine learning models
Build a production efficiency dashboard 

















   
