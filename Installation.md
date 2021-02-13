## 1. Download and Installation 
### Installing Anaconda or Miniconda
RAiDER was designed to work with __[Conda](https://docs.conda.io/en/latest/index.html)__ a cross-platform way to use Python that allows you to setup and use "virtual environments." These can help to keep dependencies for different sets of code separate. Conda is distrubed as __[Anaconda](https://www.anaconda.com/products/individual)__ or __[Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda)__, a light-weight version of Anaconda. See __[here](https://docs.anaconda.com/anaconda/install/)__ for help installing Anaconda and __[here](https://docs.conda.io/en/latest/miniconda.html)__ for installing Miniconda. 

### Requirements for running RAiDER
RAiDER currently works on \*nix systems, and has been tested on the following systems:
- Ubuntu v.16 and up
- Mac OS v.10 and up

### Installing RAiDER using conda
1. First, __[download the source code](https://github.com/dbekaert/RAiDER/archive/dev.zip)__ for RAiDER and unzip to the location where you want to keep the code, or __[clone to the repository](https://github.com/dbekaert/RAiDER)__ to your system.  
2. On a terminal, change to the source code directory and create a new conda environment using ```conda env create -f environment.yml```
3. Activate the new conda environment using ```conda activate RAiDER```
4. From inside the main source code directory, type ```python setup.py install```
5. Finally, test the new installation: ```py.test test/```

### Installing RAiDER without conda
- To be completed
