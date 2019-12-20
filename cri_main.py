# Plotting
import matplotlib   # For advanced plotting
import matplotlib.pyplot as plt # (subpackage has to be imported explicitly)

# Data Science
import numpy as np
import pandas as pd

# File Handling
import os   # For I/O and path handling
import os.path  # For walking through directories

# Colour Science
import colour
import colour.plotting
import luxpy

# Plotting
from matplotlib import pyplot as plt

# =====================================================================
# =====================================================================
# SPD to CRI Script
# Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================
# =====================================================================


# Read input folder and list all relevant files
# =====================================================================

cwd = os.getcwd()
intestpath = '/data/input/test/'
inpath = '/data/input/'
outpath = '/data/output/'

# File input
# =====================================================================

csvdict = {}

for dirpath, dirname, filenames in os.walk(cwd+intestpath):

    for file in filenames:

        # Skips hidden files like ".DStore"
        if file[0][0] == '.':
            continue

        print(file)

        try:
            # Reads all files in the input folder
            dataframe = pd.read_csv(cwd+intestpath+file,
                                    header=None,
                                    names=['wavelength', 'intensity'])

            # Replaces negative avlues with 0
            dataframe[dataframe < 0] = 0

            # Sorts values by wavelength overwriting the dataframe
            pd.DataFrame.sort_values(dataframe,
                                     by='wavelength',
                                     inplace=True)

            # Resets the index, just in case
            pd.DataFrame.reset_index(dataframe,
                                     drop=True,
                                     inplace=True)


        except TypeError:
            print('Error reading file >>', file, '<<. Moving on.'), print()
            continue

        # Appends dataframe to a dictionary
        csvdict.update({file: dataframe})

# File postprocessing
# =====================================================================

# Checks for discontinuities in the SPD and shifts all values towards x-axis if required
for key in csvdict:
    y_beg = csvdict[key]['intensity'].iloc[0]
    y_end = csvdict[key]['intensity'].iloc[-1]
    y_max = pd.DataFrame.max(csvdict[key]['intensity'])

    beg_diff = ( y_beg / ( y_max / 100 ) )
    end_diff = ( y_end / ( y_max / 100 ) )

    if (beg_diff or end_diff) < 0.75:
        print('File >>', key, '<< discontinuity at start and end of values:')
        print('y_start=', y_beg, 'y_difference_start=', beg_diff, '%')
        print('y_end=', y_end, 'y_difference_end=', end_diff, '%'), print()
    else:
        print('Warning: Large discontinuity! Shifting values towards x-axis.')
        if y_beg < y_end:
            csvdict[key]['intensity'] = csvdict[key]['intensity'].apply(lambda y: y - y_beg)
        if y_beg > y_end:
            csvdict[key]['intensity'] = csvdict[key]['intensity'].apply(lambda y: y - y_end)

# CRI calculation with LuxPy package
# =====================================================================

cridict = {}

for key in csvdict:
    spd = np.ndarray.transpose( csvdict[key].to_numpy() )
    cri = luxpy.color.cri.spd_to_cri(spd)
    print('LuxPy calculations:')
    print('CRI=', cri[0][0], 'for', key)
    cridict[key] = cri[0][0]

print(cridict)

# CRI calculation with colour-science package
# =====================================================================

altcridict = {}

for key in csvdict:
    spd_dict = dict(zip(csvdict[key]['wavelength'], csvdict[key]['intensity']))
    spd = colour.SpectralDistribution(spd_dict)
    cri = colour.colour_rendering_index(spd)
    print('Colour calculations:')
    print('CRI=', cri, 'for', key)
    altcridict[key] = cri

print(cridict)
