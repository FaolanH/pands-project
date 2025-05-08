# analysis.py
# Project: Analyse the Iris dataset and discuss different ways of presenting the data
# Author: Faolán Hamilton

# Source: https://stackoverflow.com/questions/8265583/dividing-python-module-into-multiple-regions
# region Import
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

# bringing in mpatches allows the legend to be set easily
import matplotlib.patches as mpatches


# ---------- Importing the iris dataset through pandas, the species names can be called directly ----------

pd_iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Had to bring in the iris_data with the species as code name as they would not accept creating an array with a string
iris_data = load_iris()

#endregion

# region Summary txt.

# ---------- Creating an initial summary file for the variables ---------- 
# Source for writing and creating txt files, W3 Schools: https://w3schools.tech/tutorial/python/python_write_to_file

# Features_file
features_file = open("features_file.txt", "w")
features_file.write ("This file is a summary of the four features: sepal length, sepal width, petal length and petal width data from the Iris dataset.")
features_file.close()

#endregion

# region Features
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
#endregion

#region Histograms
# ---------- Creating histograms for individual features by species ----------

# Source: DataCamp, Intermediate Python, Chapter Matplotlib (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)

# Attempting to plot three bars on one histogram - I orginally attempted to do this with the pd_iris_data, but then thought because the species name was a string not a float, I coudln't create the array I needed to plot all three on the one! It turned out I didn't need to create a numpy array at all, and ended up not using that dataset for this.
# Source: https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html
# Source: https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries
# Source: https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it

# ---------- Sepal Length ----------

# to show the legend, this needs to be brought in as a sub plot
fig,ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica =  mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,1 that follows sets the column (sepal width)
setosa_sl = pd_iris_data.iloc[0:50,0]
versicolor_sl = pd_iris_data.iloc[50:100,0]
virginica_sl = pd_iris_data.iloc[100:150,0]

# pulling all three 
sl = ([setosa_sl, versicolor_sl, virginica_sl])

# Setting the title
plt.title("The sepal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Sepal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 20 bins (or bars)
plt.hist (sl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_length_species_comparison', bbox_inches = 'tight')


# ---------- Sepal Width ----------

# to show the legend, this needs to be brought in as a sub plot
fig,ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica =  mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper left', shadow = True)

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,1 that follows sets the column (sepal width)
setosa_sw = pd_iris_data.iloc[0:50,1]
versicolor_sw = pd_iris_data.iloc[50:100,1]
virginica_sw = pd_iris_data.iloc[100:150,1]

# pulling all three 
sw = ([setosa_sw, versicolor_sw, virginica_sw])

# Setting the title
plt.title("The sepal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Sepal width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 20 bins (or bars)
plt.hist (sw, bins = 8, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_width_species_comparison', bbox_inches = 'tight')

# ---------- Petal Length ----------

# to show the legend, this needs to be brought in as a sub plot
fig,ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica =  mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,1 that follows sets the column (sepal width)
setosa_pl = pd_iris_data.iloc[0:50,2]
versicolor_pl = pd_iris_data.iloc[50:100,2]
virginica_pl = pd_iris_data.iloc[100:150,2]

# pulling all three 
pl = ([setosa_pl, versicolor_pl, virginica_pl])

# Setting the title
plt.title("The petal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Petal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([1,2,3,4,5,6,7], ["1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm"])

colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 20 bins (or bars)
plt.hist (pl, bins = 8, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_length_species_comparison', bbox_inches = 'tight')

# ---------- Petal width ----------

# to show the legend, this needs to be brought in as a sub plot
fig,ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica =  mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,1 that follows sets the column (sepal width)
setosa_pw = pd_iris_data.iloc[0:50,3]
versicolor_pw = pd_iris_data.iloc[50:100,3]
virginica_pw = pd_iris_data.iloc[100:150,3]

# pulling all three 
pw = ([setosa_pw, versicolor_pw, virginica_pw])

# Setting the title
plt.title("The petal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Petal Width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 20 bins (or bars)
plt.hist (pw, bins = 8, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_width_species_comparison', bbox_inches = 'tight')

#endregion
