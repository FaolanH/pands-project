# analysis.py
# Project: Analyse the Iris dataset and discuss different ways of presenting the data
# Author: Faolán Hamilton

# Source: 1) Setting regions

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

# adding colours to scatterplots
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# ---------- Importing the iris dataset through pandas, the species names can be called directly ----------
# Source: 2) Iris dataset
pd_iris_data = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Had to bring in the iris_data with the species as code name as they would not accept creating an array with a string, used for heatmaps
iris_data = load_iris()

#endregion

# region Summary txt.

# ---------- Creating an initial summary file for the variables ---------- 
# Source for writing and creating txt files, W3 Schools: 3) Creating txt file

#endregion

# region Summary
# ---------- Setting the data needed for the pdDataFrame ----------

# Mean
# Source: 4) np Mean
sl_mean = np.mean(pd_iris_data['sepal_length'])
sw_mean = np.mean(pd_iris_data['sepal_width'])
pl_mean = np.mean(pd_iris_data['petal_length'])
pw_mean = np.mean(pd_iris_data['petal_width'])

# Median 
# Source: 5) np Median
sl_median = np.median(pd_iris_data['sepal_length'])
sw_median = np.median(pd_iris_data['sepal_width'])
pl_median = np.median(pd_iris_data['petal_length'])
pw_median = np.median(pd_iris_data['petal_width'])

# Minimum 
# Source: 6) np Min 
sl_min = np.min(pd_iris_data['sepal_length'])
sw_min = np.min(pd_iris_data['sepal_width'])
pl_min = np.min(pd_iris_data['petal_length'])
pw_min = np.min(pd_iris_data['petal_width'])

# Maximum 
# Source: 7) np Max
sl_max = np.max(pd_iris_data['sepal_length'])
sw_max = np.max(pd_iris_data['sepal_width'])
pl_max = np.max(pd_iris_data['petal_length'])
pw_max = np.max(pd_iris_data['petal_width'])

# Standard Deviation
# Source: 8) Std Dev
sl_stdd = np.std(pd_iris_data['sepal_length'])
sw_stdd = np.std(pd_iris_data['sepal_width'])
pl_stdd = np.std(pd_iris_data['petal_length'])
pw_stdd = np.std(pd_iris_data['petal_width'])

#end region

# region Setosa Sum

# Summary by species
# Setosa

# Setosa Mean 
# Source: 4) np Mean
setosa_sl_mean = np.mean(pd_iris_data.iloc[0:50,0])
setosa_sw_mean = np.mean(pd_iris_data.iloc[0:50,1])
setosa_pl_mean = np.mean(pd_iris_data.iloc[0:50,2])
setosa_pw_mean = np.mean(pd_iris_data.iloc[0:50,3])

# Setosa Median 
# Source: 5) np Median
setosa_sl_median = np.median(pd_iris_data.iloc[0:50,0])
setosa_sw_median = np.median(pd_iris_data.iloc[0:50,1])
setosa_pl_median = np.median(pd_iris_data.iloc[0:50,2])
setosa_pw_median = np.median(pd_iris_data.iloc[0:50,3])

# Setosa Minimum 
# Source: 6) np Min 
setosa_sl_min = np.min(pd_iris_data.iloc[0:50,0])
setosa_sw_min = np.min(pd_iris_data.iloc[0:50,1])
setosa_pl_min = np.min(pd_iris_data.iloc[0:50,2])
setosa_pw_min = np.min(pd_iris_data.iloc[0:50,3])

# Setosa Maximum 
# Source: 7) np Max
setosa_sl_max = np.max(pd_iris_data.iloc[0:50,0])
setosa_sw_max = np.max(pd_iris_data.iloc[0:50,1])
setosa_pl_max = np.max(pd_iris_data.iloc[0:50,2])
setosa_pw_max = np.max(pd_iris_data.iloc[0:50,3])

# Setosa Standard Deviation
# Source: 8) Std Dev
setosa_sl_stdd = np.std(pd_iris_data.iloc[0:50,0])
setosa_sw_stdd = np.std(pd_iris_data.iloc[0:50,1])
setosa_pl_stdd = np.std(pd_iris_data.iloc[0:50,2])
setosa_pw_stdd = np.std(pd_iris_data.iloc[0:50,3])

#endregion

# region Versicolor

# Summary by species
# Versicolor

