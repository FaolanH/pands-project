# pands-project
# Author: Faolán Hamilton
# Project for the Programming and Scripting module

## Interacting with this project
### Welcome to this repository!  In this project I will look at what is possible through Python for Data Analytics using a well-known dataset in the coding community: the Iris dataset. Through a mixture of methods I will look at different ways of exploring the data visually and what the results can be used to demonstrate. While it is a specific dataset being analysed, the methods used throughout are applicable with other datasets.

### This project uses a python script to run through the code, which then outputs the results of the analysis into several separate pngs and a txt file. To see how this script runs and recreate the outputs seen in this repository, I would recommend one of two options: opening codespaces on this repository by clicking the green <> Code button to the top right of the repository and creating a codespace to run the code in. The other option would be opening this on VSCode to easily flick between the different sections of the code; to do this please navigate to the download section through the three dots to the top right of the analysis.py file and open file in VSCode. Please note there will be no output in the terminal (other than a message guiding you to the output folders and txt file).

![image](https://github.com/user-attachments/assets/df0b916a-1b4c-4c10-ad7d-6f9fbd4714eb)

## Python Script
### The following is a breakdown of my python script:
#### A section for importing all the packages I need to run the code
##### - Numpy
##### - Pandas
##### - Matplotlib
##### - Seaborn
##### - sklearn.datasets
##### - Matplotlib.patches
##### - Matplotlib.colors
##### For more details on these packages, you can view documentation in the references section below.
#### Importing in the two versions of the iris dataset
##### I used the pandas DataFrame for the vast majority of the work in this notebook, the only instance where I used the load.iris() package (from sklearn.dataset) is for the heatmap
#### Creating a summary txt file 
##### Initially, I set all the analysis by calling on the data location and using numpy functions (np.mean, np.median, np.min, np.max, np.std). I did this for the dataset as a whole for each feature and then for each feature by species. I then created a summary DataFrame with all this information to display it neatly in the txt. file (which is output separately in the repository as features_file.txt)
#### Setting the features
##### In this section I set the features and species into variable that are used throughout the notebook. 
#### Boxplots
##### With the modules imported and the data set, in this section I began plotting the data onto boxplots. Here, it was a comparison of the three species and the overall dataset for each feature, with four boxplots saved into the boxplot_outputs folder. This is an important plot to visualize the minimum, maximum and median figure for each feature, which visualizes the data described in the features_file.txt
#### Scatterplots
##### For the scatterplots, I showed the comparison between the sepal width and sepal length, sepal width and petal width, petal width and petal length and sepal length and petal length. I think this mixture of analysis and point plotting is interesting in seeing where the different species lie, with clear overlap for some features and distance in others. The outputs of this are saved in the scatterplot folder
#### Histograms
##### I used histograms to compare species features across the species and features as a whole. These are useful plots to see the data in a bar format, to compare bins and show how many samples fit into each range. There are eight histogram plots in the histograms outputs folder.
#### Heatmap
##### I created a heatmap of the entire iris data set, which used the iris.data format as they did not accept the string format used for the species in the pd_iris_data. This heatmap displays each row of data and shows the correlations between the features. This can be viewed in the heatmap_outputs folder
#### Pairplot
##### I created a pairplot of the features using seaborn, which outputs 16 plots comparing the three species across the features. It is very useful to see them side by side for visual comparison. This can be viewed in the pairplot_outputs section
#### References
##### The final section of this script is the references section. Throughout the notebook, there are comments with the Source number and title to find where the structure/data came from. This is also available to view in the references section at the bottom of this README

## Iris Dataset
The Fisher's Iris dataset contains 150 rows and 4 columns of data, looking at 150 samples taken from three species of iris: setosa, versicolor and virginica. These samples are measured by four features: sepal width, sepal length, petal width and petal length. There is some interesting context on the background for this dataset and possible uses (Source: L) Iris Dataset Info)
To see the actual data in the iris dataset, please see the iris_data_folder for more details (Source: M) Iris Dataset Literal

### Below is a diagram of the components of the Iris flower. When the data refers to "sepal", "petal", it can be hard to visualize what it is that I am discussing. The imagery shows the differences between the three species used in this dataset. 

#### Source: A)
![image](https://github.com/user-attachments/assets/137215fd-8540-4511-9c81-c5832036b93a)

## Project Plan
### This was the initial plan I set out when beginning this project, I will go through each statement and discuss it
#### - Describe the iris dataset briefly and how other data might have similar structure
#### - Investigate the different ways this data can be examined, in the simplest terms (inspiration from the Principles of Data Analytics module):
  ##### - mean, median, minimum, maximum, standard deviation
  ###### - This analysis can be viewed in the features_file which is a summary of the four main features and three species
  ##### - plotting the data on histograms/boxplots, comparing the species or across one specific species e.g. comparing petal length across setosa, versicolor and virginica or showing the range of petal length (min to max) in one species
  ###### - This analysis can be viewed in the various output folders seen in this repository (histogram_outputs, boxplot_outputs, scatterplot_outputs, heatmap_outputs and pairplot_outputs). 
  ##### - what libraries are available to help me display this data?
  ###### - As listed in the references section, I used a series of libraries and packages to help me visualize this data: numpy, pandas, matplotlib, seaborn and sklearn.dataset
  ##### - can I use user input to ask the user what they want to see?
  ###### - Unfortunately, I did not get to investigate this element of the project, which would be interesting to consider for future projects
  ##### - investigate the pandas read.csv to see what can be done
  ###### - I used this dataset throughout the notebook and found it very useful particularly as the species name was within this dataset.

##### The iris dataset has been added into this repository, including the raw data, description of the data and index. 

## Colours used in the Project
### The colours used in the plots throughout the project are based on the colours of the iris flowers. 

### Palette:
#### Source: B)
![Iris_dataset_colour_scheme](https://github.com/user-attachments/assets/36592a7e-b26e-41f6-a237-a9777c61331f)

### Used ColorPicker to select hex codes from the images, source: https://imagecolorpicker.com/

### Setosa Iris flower 

### HEX Code: #7c70cb

![image](https://github.com/user-attachments/assets/d3e3c930-7059-42c1-af2b-e03d8d0e1163)

Source: C)

![image](https://github.com/user-attachments/assets/5e2f8236-cfd0-4034-82c7-0cb690a0d25f)

Source: D)

### Versicolor Iris flower

### HEX Code: #632AC5

![image](https://github.com/user-attachments/assets/7cffb87a-1080-4349-9b9f-900cd7503ef1)

Source: E)

![image](https://github.com/user-attachments/assets/04d05e00-ef6a-431f-aded-34aa7e08afc0)

Source: F)

### Virginica Iris flower

### HEX Code: #B9B0E7

![image](https://github.com/user-attachments/assets/7446098c-ba03-463e-898f-3eb8b3147860)

Source: G)

![image](https://github.com/user-attachments/assets/c6e69ab4-3b81-465d-87dd-dec4c6019040)

Source: H)

### Yellow signal (accent colour)

### HEX Code: #E1AD01

![image](https://github.com/user-attachments/assets/c1715073-de4f-4630-89a3-445396ed3350)

Source: I)

![image](https://github.com/user-attachments/assets/4a8de5db-dab1-4530-ad92-6a3d74e2f1f7)

Source: J)

### Green stem (accent colour)

### HEX Code: #819929

![image](https://github.com/user-attachments/assets/8789636a-63ac-41e8-8282-a0a370403653)

Source: K)

## Further Research:
#### This project is intended to be an introduction into the iris dataset, the functionalities of python and how to display data in interesting ways. Below I have listed some other resources which discuss other ways the data can be displayed, such as Three Dimensional plots and mapping scatterplot sections in colours

3D plot: (https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)
GPC plot: (https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)
Pairplot, including some key summary figures: (https://www.researchgate.net/figure/Distributions-and-correlations-for-numeric-variables-in-iris-petal-length-cm-petal_fig2_362573623)

## References:

### In this README:
#### A) Sepal and Petal Lengths and Widths Diagram: MachineLearning4ya (https://machinelearning4ya.blogspot.com/2022/04/iris-flowers-classification-using.html)
#### B) Colour Palette Generator: Colorkit (https://colorkit.co/color-palette-generator/B9B0E7-7c70cb-632AC5-E1AD01-819929/)
#### C) Setosa Hex Code: Colorhexa (https://www.colorhexa.com/7c70cb)
#### D) Setosa Reference Photo: Gardenia (https://www.gardenia.net/plant/iris-setosa)
#### E) Versicolor Hex Code: Colorhexa (https://www.colorhexa.com/632ac5)
#### F) Versicolor Reference Photo: Gardenia (https://www.gardenia.net/plant/iris-versicolor)
#### G) Virginica Hex Code: Colorhexa (https://www.colorhexa.com/b9b0e7)
#### H) Virginica Reference Photo: Gardenia (https://www.gardenia.net/plant/iris-virginica-var-shrevei)
#### I) Signal identification: FS.USDA.GOV (https://www.fs.usda.gov/wildflowers/beauty/iris/flower.shtml)
#### J) Signal Yellow Hex Code: Colorhexa (https://www.colorhexa.com/e1ad01)
#### K) Stem Green Hex Code: Colorhexa (https://www.colorhexa.com/819929)
#### L) Iris Dataset Info: GeeksforGeeks (https://www.geeksforgeeks.org/iris-dataset/)
#### M) Iris Dataset Literal: UC Irvine Machine Learning Repository (Source: https://archive.ics.uci.edu/dataset/53/iris)

### Documentation for packages used:

#### 0.1) Numpy - https://numpy.org/doc/
#### 0.2) Pandas - https://pandas.pydata.org/docs/
#### 0.3) Matplotlib - https://matplotlib.org/stable/index.html
#### 0.4) Seaborn - https://seaborn.pydata.org/
#### 0.5) Sklearn.datasets, load.iris() - https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
#### 0.6) Matplotlib, m.patches - https://matplotlib.org/stable/api/patches_api.html
#### 0.7) Matplotlib, ListedColorMap - https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html

### In analysis.py:

#### 1) Setting regions: Stack overflow (https://stackoverflow.com/questions/8265583/dividing-python-module-into-multiple-regions)
#### 2) Iris dataset: GitHub (https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv)
#### 3) Creating txt file: W3 Schools (https://w3schools.tech/tutorial/python/python_write_to_file)
#### 4) np Mean: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
#### 5) np Median: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.median.html)
#### 6) np Min: Numpy (https://numpy.org/doc/stable//reference/generated/numpy.min.html)
#### 7) np Max: Numpy (https://numpy.org/doc/stable//reference/generated/numpy.max.html)
#### 8) np Std Dev: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.std.html)
#### 9) pdDataFrame: GeeksforGeeks (https://www.geeksforgeeks.org/how-to-make-a-table-in-python/####using-prettytable)
#### 10) dfround: Stack overflow (https://stackoverflow.com/questions/38255796/pandas-round-is-not-working-for-dataframe)
#### 11) Standard Deviation definition: GeeksforGeeks(https://www.geeksforgeeks.org/standard-deviation-formula/)
#### 12) loc and iloc: DataCamp (https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17)
#### 13) no background output text: Stack overflow (https://stackoverflow.com/questions/74696163/how-to-remove-name-and-dtype-from-output-code)
#### 14) Plot Additions: DataCamp (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)
#### 15) Boxplot label and colour: (Matplotlib (https://matplotlib.org/stable/gallery/statistics/boxplot_color.html####sphx-glr-gallery-statistics-boxplot-color-py)
#### 16) Fig size: How2Matplotlib (fig size: https://how2matplotlib.com/matplotlib-boxplot-x-axis-label.html)
#### 17) Linepoint: Matplotlib (https://matplotlib.org/stable/gallery/statistics/boxplot.html)
#### 18) Setting scatterplot colour: Python Examples (https://pythonexamples.org/matplotlib-scatter-plot-color/)
#### 19) Markers: Matplotlib (https://matplotlib.org/stable/api/markers_api.html)
#### 20) Saving figures: Stack overflow (https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it)
#### 21) Forward Slash when saving figure: DNM (https://dnmtechs.com/fixing-deprecationwarning-invalid-escape-sequence-in-python-3/)
#### 22) Setting the edgecolour: Matplotlib (https://matplotlib.org/stable/api/figure_api.html)
#### 23) Chapter Matplotlib: DataCamp (https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=1)
#### 24) Assigning hist colours: Matplotlib (https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)
#### 25) Legend Styling: Matplotlib (https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries)
#### 26) patches: Matplotlib (https://matplotlib.org/stable/api/patches_api.html)
#### 27) ListedColorMap: Matplotlib (https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html)
#### 28) Tutorial Colormaps: DataCamp (https://www.datacamp.com/tutorial/matplotlib-colormaps)
#### 29) colors.Colormap: GeeksforGeeks (https://www.geeksforgeeks.org/matplotlib-colors-colormap-class-in-python/)
#### 30) Pairplot: GeeksforGeeks (https://www.geeksforgeeks.org/python-seaborn-pairplot-method/)
#### 31) Numpy Coefficient: Numpy (https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
