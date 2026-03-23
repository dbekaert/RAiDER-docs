#!/usr/bin/env python3
"""Validate and run RAiDER example data set."""
from pathlib import Path
import subprocess
import sys

required_files = [
    Path('dem.tif'),
    Path('products/S1-GUNW-A-R-064-tops-20250912_20250819-014931-00119W_00033N-PP-6a98-v3_0_1.nc'),
    Path('products/S1-GUNW-A-R-064-tops-20250912_20250831-014931-00119W_00033N-PP-e54e-v3_0_1.nc'),
    Path('products/S1-GUNW-A-R-064-tops-20250912_20250906-014931-00119W_00033N-PP-9580-v3_0_1.nc'),
    Path('GACOS/20250819.ztd.tif'),
    Path('GACOS/20250831.ztd.tif'),
    Path('GACOS/20250906.ztd.tif'),
    Path('GACOS/20250912.ztd.tif')
]

missing = [f for f in required_files if not f.exists()]
if missing:
    print('Missing required files:')
    for f in missing:
        print(' -', f)
    sys.exit(1)

print('All required files are present (OK).')

print('\nYou can run:')
print('  python3 Compare_RAiDER_PyAPS_GACOS.py')
print('  jupyter notebook Compare_RAiDER_PyAPS_GACOS_explicit.ipynb')

# Optional: run the script automatically
if '--run' in sys.argv:
    print('\nRunning Compare_RAiDER_PyAPS_GACOS.py...')
    try:
        subprocess.run(['python3', 'Compare_RAiDER_PyAPS_GACOS.py'], check=True)
    except subprocess.CalledProcessError as e:
        print('ERROR: script run failed:', e)
        sys.exit(e.returncode)