# Versicolor Mean
# Source: 4) np Mean
vs_sl_mean = np.mean(pd_iris_data.iloc[50:100,0])
vs_sw_mean = np.mean(pd_iris_data.iloc[50:100,1])
vs_pl_mean = np.mean(pd_iris_data.iloc[50:100,2])
vs_pw_mean = np.mean(pd_iris_data.iloc[50:100,3])

# Versicolor Median
# Source: 5) np Median
vs_sl_median = np.median(pd_iris_data.iloc[50:100,0])
vs_sw_median = np.median(pd_iris_data.iloc[50:100,1])
vs_pl_median = np.median(pd_iris_data.iloc[50:100,2])
vs_pw_median = np.median(pd_iris_data.iloc[50:100,3])

# Versicolor Minimum
# Source: 6) np Min 
vs_sl_min= np.min(pd_iris_data.iloc[50:100,0])
vs_sw_min= np.min(pd_iris_data.iloc[50:100,1])
vs_pl_min= np.min(pd_iris_data.iloc[50:100,2])
vs_pw_min= np.min(pd_iris_data.iloc[50:100,3])

# Versicolor Maximum 
# Source: 7) np Max
vs_sl_max = np.max(pd_iris_data.iloc[50:100,0])
vs_sw_max = np.max(pd_iris_data.iloc[50:100,1])
vs_pl_max = np.max(pd_iris_data.iloc[50:100,2])
vs_pw_max = np.max(pd_iris_data.iloc[50:100,3])

# Versicolor Standard Deviation
# Source: 8) Std Dev
vs_sl_stdd = np.std(pd_iris_data.iloc[50:100,0])
vs_sw_stdd = np.std(pd_iris_data.iloc[50:100,1])
vs_pl_stdd = np.std(pd_iris_data.iloc[50:100,2])
vs_pw_stdd = np.std(pd_iris_data.iloc[50:100,3])

#endregion

# region Virginica

# Summary by species
# Virginica

# Virginica Mean
# Source: 4) np Mean
va_sl_mean = np.mean(pd_iris_data.iloc[100:150,0])
va_sw_mean = np.mean(pd_iris_data.iloc[100:150,1])
va_pl_mean = np.mean(pd_iris_data.iloc[100:150,2])
va_pw_mean = np.mean(pd_iris_data.iloc[100:150,3])

# Virginica Median
# Source: 5) np Median
va_sl_median = np.median(pd_iris_data.iloc[100:150,0])
va_sw_median = np.median(pd_iris_data.iloc[100:150,1])
va_pl_median = np.median(pd_iris_data.iloc[100:150,2])
va_pw_median = np.median(pd_iris_data.iloc[100:150,3])

# Virginica Minimum
# Source: 6) np Min 
va_sl_min = np.min(pd_iris_data.iloc[100:150,0])
va_sw_min = np.min(pd_iris_data.iloc[100:150,1])
va_pl_min = np.min(pd_iris_data.iloc[100:150,2])
va_pw_min = np.min(pd_iris_data.iloc[100:150,3])

# Virginica Maximum 
# Source: 7) np Max
va_sl_max = np.max(pd_iris_data.iloc[100:150,0])
va_sw_max = np.max(pd_iris_data.iloc[100:150,1])
va_pl_max = np.max(pd_iris_data.iloc[100:150,2])
va_pw_max = np.max(pd_iris_data.iloc[100:150,3])

# Virginica Standard Deviation
# Source: 8) Std Dev
va_sl_stdd = np.std(pd_iris_data.iloc[100:150,0])
va_sw_stdd = np.std(pd_iris_data.iloc[100:150,1])
va_pl_stdd = np.std(pd_iris_data.iloc[100:150,2])
va_pw_stdd = np.std(pd_iris_data.iloc[100:150,3])

#end region 

# region DataFrame

# ---------- Creating a DataFrame to show in the summary txt file ----------
# Source: 9) pdDataFrame

