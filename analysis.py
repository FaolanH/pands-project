# analysis.py
# Project: Analyse the Iris dataset and discuss different ways of presenting the data
# Author: Faolán Hamilton

# ---------- Importing the modules I will need for this project ----------

# this module is used to analyse the data and perform calculations
import numpy as np 

# this module is used to create a DataFrame of the dataset
import pandas as pd 

# this module is used to visualise the data on plots
import matplotlib.pyplot as plt 

# this module is used to visualise the data on more complicated plots
import seaborn as sns 


# ---------- Importing the iris dataset through pandas, the species names can be called directly ----------

pd_iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")


# ---------- Creating an initial summary file for the variables ---------- 
# Source for writing and creating txt files, W3 Schools: https://w3schools.tech/tutorial/python/python_write_to_file

# Features_file
features_file = open("features_file.txt", "w")
features_file.write ("This file is a summary of the four features: sepal length, sepal width, petal length and petal width data from the Iris dataset.")
features_file.close()

# ---------- Dividing the features up ----------
# Source: DataCamp, Intermediate Python, Dictionaries and Pandas Chapter, loc and iloc (https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17)

sepal_length = pd_iris_data.iloc[0:,0]
sepal_width = pd_iris_data.iloc[0:,1]
petal_length = pd_iris_data.iloc[0:,2]
petal_width = pd_iris_data.iloc[0:,3]

# Ensure that the output doesn't include unnecessary data like dtype:float64 (https://stackoverflow.com/questions/74696163/how-to-remove-name-and-dtype-from-output-code)

print (f'Sepal Length is:\n{sepal_length.to_string()}')
print (f'Sepal Width is:\n{sepal_width.to_string()}')
print (f'Petal Length is:\n{petal_length.to_string()}')
print (f'Petal Width is:\n{petal_width.to_string()}')