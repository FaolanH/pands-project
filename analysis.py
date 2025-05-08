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

# shows the output as a table
from tabulate import tabulate

# ---------- Importing the iris dataset through pandas, the species names can be called directly ----------

pd_iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Had to bring in the iris_data with the species as code name as they would not accept creating an array with a string
iris_data = load_iris()

#endregion

# region Summary txt.

# ---------- Creating an initial summary file for the variables ---------- 
# Source for writing and creating txt files, W3 Schools: https://w3schools.tech/tutorial/python/python_write_to_file

# ---------- Creating a DataFrame to show in the summary txt file ----------
# Mean
sl_mean = np.mean(pd_iris_data['sepal_length'])
sw_mean = np.mean(pd_iris_data['sepal_width'])
pl_mean = np.mean(pd_iris_data['petal_length'])
pw_mean = np.mean(pd_iris_data['petal_width'])

# Median 
sl_median = np.median(pd_iris_data['sepal_length'])
sw_median = np.median(pd_iris_data['sepal_width'])
pl_median = np.median(pd_iris_data['petal_length'])
pw_median = np.median(pd_iris_data['petal_width'])

# Minimum 
sl_minimum = np.min(pd_iris_data['sepal_length'])
sw_minimum = np.min(pd_iris_data['sepal_width'])
pl_minimum = np.min(pd_iris_data['petal_length'])
pw_minimum = np.min(pd_iris_data['petal_width'])

# Maximum 
sl_maximum = np.max(pd_iris_data['sepal_length'])
sw_maximum = np.max(pd_iris_data['sepal_width'])
pl_maximum = np.max(pd_iris_data['petal_length'])
pw_maximum = np.max(pd_iris_data['petal_width'])

# Standard Deviation
sl_stdd = np.std(pd_iris_data['sepal_length'])
sw_stdd = np.std(pd_iris_data['sepal_width'])
pl_stdd = np.std(pd_iris_data['petal_length'])
pw_stdd = np.std(pd_iris_data['petal_width'])

# Summary by species

# Setosa Mean
setosa_sl_mean = np.mean(pd_iris_data.iloc[0:50,0])
setosa_sw_mean = np.mean(pd_iris_data.iloc[0:50,1])
setosa_pl_mean = np.mean(pd_iris_data.iloc[0:50,2])
setosa_pw_mean = np.mean(pd_iris_data.iloc[0:50,3])
'''
# Median 
setosa_sl_median = np.median(pd_iris_data['sepal_length'])
setosa_sw_median = np.median(pd_iris_data['sepal_width'])
setosa_pl_median = np.median(pd_iris_data['petal_length'])
setosa_pw_median = np.median(pd_iris_data['petal_width'])

# Minimum 
setosa_sl_minimum = np.min(pd_iris_data['sepal_length'])
setosa_sw_minimum = np.min(pd_iris_data['sepal_width'])
setosa_pl_minimum = np.min(pd_iris_data['petal_length'])
setosa_pw_minimum = np.min(pd_iris_data['petal_width'])

# Maximum 
setosa_sl_maximum = np.max(pd_iris_data['sepal_length'])
setosa_sw_maximum = np.max(pd_iris_data['sepal_width'])
setosa_pl_maximum = np.max(pd_iris_data['petal_length'])
setosa_pw_maximum = np.max(pd_iris_data['petal_width'])

# Standard Deviation
setosa_sl_stdd = np.std(pd_iris_data['sepal_length'])
setosa_sw_stdd = np.std(pd_iris_data['sepal_width'])
setosa_pl_stdd = np.std(pd_iris_data['petal_length'])
setosa_pw_stdd = np.std(pd_iris_data['petal_width'])

summary = {
    "Feature": ["Sepal Length", "Sepal Width", "Petal Length","Petal Width"], 
    "Mean": [sl_mean, sw_mean, pl_mean, pw_mean],
    "Median": [sl_median, sw_median, pl_median, pw_median], 
    "Minimum": [sl_minimum, sw_minimum, pl_minimum, pw_minimum], 
    "Maximum": [sl_maximum, sw_maximum, pl_maximum, pw_maximum],
    "Standard Deviation": [sl_stdd, sw_stdd, pl_stdd, pw_stdd],
    "Setosa": ["----", "----", "----", "----"],
    "Setosa Mean": [setosa_sl_mean, setosa_sw_mean, setosa_pl_mean, setosa_pw_mean]
}
'''

summary = {
    "Feature": ["Mean", "Median", "Minimum", "Maximum", "Standard Deviation"],
    "Sepal Length": [sl_mean, sl_median, sl_minimum, sl_maximum, sl_stdd], 
    "Sepal Width": [sw_mean, sw_median, sw_minimum, sw_maximum, sw_stdd], 
    "Petal Length": [pl_mean, pl_median, pl_minimum, pl_maximum, pl_stdd]
}
# Creating the DataFrame of the summary data
summary_df = pd.DataFrame(summary)