summary = {
    "Feature": ["Overall Data", "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Setosa Data", "Setosa Sepal Length", "Setosa Sepal Width", "Setosa Petal Length", "Setosa Petal Width", "Versicolor Data", "Versicolor Sepal Length", "Versicolor Sepal Width", "Versicolor Petal Length", "Versicolor Petal Width", "Virginica Data", "Virginica Sepal Length", "Virginica Sepal Width", "Virginica Petal Length", "Virginica Petal Width"], 
    "Mean": [0, sl_mean, sw_mean, pl_mean, pw_mean, 0, setosa_sl_mean, setosa_sw_mean, setosa_pl_mean, setosa_pw_mean, 0, vs_sl_mean, vs_sw_mean, vs_pl_mean, vs_pw_mean, 0, va_sl_mean, va_sw_mean, va_pl_mean, va_pw_mean],
    "Median": [0, sl_median, sw_median, pl_median, pw_median, 0, setosa_sl_median, setosa_sw_median, setosa_pl_median, setosa_pw_median, 0, vs_sl_median, vs_sw_median, vs_pl_median, vs_pw_median, 0, va_sl_median, va_sw_median, va_pl_median, va_pw_median], 
    "Minimum": [0, sl_min, sw_min, pl_min, pw_min, 0, setosa_sl_min, setosa_sw_min, setosa_pl_min, setosa_pw_min, 0,vs_sl_min, vs_sw_min, vs_pl_min, vs_pw_min, 0, va_sl_min, va_sw_min, va_pl_min, va_pw_min], 
    "Maximum": [0, sl_max, sw_max, pl_max, pw_max, 0, setosa_sl_max, setosa_sw_max, setosa_pl_max, setosa_pw_max, 0, vs_sl_max, vs_sw_max, vs_pl_max, vs_pw_max, 0, va_sl_max, va_sw_max, va_pl_max, va_pw_max],
    "Standard Deviation": [0, sl_stdd, sw_stdd, pl_stdd, pw_stdd, 0, setosa_sl_stdd, setosa_sw_stdd, setosa_pl_stdd, setosa_pw_stdd, 0, vs_sl_stdd, vs_sw_stdd, vs_pl_stdd, vs_pw_stdd, 0, va_sl_stdd, va_sw_stdd, va_pl_stdd, va_pw_stdd]
}

# Creating the DataFrame of the summary data
summary_df = pd.DataFrame(summary)

# Source: 10) dfround
summary_df['Mean'] = summary_df['Mean'].astype(float).round(1)
summary_df['Median'] = summary_df['Median'].astype(float).round(1)
summary_df['Standard Deviation'] = summary_df['Standard Deviation'].astype(float).round(1)

# endregion

# region File
# Features_file
features_file = open("features_file.txt", "w")
features_file.write("This file is a summary of the four features: sepal length, sepal width, petal length and petal width data from the Iris dataset.")
features_file.write(f'\nThere is a breakdown of each feature by four categories: total, setosa, versicolor and virginica.')
features_file.write(f'\nPlease note that a divider dud column has been included to break down the sections e.g. Overall Data which is listed as 0.0 under each measurement')
features_file.write(f'\nThere are five columns of measurement: Mean (the average), Median (the middle of the data), Minimum (the lowest figure), Maximum (the highest figure) and the Standard Deviation (How much variation there is in a set of data points)')
features_file.write(f'\nSource: 11) Standard Deviation definition: (https://www.geeksforgeeks.org/standard-deviation-formula/)')

features_file.write(f'\n\nThe median, min and max of each variable is plotted on the boxplots, please see the boxplot_outputs folder.\n')
features_file.write(f'\n\n{summary_df}')
features_file.close()

#endregion

# region Features
# ---------- Dividing the features up to be used throughout the project ----------
# Source: 12) loc and iloc

# Species
setosa = pd_iris_data.iloc[0:50, ]
versicolor = pd_iris_data.iloc[50:100, ]
virginica = pd_iris_data.iloc[100:150, ]

# Sepal Length
sepal_length = pd_iris_data.iloc[0:,0]
setosa_sl = pd_iris_data.iloc[0:50,0]
versicolor_sl = pd_iris_data.iloc[50:100,0]
virginica_sl = pd_iris_data.iloc[100:150,0]

# Sepal Width
sepal_width = pd_iris_data.iloc[0:,1]
setosa_sw = pd_iris_data.iloc[0:50,1]
versicolor_sw = pd_iris_data.iloc[50:100,1]
virginica_sw = pd_iris_data.iloc[100:150,1]

# Petal Length 
petal_length = pd_iris_data.iloc[0:,2]
setosa_pl = pd_iris_data.iloc[0:50,2]
versicolor_pl = pd_iris_data.iloc[50:100,2]
virginica_pl = pd_iris_data.iloc[100:150,2]

# Petal Width
petal_width = pd_iris_data.iloc[0:,3]
setosa_pw = pd_iris_data.iloc[0:50,3]
versicolor_pw = pd_iris_data.iloc[50:100,3]
virginica_pw = pd_iris_data.iloc[100:150,3]

# Source: 13) no background output text
# Ensure that the output does not include unnecessary data like dtype:float64

