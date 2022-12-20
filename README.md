# **R**aytracing **A**tmospher**i**c **D**elay **E**stimator for **R**ADAR - RAiDER

[RAiDER](https://github.com/dbekaert/RAiDER) is a package in Python which contains tools to calculate tropospheric corrections for Radar using a raytracing implementation. Its development was funded under the NASA Sea-level Change Team (NSLCT) program, the Earth Surface and Interior (ESI) program, and the NISAR Science Team (NISAR-ST) (NTR-51433). U.S. Government sponsorship acknowledged.

Copyright (c) 2019-2022, California Institute of Technology ("Caltech"). All rights reserved.

THIS IS RESEARCH CODE PROVIDED TO YOU "AS IS" WITH NO WARRANTIES OF CORRECTNESS. USE AT YOUR OWN RISK.

## Getting Started

### Quick Start
To get started, run the following lines in a terminal: 
```
conda env create --name RAiDER  -c conda-forge raider jupyterlab
conda activate RAiDER
```
Then download or clone this repository to your working directory, and run
```
jupyter lab
``` 
navigate to one of the tutorial notebooks, and open it. 

[Other ways to install](Installation.md)  
[Defining Custom Weather Models](notebooks/Defining_Custom_Weather_Models/Defining_custom_Weather_Models_in_RAiDER.ipynb) 

## Tutorials 
[Pandas tutorial for GNSS delay manipulation](notebooks/Pandas_tutorial/Pandas_tutorial.ipynb)  
[RAiDER tutorial](notebooks/RAiDER_tutorial/RAiDER_tutorial.ipynb)  
[RAiDER library access in Python](notebooks/RAiDER_tutorial/RAiDER_Python_access.ipynb)
[Tutorial downloading GNSS tropospheric delays](notebooks/raiderDownloadGNSS/raiderDownloadGNSS_tutorial.ipynb)  
[raiderStats tutorial](notebooks/raiderStats/raiderStats_tutorial.ipynb)  
