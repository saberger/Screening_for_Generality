<div align="justify">

# Initial Screening
## Table of Contents
- [General](#general)
- [Heatmap](#heatmap)
- [Scatterplot](#scatterplot)


## General
The use of **python 3.7** is recommended, since it seems there is a bug in heatmap labeling with the newest version of matplotlib 

To start the combination of individual template sheets, you should have all of them in one folder. \
Generate a new folder, called "output" in the folder where all of the template sheets are stored.\
The script **sumarize-3D-hits-only.py** should be copied also in that folder.

After running the script\
`python summarize-3-SD-hits-only.py`

Two new files will appear in the output folder:
* alldata_3SD.xlsx (as it says, all data, even the substrate combinations with no hit)
* matrix3SD-hits-only.xlsx (combinations removed with no activity and also combinations that were not evaluable)

## Heatmap
With the script\
`python get-matrix.py`\
you can extract how many hits per substrate combination were.
It will ask you for a user input:\
**Enter the file path:** \
were should enter the file path of your `matrix3SD-hits-only.xlsx` file.
In order to obtain a heatmap out of it, you must first sort this data according to your plate layout.
So instead of a single column, you should end up with a text file of 8x12 dimension (you can sort the data in excel and copy the table to a editor file).
You can paste the output of the matix.csv file in the A and B column of the `give-matrix-heatmap.ods` file, but copy only the table without labels to a text file.

You can generate the heatmap then with\
`python heatmap.py`\
It will ask you for a user input\
**Please enter the filepath for the matrix file:**\
were you should enter the filepath of your generated **matrix.txt** file.

## Scatterplot
In order to obtain the scatterplot, with the maximum activity of an enzyme for its most active substrate combination, you have to edit the *matrix3SD-hits-only.xlsx* file with excel or libre office calculator.
* Add a new column, with the label "div"
* Sort the sheet first by Enzyme ID followed by Activity Mean
* then write the following formular in the div column: \
`=COUNTIF(A:A,A2)`
which will count how many substrate combinations a specific IRED can calatlyze
* in order to only show the most active substrate combination and remove the rest, to make the scatterplot, you have to filter the table, for that, write this in the last column
`=IF(A2=A3,"",1)`
this will write a 1 at the most active substrate combination and you can now filter the table and remove all other combinations
copy this to a knew excel sheet and you can generate the scatterplot with\
`python plot-data.py`
</p>