'''
print(f'Sepal Length is:\n{sepal_length.to_string()}')
print(f'Sepal Width is:\n{sepal_width.to_string()}')
print(f'Petal Length is:\n{petal_length.to_string()}')
print(f'Petal Width is:\n{petal_width.to_string()}')
'''
#endregion

# region SL Boxplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Setting the Sepal Length Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# Source: 16) Fig size

# Setting the plot and figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Setting the sepal length data as one variable
all_sl =(sepal_length, setosa_sl, versicolor_sl, virginica_sl)

# Setting the labels
labels = ['Overall Sepal Length', 'Setosa Sepal Length', 'Versicolor Sepal Length', 'Virginica Sepal Length']

# For this one specifically, I did not need to assign the colours the species, just put in the colours I wanted
colours = ['#E1AD01', '#7c70cb', '#632AC5', '#B9B0E7']

# y tick labels
plt.yticks([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# Setting an appropriate title(I originally learned this method on DataCamp)
plt.title('Iris Species by Sepal Length')
# Setting the x axis label
plt.xlabel('Iris Species')
# Setting the y axis label
plt.ylabel('Sepal Length')

# Setting a background grid for more clarity
plt.grid(True)

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this
# Source: 17) Linepoint 
medianprops = dict(linewidth = 3, color = '#819929')

# Source: 15) Boxplot label and colour I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_sl, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot (Source: 15 Boxplot label and colour)
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# saving the figure in the boxplot outputs named sepal_length_range
plt.savefig('boxplot_outputs/sepal_length_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region SW Boxplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# Setting the Sepal Width Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# Source: 16) Fig size

# Setting the plot and figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Setting the sepal width data as one variable
all_sw =(sepal_width, setosa_sw, versicolor_sw, virginica_sw)

# Setting the labels
labels = ['Overall Sepal Width', 'Setosa Sepal Width', 'Versicolor Sepal Width', 'Virginica Sepal Width']

# For this one specifically, I did not need to assign the colours the species, just put in the colours I wanted
colours = ['#E1AD01', '#7c70cb', '#632AC5', '#B9B0E7']

# y tick labels
plt.yticks([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# Setting an appropriate title(I originally learned this method on DataCamp)
plt.title('Iris Species by Sepal Width')
# Setting the x axis label
plt.xlabel('Iris Species')
# Setting the y axis label
plt.ylabel('Sepal Width')

# Setting a background grid for more clarity
plt.grid(True)

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this
# Source: 17) Linepoint 
medianprops = dict(linewidth = 3, color = '#819929')

# Source: 15) Boxplot label and colour I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_sw, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot (Source: 15 Boxplot label and colour)
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# saving the figure in the boxplot outputs named sepal_width_range
plt.savefig('boxplot_outputs/sepal_width_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion 

# region PL Boxplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Setting the Petal Length Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# Source: 16) Fig size

#Setting the plot and figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Setting the petal length data as one variable
all_pl =(petal_length, setosa_pl, versicolor_pl, virginica_pl)

# Setting the labels
labels = ['Overall Petal Length', 'Setosa Petal Length', 'Versicolor Petal Length', 'Virginica Petal Length']

# For this one specifically, I did not need to assign the colours the species, just put in the colours I wanted
colours = ['#E1AD01', '#7c70cb', '#632AC5', '#B9B0E7']

# y tick labels
plt.yticks([1,2,3,4,5,6,7], ['1cm', '2cm', '3cm', '4cm', '5cm', '6cm', '7cm'])

# Setting an appropriate title(I originally learned this method on DataCamp)
plt.title('Iris Species by Petal Length')
# Setting the x axis label
plt.xlabel('Iris Species')
# Setting the y axis label
plt.ylabel('Petal Length')

# Setting a background grid for more clarity
plt.grid(True)

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this
# Source: 17) Linepoint 
medianprops = dict(linewidth = 3, color = '#819929')

# Source: 15) Boxplot label and colour I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_pl, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot (Source: 15 Boxplot label and colour)
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# saving the figure in the boxplot outputs named petal_length_range
plt.savefig('boxplot_outputs/petal_length_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region PW Boxplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Setting the Petal Width Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours 
# Source: 15) Boxplot label and colour

# Source: 16) Fig size

# Setting the plot and figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Setting the petal width data as one variable
all_pw =(petal_width, setosa_pw, versicolor_pw, virginica_pw)

# Setting the labels
labels = ['Overall Petal Width', 'Setosa Petal Width', 'Versicolor Petal Width', 'Virginica Petal Width']

# For this one specifically, I did not need to assign the colours the species, just put in the colours I wanted
colours = ['#E1AD01', '#7c70cb', '#632AC5', '#B9B0E7']

# y tick labels
plt.yticks([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# Setting an appropriate title(I originally learned this method on DataCamp)
plt.title('Iris Species by Petal Width')
# Setting the x axis label
plt.xlabel('Iris Species')
# Setting the y axis label
plt.ylabel('Petal Width')

# Setting a background grid for more clarity
plt.grid(True)

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this
# Source: 17) Linepoint 
medianprops = dict(linewidth = 3, color = '#819929')

# Source: 15) Boxplot label and colour I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_pw, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot (Source: 15 Boxplot label and colour)
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# saving the figure in the boxplot outputs named petal_width_range
plt.savefig('boxplot_outputs/petal_width_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region SW v SL Scatterplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Sepal Width vs Sepal Width for each species

# I tried to do this scatterplot many ways: selecting all rows and just the sepal width or sepal length column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.
# Source: 18) Setting scatterplot colour

# Setting the x for setosa sepal width(as defined in the 'Features' section)
x1 = setosa_sw

# Setting the y for setosa sepal length(as defined in the 'Features' section)
y1 = setosa_sl

# Setting the x for versicolor sepal width(as defined in the 'Features' section)
x2 = versicolor_sw

# Setting the y for versicolor sepal length(as defined in the 'Features' section)
y2 = versicolor_sl

# Setting the x for virginica sepal width(as defined in the 'Features' section)
x3 = virginica_sw

# Setting the y for virginica sepal length(as defined in the 'Features' section)
y3 = virginica_sl

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the scatterplot using sepal_length data
# Source: 18) Setting scatterplot colour
# Source: 19) Markers
plt.scatter(x1, y1, marker = '*', c = '#7c70cb', label = 'Setosa')
plt.scatter(x2, y2, marker = '*', c = '#632AC5', label = 'Versicolor')
plt.scatter(x3, y3,marker = '*', c = '#B9B0E7', label = 'Virginica')

# Setting the title
plt.title("The sepal width versus sepal length of the Iris flower samples")

# setting the x axis 
plt.xlabel("Sepal width (in centimetres)")

# setting the y axis label
plt.ylabel("Sepal length (in centimetres)")

# setting the xticks to show the cm for the sepal width
plt.xticks([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the yticks to show the cm for the sepal length
plt.yticks([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# showing the legend, which takes the 'labels' identified previously and assigning a shadow for nicer display
plt.legend(shadow = True)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/sepal_length_v_sepal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region SW v PW Scatterplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Sepal Width vs Petal Width for each species

# I tried to do this scatterplot many ways: selecting all rows and just the sepal width or petal width column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.
# Source: 18) Setting scatterplot colour

# Setting the x for setosa sepal width(as defined in the 'Features' section)
x1 = setosa_sw

# Setting the y for setosa petal width(as defined in the 'Features' section)
y1 = setosa_pw

# Setting the x for versicolor sepal width(as defined in the 'Features' section)
x2 = versicolor_sw

# Setting the y for versicolor petal width(as defined in the 'Features' section)
y2 = versicolor_pw

# Setting the x for virginica sepal width(as defined in the 'Features' section)
x3 = virginica_sw

# Setting the y for virginica petal width(as defined in the 'Features' section)
y3 = virginica_pw

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the scatterplot using petal_width data
# Source: 18) Setting scatterplot colour
# Source: 19) Markers
plt.scatter(x1, y1, marker = '*', c = '#7c70cb', label = 'Setosa')
plt.scatter(x2, y2, marker = '*', c = '#632AC5', label = 'Versicolor')
plt.scatter(x3, y3,marker = '*', c = '#B9B0E7', label = 'Virginica')

# Setting the title
plt.title("The sepal width versus petal width of the Iris flower samples")

# setting the x axis 
plt.xlabel("Sepal width (in centimetres)")

# setting the y axis label
plt.ylabel("Petal width (in centimetres)")

# setting the xticks to show the cm for the sepal width
plt.xticks([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the yticks to show the cm for the petal width
plt.yticks([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# showing the legend, which takes the 'labels' identified previously and assigning a shadow for nicer display
plt.legend(shadow = True)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/sepal_width_v_petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region PW v PL Scatterplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Petal Length vs Petal Width for each species

# I tried to do this scatterplot many ways: selecting all rows and just the petal width or petal length column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.
# Source: 18) Setting scatterplot colour

# Setting the x for setosa petal width(as defined in the 'Features' section)
x1 = setosa_pw

# Setting the y for setosa petal length(as defined in the 'Features' section)
y1 = setosa_pl

# Setting the x for versicolor petal width(as defined in the 'Features' section)
x2 = versicolor_pw

# Setting the y for versicolor petal length(as defined in the 'Features' section)
y2 = versicolor_pl

# Setting the x for virginica petal width(as defined in the 'Features' section)
x3 = virginica_pw

# Setting the y for virginica petal length(as defined in the 'Features' section)
y3 = virginica_pl

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the scatterplot using petal_length data
# Source: 18) Setting scatterplot colour
# Source: 19) Markers
plt.scatter(x1, y1, marker = '*', c = '#7c70cb', label = 'Setosa')
plt.scatter(x2, y2, marker = '*', c = '#632AC5', label = 'Versicolor')
plt.scatter(x3, y3,marker = '*', c = '#B9B0E7', label = 'Virginica')

# Setting the title
plt.title("The petal width versus petal length of the Iris flower samples")

# setting the x axis 
plt.xlabel("Petal width (in centimetres)")

# setting the y axis label
plt.ylabel("Petal length (in centimetres)")

# setting the xticks to show the cm for the petal width
plt.xticks([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# setting the yticks to show the cm for the petal length
plt.yticks([1,2,3,4,5,6,7], ['1cm', '2cm', '3cm', '4cm', '5cm', '6cm', '7cm'])

# showing the legend, which takes the 'labels' identified previously and assigning a shadow for nicer display
plt.legend(shadow = True)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/petal_length_v_petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

# region SL v PL Scatterplot

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# Petal Length vs sepal length for each species

# I tried to do this scatterplot many ways: selecting all rows and just the sepal length or petal length column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.
# Source: 18) Setting scatterplot colour

# Setting the x for setosa sepal length(as defined in the 'Features' section)
x1 = setosa_sl

# Setting the y for setosa petal length(as defined in the 'Features' section)
y1 = setosa_pl

# Setting the x for versicolor sepal length(as defined in the 'Features' section)
x2 = versicolor_sl

# Setting the y for versicolor petal length(as defined in the 'Features' section)
y2 = versicolor_pl

# Setting the x for virginica sepal length(as defined in the 'Features' section)
x3 = virginica_sl

# Setting the y for virginica petal length(as defined in the 'Features' section)
y3 = virginica_pl

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the scatterplot using petal_length data
# Source: 18) Setting scatterplot colour
# Source: 19) Markers
plt.scatter(x1, y1, marker = '*', c = '#7c70cb', label = 'Setosa')
plt.scatter(x2, y2, marker = '*', c = '#632AC5', label = 'Versicolor')
plt.scatter(x3, y3,marker = '*', c = '#B9B0E7', label = 'Virginica')

# Setting the title
plt.title("The sepal length versus petal length of the Iris flower samples")

# setting the x axis 
plt.xlabel("Sepal Length (in centimetres)")

# setting the y axis label
plt.ylabel("Petal length (in centimetres)")

# setting the xticks to show the cm for the sepal length
plt.xticks([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# setting the yticks to show the cm for the petal length
plt.yticks([1,2,3,4,5,6,7], ['1cm', '2cm', '3cm', '4cm', '5cm', '6cm', '7cm'])

# showing the legend, which takes the 'labels' identified previously and assigning a shadow for nicer display
plt.legend(shadow = True)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/petal_length_v_sepal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# ---------- Creating histograms for individual features ----------

#region SL Histograms

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Sepal Length ----------

# Setting the title
plt.title("The sepal length of the Iris flower samples")

# setting the x axis 
plt.xlabel("Sepal length (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples")

# setting the xticks to show the cm
plt.xticks([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# setting the plot colours
colours =('#7c70cb')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(sepal_length, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/sepal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region SW Histograms

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Sepal Width ----------

# Setting the title
plt.title("The sepal width of the Iris flower samples")

# setting the x axis 
plt.xlabel("Sepal width (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples")

# setting the xticks to show the cm
plt.xticks([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the plot colours
colours =('#632AC5')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_width data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(sepal_width, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/sepal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PL Histograms

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Petal Length ----------

# Setting the title
plt.title("The petal length of the Iris flower samples")

# setting the x axis 
plt.xlabel("Petal length (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples")

# setting the xticks to show the cm
plt.xticks([1,2,3,4,5,6,7], ["1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm"])

# setting the plot colours
colours =('#E1AD01')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_length data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(petal_length, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/petal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

#region PL Histograms

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Petal width ----------

# Setting the title
plt.title("The petal width of the Iris flower samples")

# setting the x axis 
plt.xlabel("Petal Width (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples")

# setting the xticks to show the cm
plt.xticks([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# setting the plot colours
colours =('#819929')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_width data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(petal_width, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region SL Species Hist

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Creating histograms for individual features by species ----------

# Attempting to plot three bars on one histogram - I originally attempted to do this with the pd_iris_data but then thought because the species name was a string not a float, I could not create the array I needed to plot all three on the one! It turned out I did not need to create a numpy array at all and ended up not using that dataset for this.
# Source: 24) Assigning hist colours

# ---------- Sepal Length ----------

# Source: 23) Chapter Matplotlib

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
# Source: 22) Setting the edgecolour
# Source: 26) patches
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# Source: 25) Legend Styling
# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# pulling all three together into one variable
species_sl =([setosa_sl, versicolor_sl, virginica_sl])

# Setting the title
plt.title("The sepal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel("Sepal length (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples per species")

# setting the xticks to show the cm
plt.xticks([4.5,5.0,5.5,6.0,6.5,7.0,7.5, 8.0], ["4.5cm", "5cm", "5.5cm", "6cm", "6.5cm", "7cm", "7.5cm", "8cm"])

# setting the colours(based on the actual iris species colours as described in the README.md)
colours =('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_length data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(species_sl, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/sepal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

# region SW Species Hist

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Sepal Width ----------

# Source: 23) Chapter Matplotlib

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
# Source: 22) Setting the edgecolour
# Source: 26) patches
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# Source: 25) Legend Styling
# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper left', shadow = True)

# pulling all three together into one variable 
species_sw =([setosa_sw, versicolor_sw, virginica_sw])

# Setting the title
plt.title("The sepal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel("Sepal width (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples per species")

# setting the xticks to show the cm
plt.xticks([2.0,2.5,3.0,3.5,4.0,4.5], ["2cm", "2.5cm", "3cm", "3.5cm", "4cm", "4.5cm"])

# setting the colours(based on the actual iris species colours as described in the README.md)
colours =('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using sepal_width data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(species_sw, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/sepal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PL Species Hist

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Petal Length ----------

# Source: 23) Chapter Matplotlib

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
# Source: 22) Setting the edgecolour
# Source: 26) patches
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# Source: 25) Legend Styling
# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# pulling all three together into one variable
species_pl =([setosa_pl, versicolor_pl, virginica_pl])

# Setting the title
plt.title("The petal length of the Iris flower samples by species")

# setting the x axis 
plt.xlabel("Petal length (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples per species")

# setting the xticks to show the cm
plt.xticks([1,2,3,4,5,6,7], ["1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm"])

# setting the colours(based on the actual iris species colours as described in the README.md)
colours =('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_length data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(species_pl, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/petal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PW Species Hist

# The additions (adding in tick marks, labels, titles etc.) of most plots throughout this notebook is inspired from DataCamp
# Source: 14) Plot Additions

# ---------- Petal width ----------

# Source: 23) Chapter Matplotlib

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
# Source: 22) Setting the edgecolour
# Source: 26) patches
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

# Source: 25) Legend Styling
# plotting the legend
ax.legend(handles=[setosa, versicolor, virginica], loc = 'upper right', shadow = True)

# pulling all three together into one variable
species_pw =([setosa_pw, versicolor_pw, virginica_pw])

# Setting the title
plt.title("The petal width of the Iris flower samples by species")

# setting the x axis 
plt.xlabel("Petal Width (in centimetres)")

# setting the y axis label
plt.ylabel("Number of samples per species")

# setting the xticks to show the cm
plt.xticks([0.5,1,1.5,2,2.5], ["0.5cm", "1cm", "1.5cm", "2cm", "2.5cm"])

# setting the colours(based on the actual iris species colours as described in the README.md)
colours =('#7c70cb', '#632AC5', '#B9B0E7')

# setting a grid for context
plt.grid(linewidth = 0.5, c = 'grey', alpha = 0.2)

# plotting the histogram using petal_width data, with 10 bins(or bars)
# Source: 22) Setting the edgecolour
plt.hist(species_pw, bins = 10, edgecolor = 'black', color = colours)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the histogram outputs folder
plt.savefig('histogram_outputs/petal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region Heatmap

# In order for Heatmaps to display correctly, there has to be enough data to compare. Using the numpy coefficient module allowed the data to compared crossways
# The structure of heatmaps was a mixture of two sources: Source 28) Tutorial Colormaps and 29) colors.Colormap
# Source: 31) Numpy Coefficient
data = np.corrcoef(iris_data.data)

# Setting the colours 
colours = ['#5A4FCF','#897CAC', '#AC37B2', '#658F3A', '#E1AD01']
# Source: 27) ListedColorMap
cmap = ListedColormap(colours)

# Making the plot bigger
# Source 16) Fig size
plt.figure (figsize=(12,12))

# Setting the title
plt.title('Correlation between features in the Iris dataset')

# Adding in a note (Source 23) Chapter Matplotlib)
plt.text (-6,-10,'*Note: Yellow and green indicate a stronger correlation, whereas purple indicate a weaker correlation')

# Setting the y ticks
#plt.yticks ([0,1,2,3,4,], ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species'])
# Setting the x ticks
#plt.xticks ([0,1,2,3,4,], ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species'])

# Plotting the data
plt.imshow(data, cmap = cmap)
plt.grid(True, color = 'w')
plt.colorbar()

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the heatmap outputs folder
plt.savefig('heatmap_outputs/heatmap', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region Pairplot

# using the seaborn module that was previously imported
# Source: 30) Pairplot
palette_colors = {'setosa':'#7c70cb', 'versicolor' : '#632AC5', 'virginica' : '#B9B0E7'}
sns.pairplot(pd_iris_data, hue ='species', palette=palette_colors)

# Source: 20) Saving figures
# Using a forward slash for the path helped to not throw an error
# Source: 21) Forward Slash when saving figure
# Saving the figure in the pairplot outputs folder
plt.savefig('pairplot_outputs/pairplot', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region References:

# 1) Setting regions: Stack overflow (https://stackoverflow.com/questions/8265583/dividing-python-module-into-multiple-regions)
# 2) Iris dataset: GitHub (https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv)
# 3) Creating txt file: W3 Schools (https://w3schools.tech/tutorial/python/python_write_to_file)
# 4) np Mean: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
# 5) np Median: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.median.html)
# 6) np Min: Numpy (https://numpy.org/doc/stable//reference/generated/numpy.min.html)
# 7) np Max: Numpy (https://numpy.org/doc/stable//reference/generated/numpy.max.html)
# 8) np Std Dev: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.std.html)
# 9) pdDataFrame: GeeksforGeeks (https://www.geeksforgeeks.org/how-to-make-a-table-in-python/#using-prettytable)
# 10) dfround: Stack overflow (https://stackoverflow.com/questions/38255796/pandas-round-is-not-working-for-dataframe)
# 11) Standard Deviation definition: GeeksforGeeks(https://www.geeksforgeeks.org/standard-deviation-formula/)
# 12) loc and iloc: DataCamp (https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17)
# 13) no background output text: Stack overflow (https://stackoverflow.com/questions/74696163/how-to-remove-name-and-dtype-from-output-code)
# 14) Plot Additions: DataCamp (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)
# 15) Boxplot label and colour: (Matplotlib (https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py)
# 16) Fig size: How2Matplotlib (fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html)
# 17) Linepoint: Matplotlib (https://matplotlib.org/stable/gallery/statistics/boxplot.html)
# 18) Setting scatterplot colour: Python Examples (https://pythonexamples.org/matplotlib-scatter-plot-color/)
# 19) Markers: Matplotlib (https://matplotlib.org/stable/api/markers_api.html)
# 20) Saving figures: Stack overflow (https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it)
# 21) Forward Slash when saving figure: DNM (https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/)
# 22) Setting the edgecolour: Matplotlib (https://matplotlib.org/stable/api/figure_api.html)
# 23) Chapter Matplotlib: DataCamp (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)
# 24) Assigning hist colours: Matplotlib (https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)
# 25) Legend Styling: Matplotlib (https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries)
# 26) patches: Matplotlib (https://matplotlib.org/stable/api/patches_api.html)
# 27) ListedColorMap: Matplotlib (https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html)
# 28) Tutorial Colormaps: DataCamp (https://www.datacamp.com/tutorial/matplotlib-colormaps)
# 29) colors.Colormap: GeeksforGeeks (https://www.geeksforgeeks.org/matplotlib-colors-colormap-class-in-python/)
# 30) Pairplot: GeeksforGeeks (https://www.geeksforgeeks.org/python-seaborn-pairplot-method/)
# 31) Numpy Coefficient: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)

#endregion

# ---------- END ---------