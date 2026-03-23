# RAiDER / PyAPS / GACOS ARIA Example Tutorial

This tutorial package provides:

- `Compare_RAiDER_PyAPS_GACOS.ipynb`, a notebook that compares the output of RAiDER, PyAPS, and GACOS.
- `run_raider_example.py` (dataset validator + launch helper)

## Quick start
1. Download and extract the data files from https://osf.io/ygm3f/files/osfstorage. 

2. Validate dataset presence:

```bash
python3 run_raider_example.py
```

3. Run the notebook:

```bash
jupyter notebook Compare_RAiDER_PyAPS_GACOS.ipynb
```

## Dependencies

- Python 3.8+
- numpy
- xarray
- netCDF4
- matplotlib
- cartopy
- rasterio
- scipy
- pyaps3 (Required to be able to run the PyAPS example)

