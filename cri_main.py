import numpy as np

# Subpackages have to be imported explicitly
import scipy
import scipy.interpolate as interpolate

import math

import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import os
import pathlib
from pathlib import Path

import csv

# Subpackages have to be imported explicitly
import colour
import colour.plotting

# =====================================================================
# SPD to CRI Script
# (C) Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================

# Get correct file paths for import and export
# ============================================
currentpath = os.path.dirname(os.path.abspath(__file__))
input_subfolder = "Data/Input/spd_in.csv"
inputpath = os.path.join(currentpath, input_subfolder)
print(inputpath)

# SPD data import from csv file
# =============================

try:
    fin = open(inputpath, 'r')
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
# Note that the colour science module employs its own interpolation of data points
# ================================

# Initialize empty data types
spd_dict_raw = dict()
X = list()
Y = list()

# Fill empty data types
for row in csvreader:
#    print('x=', row[0])
#    print('y=', row[1])
    X.append(row[0])
    Y.append(row[1])
fin.seek(0)

# Sort lists, just in case
X.sort()
Y.sort()

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