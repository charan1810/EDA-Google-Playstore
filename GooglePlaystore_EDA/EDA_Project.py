import numpy as np
import pandas as pd

pd.set_option("display.max_columns",None)
df=pd.read_csv("Google-Playstore.csv")
print("="*55)

# 1. Find Total Number Apps in Google Play Store

print("The number of apps in playstore : ",df.shape[0])
print("="*55)

# 2. Find the Total Number of Columns in Each app of Google Play Store

print("The total number of columns : ",df.shape[1])
print("="*55)

# 1. Display Top 5 Rows of The Dataset

print("The top five row of the google-playstore : ",df.head())
print("="*55)

# 2. Check the Last 3 Rows of The Dataset

print("The last three rows from the dataset : ",df.tail(3))
print("="*55)

# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)

print("The Shape of Our Dataset (Number of Rows & Number of Columns) : %d , %d" %(df.shape[0],df.shape[1]))
print("="*55)

# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column
#    And  Memory Requirement

print("The total number of rows :",df.shape[0])
print("The total number of column:",df.shape[1])
print(df.info)
print("="*55)

# 5. Get Overall Statistics About The Dataframe

print("Overall Statistics About The Dataframe : ",df.describe())
print("="*55)

# 6. Total Number of App Category Contain Tools
print("Total Number of App Category Contain Tools : ",df[df["Category"].str.contains("Tools",case=False)])
print("="*55)

# 7. Find Average App Rating
print("The average rating of all apps : ",df["Rating"].mean())
print("="*55)

# 8.  Find Total Number of Unique Category
print("The total Number of Unique Category : ",df["Category"].unique())
print("="*55)

# 9. Which Category Getting The Highest Average Rating?
print("The category Getting The Highest Average Rating : \n",df.groupby("Category")["Rating"].mean().sort_values())
print("="*55)

# 10. Find Total Number of App having 5 Star Rating
print("The Total Number of App having 5 Star Rating : ",len(df[df["Rating"]==5]))
print("="*55)

# 11. Find Average Value of Reviews
df.rename(columns={"Rating Count":"review"},inplace=True)
df["review"]=df["review"].astype("float")
print("Average Value of Reviews : ",df["review"].mean())
print("="*55)

# 12. Find Total Number of Free and Paid Apps
print("Total Number of Free and Paid Apps : {} , {} ".format(len(df[df["Price"].astype("float")==0.0]),len(df[df["Price"].astype("float")>0.0])))
print("="*55)

# 13.  Which App Has Maximum Reviews?
print("The app Has Maximum Reviews : ",df.sort_values("review",ascending=False).head(1)["App Name"])
print("="*55)

# 14. Display Top 5 Apps Having Highest Reviews
print("Top 5 Apps Having Highest Reviews : ",df.sort_values("review",ascending=False).head())
print("="*55)

# 15. Find Average Rating of Free and Paid Apps
print("Average Rating of Free and Paid Apps : {}, {}".format(df[df["Price"]==0.0]["review"].mean(),df[df["Price"]>0.0]["review"].mean()))

# 16. Display Top  5 Apps Having Maximum Installs
print("Top  5 Apps Having Maximum Installs : ",df.sort_values("Installs",ascending=False).head())