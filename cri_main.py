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
inpath = '/data/input/'
outpath = '/data/output/'

csvdict = {}

for dirpath, dirname, filenames in os.walk(cwd+inpath):

    for file in filenames:

        # Skips hidden files like ".DStore"
        if file[0][0] == '.':
            continue

        print(file)

        try:
            # Reads all files in the input folder
            dataframe = pd.read_csv(cwd+inpath+file,
                                    header=None,
                                    names=['wavelength', 'intensity'])

            # Replaces negative avlues with 0
            dataframe[dataframe < 0] = 0

            # Sorts values by wavelength overwriting the dataframe
            pd.DataFrame.sort_values(dataframe,
                                     by='wavelength',
                                     inplace=True)

        except TypeError:
            print('Error reading file >>', file, '<<. Moving on.'), print()
            continue

        # Appends dataframe to a dictionary
        csvdict.update({file: dataframe})


# CRI calculation with LuxPy package
# =====================================================================


'''
cridict = {}

for key in csvdict:
    spd = np.ndarray.transpose( csvdict[key].to_numpy() )
    cri = luxpy.color.cri.spd_to_cri(spd)
    print('CRI=', cri[0][0], 'for', key)
#    cridict[key] = luxpy.color.cri.spd_to_cri(spd)

#print(cridict)



def wavelength_extender(array):
    wl_start = 400
    wl_end = 800

    wl_max = int(np.amax(array[0,:],axis=None))
    wl_min = int(np.amin(array[0,:],axis=None))


    for i in range(wl_end - wl_max):
        array = np.append(array, [i+wl_max, 0], axis=0)
        
'''

# CRI calculation with colour-science package
# =====================================================================

spd_dict = dict(zip(spd_dataframe['wavelength'],spd_dataframe['intensity']))

spd = colour.SpectralDistribution(spd_dict)
cri = colour.colour_rendering_index(spd)
