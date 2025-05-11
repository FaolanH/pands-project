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

from matplotlib import colors as mcolors

# adding colours to scatterplots
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# shows the output as a table
from tabulate import tabulate

# ---------- Importing the iris dataset through pandas, the species names can be called directly ----------

pd_iris_data = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Had to bring in the iris_data with the species as code name as they would not accept creating an array with a string
iris_data = load_iris()

#endregion

# region Summary txt.

# ---------- Creating an initial summary file for the variables ---------- 
# Source for writing and creating txt files, W3 Schools: https://w3schools.tech/tutorial/python/python_write_to_file

#endregion

# region Summary
# ---------- Creating a DataFrame to show in the summary txt file ----------
# Source: https://www.geeksforgeeks.org/how-to-make-a-table-in-python/#using-prettytable

# Mean
# Source: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
sl_mean = np.mean(pd_iris_data['sepal_length'])
sw_mean = np.mean(pd_iris_data['sepal_width'])
pl_mean = np.mean(pd_iris_data['petal_length'])
pw_mean = np.mean(pd_iris_data['petal_width'])

# Median 
# Source: https://numpy.org/doc/stable/reference/generated/numpy.median.html
sl_median = np.median(pd_iris_data['sepal_length'])
sw_median = np.median(pd_iris_data['sepal_width'])
pl_median = np.median(pd_iris_data['petal_length'])
pw_median = np.median(pd_iris_data['petal_width'])

# Minimum 
# Source: https://numpy.org/doc/stable//reference/generated/numpy.min.html
sl_min = np.min(pd_iris_data['sepal_length'])
sw_min = np.min(pd_iris_data['sepal_width'])
pl_min = np.min(pd_iris_data['petal_length'])
pw_min = np.min(pd_iris_data['petal_width'])

# Maximum 
# Source: https://numpy.org/doc/stable//reference/generated/numpy.max.html
sl_max = np.max(pd_iris_data['sepal_length'])
sw_max = np.max(pd_iris_data['sepal_width'])
pl_max = np.max(pd_iris_data['petal_length'])
pw_max = np.max(pd_iris_data['petal_width'])

# Standard Deviation
# Source: https://numpy.org/doc/stable/reference/generated/numpy.std.html
sl_stdd = np.std(pd_iris_data['sepal_length'])
sw_stdd = np.std(pd_iris_data['sepal_width'])
pl_stdd = np.std(pd_iris_data['petal_length'])
pw_stdd = np.std(pd_iris_data['petal_width'])

#end region

# region Setosa Sum

# Summary by species
# Setosa

# Setosa Mean
setosa_sl_mean = np.mean(pd_iris_data.iloc[0:50,0])
setosa_sw_mean = np.mean(pd_iris_data.iloc[0:50,1])
setosa_pl_mean = np.mean(pd_iris_data.iloc[0:50,2])
setosa_pw_mean = np.mean(pd_iris_data.iloc[0:50,3])

# Setosa Median 
setosa_sl_median = np.median(pd_iris_data.iloc[0:50,0])
setosa_sw_median = np.median(pd_iris_data.iloc[0:50,1])
setosa_pl_median = np.median(pd_iris_data.iloc[0:50,2])
setosa_pw_median = np.median(pd_iris_data.iloc[0:50,3])

# Setosa Minimum 
setosa_sl_min = np.min(pd_iris_data.iloc[0:50,0])
setosa_sw_min = np.min(pd_iris_data.iloc[0:50,1])
setosa_pl_min = np.min(pd_iris_data.iloc[0:50,2])
setosa_pw_min = np.min(pd_iris_data.iloc[0:50,3])

# Setosa Maximum 
setosa_sl_max = np.max(pd_iris_data.iloc[0:50,0])
setosa_sw_max = np.max(pd_iris_data.iloc[0:50,1])
setosa_pl_max = np.max(pd_iris_data.iloc[0:50,2])
setosa_pw_max = np.max(pd_iris_data.iloc[0:50,3])

# Setosa Standard Deviation
setosa_sl_stdd = np.std(pd_iris_data.iloc[0:50,0])
setosa_sw_stdd = np.std(pd_iris_data.iloc[0:50,1])
setosa_pl_stdd = np.std(pd_iris_data.iloc[0:50,2])
setosa_pw_stdd = np.std(pd_iris_data.iloc[0:50,3])

#endregion

# region Versicolor

# Summary by species
# Versicolor

# Versicolor Mean
vs_sl_mean = np.mean(pd_iris_data.iloc[50:100,0])
vs_sw_mean = np.mean(pd_iris_data.iloc[50:100,1])
vs_pl_mean = np.mean(pd_iris_data.iloc[50:100,2])
vs_pw_mean = np.mean(pd_iris_data.iloc[50:100,3])

