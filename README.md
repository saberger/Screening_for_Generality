<div align="justify">

# Screening_for_Generality

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Citation](#citation)
- [License](#license)

If you have questions, please feel free to message me on Github or per mail: [sarah.berger@uni-graz.at](sarah.berger@uni-graz.at)

## Introduction
This is a brief introduction to the project.
The use of **python 3.7** is recommended, since it seems there is a bug in heatmap labeling with the newest version of matplotlib.

## Installation
To install the project, follow these steps:\
(0. If you are on Windows, install [Anaconda](https://www.anaconda.com/download/success)), open the Anaconda Powershell and run `conda init powershell`.
1. Clone the repository: \
`git clone https://github.com/saberger/Screening_for_Generality`
2. Install the dependencies by setting up a conda environment with necessary packages by:\
`conda env create -f environment.yml`\
The setup might take some time (approx. 0.5-1 h). Finally you can start the environment with\
`conda activate screening_environment`.\
If you open the powershell for the first time, and there is written (base) on the beginning of your prompt, you first need to deactive the base environment by `conda deactivate base`.
Alternatively, you can also create your own conda environment and install the packages manually, this should work much faster. You can follow this steps:
```
conda create -n screening_environment python=3.7

pip install matplotlib numpy pandas seaborn openpyxl pdfplumber jupyterlab
```

## Usage
See on the individual README files in the subfolders.
You can run within the jupyter folder\
`python -m jupyterlab`\
to enter the jupyter environment if you are more familiar with jupyter.

## Citation
Insert bibtex here

## License
[MIT](./LICENSE)
</p>
