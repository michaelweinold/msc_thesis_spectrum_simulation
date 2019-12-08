# PACKAGES
# =====================================================================

# Plotting
# =====================================================================
import matplotlib # For advanced plotting
import matplotlib.pyplot as plt # (subpackage has to be imported explicitly)
import tikzplotlib # For export of figures to LaTeX pgfplot

# Data Science
# =====================================================================
import math
import numpy as np
import pandas as pd
import scipy
import scipy.interpolate as interpolate # (subpackage has to be imported explicitly)

# File Handling
# =====================================================================
import os # For I/O and path handling
import pathlib # For advanced path handling
import csv # For CSV file import and manipulation

# Colour Science
# =====================================================================
import colour
import colour.plotting # (subpackage has to be imported explicitly)

# =====================================================================
# =====================================================================
# SPD to CRI Script
# Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================
# =====================================================================

# Get correct file paths for import and export
# ============================================
indir = os.path.join(os.getcwd(), "data/input")
infile = os.path.join(indir, "/spd_in.csv")
print('Attempting to read CSV file from path:', infile)

# SPD data import from csv file
# =============================

try:
    fin = open(infile, 'r')
except:
    print('CSV file could not be opened.')
else:
    print('CSV file opened.')
finally:
    print('Opening attempt complete.')

# Set custom CSV dialect
csv.register_dialect('WebPlotDigitizer-4.2',
                     delimiter = ',',
                     skipinitialspace=True)

# Attempt to determine the correct csv dialect
# Note that reading less than the entire file may lead to incorrect dialect detection.
try:
    autodialect = csv.Sniffer().sniff(fin.read()) # Reads entire file to determine csv dialect.
    fin.seek(0) # Resets the file's object position to the beginning
    print('CSV-file dialect successfully detected.')
except:
    autodialect = 'WebPlotDigitizer-4.2'
    print('CSV-file dialect detection failed. Falling back to custom >>WebPlotDigitizer-4.2<< dialect.')
finally:
    csvreader = csv.reader(fin, dialect=autodialect, quoting=csv.QUOTE_NONNUMERIC)
    print('CSV detection and reading attempt complete.')
#    for i in csvreader:
#        print(i)
    if(len(list(csvreader))==0):
        print('Warning: csv.reader produces no output!')
    fin.seek(0)

# Get spline and new x-axis points
# ================================

# Reads csv data to dictionary
spd_raw = {row[0]: row[1] for row in csvreader}
fin.seek(0)

#Set new x-axis points
x_max = X[-1]
x_min = X[0]
step_size = 1

x_start = int( math.ceil(x_min) )
x_stop = int( math.floor(x_max) )

#print('x_min=', x_min, 'x_max=', x_max)
#print('x_start=', x_start, 'x_stop=', x_stop)

X_new = list()
for i in range(x_start, x_stop):
    X_new.append(i)

# Calculate spline from original data points
#spd_spline = interpolate.splrep(X, Y)
#spd_ndarray_new = interpolate.splev(X_new, spd_spline)

# Transfer data to pandas DataFrame
# =================================
wavelength = list()
intensity = list()

try:
    for row in csvreader:
        wavelength.append(row[0])
        intensity.append(row[1])
except:
    print('Error in csv.reader output. Check CSV dialect detection or CSV file for anomalies.')
finally:
    fin.seek(0)

spd_dataframe = pd.DataFrame({'wavelength': wavelength, 'intensity': intensity})
print('Spectral Power Distribution extracted from CSV file: \n', spd_dataframe)

# Transfer data to dict
# =====================
spd_dict_new = dict()

try:
    for row in csvreader:
        spd_dict_new[row[0]] = row[1]
except:
    print('Error in csv.reader output. Check CSV dialect detection or CSV file for anomalies.')
finally:
    fin.seek(0)
    fin.close()

# Test colour science module and functions
# ========================================
#
# from sample_data import sample_spd_data
# sample_spd = colour.SpectralDistribution(sample_spd_data)
#
# colour.plotting.plot_single_sd(sample_spd)
#
# sample_cri = colour.colour_rendering_index(sample_spd)
# print('Sample CRI=', sample_cri)

# Perform colorimetric calculations
# =================================

spd = colour.SpectralDistribution(spd_dict_new)
colour.plotting.plot_single_sd(spd)
cri = colour.colour_rendering_index(spd)
print('Calculated CRI from SPD=', cri)

# Output
# ======

#fout = open('cri_data.csv', 'w')
#fieldnames = ['year', 'product', 'cri']
#csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)