# Versicolor Median
vs_sl_median = np.median(pd_iris_data.iloc[50:100,0])
vs_sw_median = np.median(pd_iris_data.iloc[50:100,1])
vs_pl_median = np.median(pd_iris_data.iloc[50:100,2])
vs_pw_median = np.median(pd_iris_data.iloc[50:100,3])

# Versicolor Minimum
vs_sl_min= np.min(pd_iris_data.iloc[50:100,0])
vs_sw_min= np.min(pd_iris_data.iloc[50:100,1])
vs_pl_min= np.min(pd_iris_data.iloc[50:100,2])
vs_pw_min= np.min(pd_iris_data.iloc[50:100,3])

# Versicolor Maximum 
vs_sl_max = np.max(pd_iris_data.iloc[50:100,0])
vs_sw_max = np.max(pd_iris_data.iloc[50:100,1])
vs_pl_max = np.max(pd_iris_data.iloc[50:100,2])
vs_pw_max = np.max(pd_iris_data.iloc[50:100,3])

# Versicolor Standard Deviation
vs_sl_stdd = np.std(pd_iris_data.iloc[50:100,0])
vs_sw_stdd = np.std(pd_iris_data.iloc[50:100,1])
vs_pl_stdd = np.std(pd_iris_data.iloc[50:100,2])
vs_pw_stdd = np.std(pd_iris_data.iloc[50:100,3])

#endregion

# region Virginica

# Summary by species
# Virginica

# Virginica Mean
va_sl_mean = np.mean(pd_iris_data.iloc[100:150,0])
va_sw_mean = np.mean(pd_iris_data.iloc[100:150,1])
va_pl_mean = np.mean(pd_iris_data.iloc[100:150,2])
va_pw_mean = np.mean(pd_iris_data.iloc[100:150,3])

# Virginica Median
va_sl_median = np.median(pd_iris_data.iloc[100:150,0])
va_sw_median = np.median(pd_iris_data.iloc[100:150,1])
va_pl_median = np.median(pd_iris_data.iloc[100:150,2])
va_pw_median = np.median(pd_iris_data.iloc[100:150,3])

# Virginica Minimum
va_sl_min = np.min(pd_iris_data.iloc[100:150,0])
va_sw_min = np.min(pd_iris_data.iloc[100:150,1])
va_pl_min = np.min(pd_iris_data.iloc[100:150,2])
va_pw_min = np.min(pd_iris_data.iloc[100:150,3])

# Virginica Maximum 
va_sl_max = np.max(pd_iris_data.iloc[100:150,0])
va_sw_max = np.max(pd_iris_data.iloc[100:150,1])
va_pl_max = np.max(pd_iris_data.iloc[100:150,2])
va_pw_max = np.max(pd_iris_data.iloc[100:150,3])

# Virginica Standard Deviation
va_sl_stdd = np.std(pd_iris_data.iloc[100:150,0])
va_sw_stdd = np.std(pd_iris_data.iloc[100:150,1])
va_pl_stdd = np.std(pd_iris_data.iloc[100:150,2])
va_pw_stdd = np.std(pd_iris_data.iloc[100:150,3])

#end region 

# region DataFrame
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

# Source: https://stackoverflow.com/questions/38255796/pandas-round-is-not-working-for-dataframe
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
features_file.write(f'\nSource for Standard Deviation definition: (https://www.geeksforgeeks.org/standard-deviation-formula/)')

features_file.write(f'\n\nThe median, min and max of each variable is plotted on the boxplots, please see the boxplot_outputs folder.\n')
features_file.write(f'\n\n{summary_df}')
features_file.close()

#endregion

# region Features
# ---------- Dividing the features up to be used throughout the project ----------
# Source: DataCamp, Intermediate Python, Dictionaries and Pandas Chapter, loc and iloc(https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17)

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

# Ensure that the output does not include unnecessary data like dtype:float64(https://stackoverflow.com/questions/74696163/how-to-remove-name-and-dtype-from-output-code)
'''
print(f'Sepal Length is:\n{sepal_length.to_string()}')
print(f'Sepal Width is:\n{sepal_width.to_string()}')
print(f'Petal Length is:\n{petal_length.to_string()}')
print(f'Petal Width is:\n{petal_width.to_string()}')
'''
#endregion

# region SL Boxplot

