## script version of SyntheticTest.ipynb

import os, os.path as op
import numpy as np
import xarray as xr
from datetime import datetime
from RAiDER.llreader import BoundingBox
from RAiDER.losreader import Zenith, Conventional, Raytracing

from RAiDER.delay import tropo_delay

# ROOT = 'test/synthetic' # eventually for pytest
ROOT = '.'

def update_wm(wm_file):
    """ Edit the values in a weather model file 

    write it out with extension _SYNTH
    Return the file name for input into tropo_delay

    wet_total/hydro_total used for zenith/proj
    wet/hydro used for ray
    """

    with xr.open_dataset(wm_file) as ds:
        # edit t, p, e, wet, hydro, wet_total, hydro_total
        ds['wet_total']   = ('z y x'.split(), np.zeros_like(ds['wet_total']))
        ds['hydro_total'] = ('z y x'.split(), np.zeros_like(ds['hydro_total']))

    dst = f'{op.splitext(wm_file)[0]}_SYNTH.nc'
    ds.to_netcdf(dst)
    print ('Wrote synthetic weather model file to:', dst)
    return dst


def compare_golden(ext='ray'):
    """ Quick check if the synth result is different than real weather wm """
    ds_orig = xr.open_dataset(f'{ROOT}/golden_data/GMAO_tropo_20181113T230000_{ext}.nc')
    da_dry0 = ds_orig['hydro']
    ds_new  = xr.open_dataset(f'{ROOT}/Synthetic_tropo_20181113T110000_{ext}.nc')
    da_dry1 = ds_new['hydro']
    equal = np.allclose(da_dry0.data, da_dry1.data, equal_nan=True)
    print ('Orig == synthetic?', equal)
    return


# print ('Exiting')
# os.sys.exit()

dt = datetime(2018, 11, 13, 23)
wm0 = f'{ROOT}/weather_files/GMAO_2018_11_13_T23_00_00_36N_39N_78W_75W.nc'
wm  = update_wm(wm0)

height_levels = np.array([0., 100., 500., 1000.])
aoi = BoundingBox([36.8, 36.85, -76.15, -76.05])
aoi.add_buffer(buffer=1.)

orbit = f'{ROOT}/S1A_OPER_AUX_POEORB_OPOD_20181203T120749_V20181112T225942_20181114T005942.EOF'
# los = Zenith()

# los = Conventional(orbit)
los = Raytracing(orbit, time=dt)
ext = 'ray'

ds  = tropo_delay(dt, wm, aoi, los, height_levels, cube_spacing_m=5000)[0]

out = f'{ROOT}/Synthetic_tropo_20181113T110000_{ext}.nc'
ds.to_netcdf(out, mode="w")
print ('Wrote:', out)

compare_golden()

