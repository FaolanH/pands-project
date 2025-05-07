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

# this module is used to bring in the dataset in a different form
from sklearn.datasets import load_iris


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
'''
print (f'Sepal Length is:\n{sepal_length.to_string()}')
print (f'Sepal Width is:\n{sepal_width.to_string()}')
print (f'Petal Length is:\n{petal_length.to_string()}')
print (f'Petal Width is:\n{petal_width.to_string()}')
'''

# ---------- Breaking down by species ----------

setosa = pd_iris_data.iloc[0:50,]
versicolor = pd_iris_data.iloc[50:100,]
virginica = pd_iris_data.iloc[100:,]


setosa_sw = pd_iris_data.iloc[0:50,1]
versicolor_sw = pd_iris_data.iloc[50:100,1]
virginica_sw = pd_iris_data.iloc[100:,1]

sw = ([setosa_sw, versicolor_sw, virginica_sw])

sepal_width_sw = np.array(setosa, pd_iris_data.iloc[0:,1])

# ---------- Creating histograms for individual features ----------
# Source: DataCamp, Intermediate Python, Chapter Matplotlib (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)

# Sepal Length Histogram 
'''
# setting the colours
colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# plotting the histogram using sepal_length data, with 20 bins (or bars)
plt.hist (sw, bins = 20, edgecolor = 'black')#, color = colours)

# setting the xticks to show the cm
plt.xticks ([4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# Setting the title
plt.title("The sepal length of the Iris flower samples")

# setting the x axis 
plt.xlabel ("Sepal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per bin")

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# showing the plot
plt.show()


# Attempting to plot three bars on one histogram

x = np.random.randn(1000, 3)

colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# plotting the histogram using sepal_length data, with 20 bins (or bars)
#plt.hist (sepal_width_sw, bins = 20, edgecolor = 'black', color = colours)

#plt.show()

#print (sepal_width_sw)
'''
