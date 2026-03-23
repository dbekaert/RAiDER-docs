# RAiDER / PyAPS / GACOS ARIA Example Tutorial

This tutorial package provides:

- `Compare_RAiDER_PyAPS_GACOS.py` (original script)
- `Compare_RAiDER_PyAPS_GACOS.ipynb` (notebook wrapper, `%run` style)
- `Compare_RAiDER_PyAPS_GACOS_explicit.ipynb` (full explicit function/workflow notebook)
- `raider_doc_example_data.zip` (data bundle)
- `run_raider_example.py` (dataset validator + launch helper)

## Quick start

1. Extract data (if not already extracted):

```bash
unzip raider_doc_example_data.zip
```

2. Validate dataset presence:

```bash
python3 run_raider_example.py
```

3. Run in notebook (recommended):

```bash
jupyter notebook Compare_RAiDER_PyAPS_GACOS_explicit.ipynb
```

4. Optional: run script directly:

```bash
python3 Compare_RAiDER_PyAPS_GACOS.py
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
- pyaps3 (optional)

## Data hosting recommendation

The bundle is 1.5GB, so avoid storing as raw git history:

- Use GitHub Releases (attach ZIP)
- Use Git LFS (if needed)
- Use cloud storage (e.g., S3, GCS, Azure Blob, Zenodo) and link in README
