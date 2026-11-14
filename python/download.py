"""Fetches the state-wide source layers from Data.SA into ../raw/ (about 1.2 GB): Land Use Generalised for 2015 to 2025
and Land Division Applications, both from the Department for Housing and Urban Development (CC BY).
    python download.py [years...]      e.g. python download.py 2018 2025"""
import os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, '..', 'raw'); os.makedirs(RAW, exist_ok=True)
years = [int(y) for y in sys.argv[1:]] or list(range(2015, 2026))
files = [(f'LandUseGeneralised{y}_shp.zip', f'https://www.dptiapps.com.au/dataportal/LandUseGeneralised{y}_shp.zip') for y in years]
files.append(('LandDivisionApplications_shp.zip', 'https://www.dptiapps.com.au/dataportal/LandDivisionApplications_shp.zip'))
for name, url in files:
    out = os.path.join(RAW, name)
    if os.path.exists(out): print('have', name); continue
    print('fetching', name); urllib.request.urlretrieve(url, out)