# Features_file
features_file = open("features_file.txt", "w")
features_file.write ("This file is a summary of the four features: sepal length, sepal width, petal length and petal width data from the Iris dataset.")
features_file.write (f'\n\n{summary_df}')
features_file.close()

#print (f'The mean sepal length is {sl_mean:.4f}')
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

# ---------- Creating histograms for individual features ----------

# ---------- Sepal Length ----------

# Setting the data location 0:150 sets all rows (0) up to but not including 150 (aka 149). The ,0 that follows sets the column (sepal_length) and so on.
sl = pd_iris_data.iloc[0:150,0]

# Setting the title
plt.title("The sepal length of the Iris flower samples")

# setting the x axis 
plt.xlabel ("Sepal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples")

# setting the xticks to show the cm
plt.xticks ([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# setting the plot colours
colours = ('#7c70cb')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 10 bins (or bars)
plt.hist (sl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

# ---------- Sepal Width ----------

# Setting the data location 0:150 sets all rows (0) up to but not including 150 (aka 149). The ,1 that follows sets the column (sepal_width) and so on.
sw = pd_iris_data.iloc[0:150,1]

# Setting the title
plt.title("The sepal width of the Iris flower samples")

# setting the x axis 
plt.xlabel ("Sepal width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples")

# setting the xticks to show the cm
plt.xticks ([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the plot colours
colours = ('#632AC5')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_width data, with 10 bins (or bars)
plt.hist (sw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

# ---------- Petal Length ----------

# Setting the data location 0:150 sets all rows (0) up to but not including 150 (aka 149). The ,2 that follows sets the column (petal_length) and so on.
pl = pd_iris_data.iloc[0:150,2]

# Setting the title
plt.title("The petal length of the Iris flower samples")

# setting the x axis 
plt.xlabel ("Petal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples")

# setting the xticks to show the cm
plt.xticks ([1,2,3,4,5,6,7], ["1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm"])

# setting the plot colours
colours = ('#E1AD01')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_length data, with 10 bins (or bars)
plt.hist (pl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close ()

# ---------- Petal width ----------

# Setting the data location 0:150 sets all rows (0) up to but not including 150 (aka 149). The ,3 that follows sets the column (petal_width) and so on.
pw = pd_iris_data.iloc[0:150,3]

# Setting the title
plt.title("The petal width of the Iris flower samples")

# setting the x axis 
plt.xlabel ("Petal Width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples")

# setting the xticks to show the cm
plt.xticks ([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# setting the plot colours
colours = ('#819929')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 10 bins (or bars)
plt.hist (pw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

#endregion

# region Hist Species

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

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,0 that follows sets the column (sepal_length) and so on.
setosa_sl = pd_iris_data.iloc[0:50,0]
versicolor_sl = pd_iris_data.iloc[50:100,0]
virginica_sl = pd_iris_data.iloc[100:150,0]

# pulling all three together into one variable
sl = ([setosa_sl, versicolor_sl, virginica_sl])

# Setting the title
plt.title("The sepal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Sepal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# setting the colours (based on the actual iris species colours as described in the README.md)
colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 10 bins (or bars)
plt.hist (sl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

# ---------- Sepal Width ----------

# to show the legend, this needs to be brought in as a sub plot
fig,ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica =  mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper left', shadow = True)

# Setting the data location for each of the species: 0:50 sets the first row (0) up to but not including 50 (aka 49) which is all the setosa data. The ,1 that follows sets the column (sepal width) and so on.
setosa_sw = pd_iris_data.iloc[0:50,1]
versicolor_sw = pd_iris_data.iloc[50:100,1]
virginica_sw = pd_iris_data.iloc[100:150,1]

# pulling all three together into one variable 
sw = ([setosa_sw, versicolor_sw, virginica_sw])

# Setting the title
plt.title("The sepal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Sepal width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the colours (based on the actual iris species colours as described in the README.md)
colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_width data, with 10 bins (or bars)
plt.hist (sw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

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

# pulling all three together into one variable
pl = ([setosa_pl, versicolor_pl, virginica_pl])

# Setting the title
plt.title("The petal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Petal length (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([1,2,3,4,5,6,7], ["1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm"])

# setting the colours (based on the actual iris species colours as described in the README.md)
colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_length data, with 10 bins (or bars)
plt.hist (pl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

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

# pulling all three together into one variable
pw = ([setosa_pw, versicolor_pw, virginica_pw])

# Setting the title
plt.title("The petal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel ("Petal Width (in centimeters)")

# setting the y axis label
plt.ylabel ("Number of samples per species")

# setting the xticks to show the cm
plt.xticks ([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# setting the colours (based on the actual iris species colours as described in the README.md)
colours = ('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_width data, with 10 bins (or bars)
plt.hist (pw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it doesn't go onto the graph
plt.close()

#endregion