# Setting the Sepal Length Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py
# Source: fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html

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

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this(https://matplotlib.org/stable/gallery/statistics/boxplot.html)
# Source: linestyle - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
medianprops = dict(linewidth = 3, color = '#819929')

# as referenced above, I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_sl, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# saving the figure in the boxplot outputs named sepal_length_range
plt.savefig('boxplot_outputs/sepal_length_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region SW Boxplot
# Setting the Sepal Width Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py
# Source: fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html

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

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this(https://matplotlib.org/stable/gallery/statistics/boxplot.html)
# Source: linestyle - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
medianprops = dict(linewidth = 3, color = '#819929')

# as referenced above, I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_sw, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# saving the figure in the boxplot outputs named sepal_width_range
plt.savefig('boxplot_outputs/sepal_width_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion 

# region PL Boxplot

# Setting the Petal Length Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py
# Source: fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html

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

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this(https://matplotlib.org/stable/gallery/statistics/boxplot.html)
# Source: linestyle - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
medianprops = dict(linewidth = 3, color = '#819929')

# as referenced above, I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_pl, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# saving the figure in the boxplot outputs named petal_length_range
plt.savefig('boxplot_outputs/petal_length_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region PW Boxplot

# Setting the Petal Width Boxplot
# I initially attempted to plot the min to max range using a scatterplot then a histogram but no joy. A box plot makes more sense to show the range (mix -> max) and the median

# This example on matplotlib was very useful, especially in adding in the axis labels and setting colours https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py
# Source: fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html

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

# I wanted to change the colour and style of the median line point, used the matplotlib boxplot documentation for this(https://matplotlib.org/stable/gallery/statistics/boxplot.html)
# Source: linestyle - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
medianprops = dict(linewidth = 3, color = '#819929')

# as referenced above, I learned the below method for assigning colours on the matplotlib gallery
bplot = ax.boxplot(all_pw, tick_labels = labels, patch_artist=True, medianprops=medianprops);

# assigning the colour to the boxplot
for patch, color in zip(bplot['boxes'], colours):
    patch.set_facecolor(color)

# saving the figure in the boxplot outputs named petal_width_range
plt.savefig('boxplot_outputs/petal_width_range')

# closing the plot to ensure it does not continue into other plots
plt.close()

#endregion

# region SW v SL Scatterplot

# Sepal Width Length vs Sepal Width for each species

# I tried to do this scatterplot many ways: selecting all rows and just the sepal width or sepal length column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.

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
# Source: https://pythonexamples.org/matplotlib-scatter-plot-color/
# Source: https://matplotlib.org/stable/api/markers_api.html
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

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/sepal_length_v_sepal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region PW v PL Scatterplot

# Petal Width Length vs petal Width for each species

# I tried to do this scatterplot many ways: selecting all rows and just the petal width or petal length column etc. In the end, I found a great source that solved my colour issue(I had trouble assigning colours I chose to the variables) and also helped to breakdown the data.

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
# Source: https://pythonexamples.org/matplotlib-scatter-plot-color/
# Source: https://matplotlib.org/stable/api/markers_api.html
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

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
# Saving the figure in the scatterplot outputs folder
plt.savefig('scatterplot_outputs/petal_length_v_petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# ---------- Creating histograms for individual features ----------

#region SL Histograms

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
plt.hist(sepal_length, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region SW Histograms

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
plt.hist(sepal_width, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PL Histograms

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
plt.hist(petal_length, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_length', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

#region PL Histograms
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
plt.hist(petal_width, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_width', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion

# region SL Species Hist

# ---------- Creating histograms for individual features by species ----------

# Source: DataCamp, Intermediate Python, Chapter Matplotlib(https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)

# Attempting to plot three bars on one histogram - I originally attempted to do this with the pd_iris_data but then thought because the species name was a string not a float, I could not create the array I needed to plot all three on the one! It turned out I did not need to create a numpy array at all and ended up not using that dataset for this.
# Source: https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html
# Source: https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries
# Source: https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it

# ---------- Sepal Length ----------

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

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
plt.hist(species_sl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

# region SW Species Hist

# ---------- Sepal Width ----------

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

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
plt.hist(species_sw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/sepal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PL Species Hist
# ---------- Petal Length ----------

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

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
plt.hist(species_pl, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_length_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion 

#region PW Species Hist

# ---------- Petal width ----------

# to show the legend, this needs to be brought in as a sub plot
fig, ax = plt.subplots()
 
# Setting the legend styles for each variable
setosa = mpatches.Patch(facecolor = '#7c70cb', edgecolor = 'black', label = 'Setosa')
versicolor = mpatches.Patch(facecolor = '#632AC5', edgecolor = 'black', label = 'Versicolor')
virginica = mpatches.Patch(facecolor = '#B9B0E7', edgecolor = 'black', label = 'Virginica')

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
plt.hist(species_pw, bins = 10, edgecolor = 'black', color = colours)

# Source: https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/
plt.savefig('histogram_outputs/petal_width_species_comparison', bbox_inches = 'tight')

# ensures the plot is closed when running off the next plot so it does not go onto the graph
plt.close()

#endregion