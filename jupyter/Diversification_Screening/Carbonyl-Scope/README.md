<div align="justify">

# Diversification Screening
## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)

## Introduction
This is a brief introduction of the project. For the carbonyl scope screening, small scale biotransformations were analyzed with Flow Injection Analysis (FIA), compare our publication on this topic [paper on FIA-MS](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cbic.202300170).\
To make this script more user friedly it was rewritten with github copilot in bash.

## Usage
### Rename the experiment folder
The Agilent HPLC prints the experiment with spaces in the filename, which could potentially lead to errors in script based processing. Therefore rename the folder and all the subfolders and filesnames whereby all spaces will be replaced by _ with:\
`python removespace.py`\
This will process all folders in the current working directory.
### Extract the SIM-Areas of each sample to a table
Now you can extract the SIMs with the following script:
`python extract-data.py $yourfilename`\
With this, you can automate the process and also loop over multiple experiments with, e.g.

```
for dir in .*/ ; do 
python extract-data.py $dir; done
```
Finally you can transfere the SIMs of interesst in your template sheet, see the example here.

## Heatmap generation
To start the combination of individual template sheets, you should have all of them in one folder. \
Generate a new folder, called "output" in the folder where all of the template sheets are stored.\
The script **summary-hits-only-carbonyl-scope.py** should be copied also in that folder.

After running the script\
`python summary-hits-only-carbonyl-scope.py`

Two new files will appear in the output folder:
* alldata_carbonyl.xlsx (as it says, all data, even the substrate combinations with no hit)
* matrix-hits-only.xlsx (combinations removed with no activity and also combinations that were not evaluable)

With the script\
`python get-matrix.py`\
you can extract how many hits per substrate combination were generated.
It will ask you for a user input:\
**Enter the file path:** 
were should enter the file path of your *matrix-hits-only.xlsx* file.
In order to obtain a heatmap out of it, you must first sort this data according to your plate layout.
So instead of a single column, you should end up with a text file of 8x12 dimension (you can sort the data in excel and copy the table to a editor file).
You can paste the output of the matix.csv file in the A and B column of the `give-matrix-heatmap.ods` file, but copy only the table without labels to a text file.

You can generate the heatmap then with\
`python heatmap.py`\
It will ask you for a user input\
**Please enter the filepath for the matrix file:**\
were you should enter the filepath of your generated **matrix.txt** file.
</p>