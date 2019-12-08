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

infile = os.path.join(os.getcwd(), "data/input/spd_in.csv")
print('Attempting to read CSV file from path:', infile)

# SPD data import from csv file
# =============================

# Attempts to determine the correct csv dialect
def dialect_detector():
    try:
        autodialect = csv.Sniffer().sniff(fin.read())  # Reads entire file to determine csv dialect
        fin.seek(0)  # Resets the file's object position to the beginning
        print('CSV-file dialect successfully detected.')
    except:
        # Set custom CSV dialect
        csv.register_dialect('WebPlotDigitizer-4.2',
                             delimiter=',',
                             skipinitialspace=True)
        autodialect = 'WebPlotDigitizer-4.2'
        print('CSV-file dialect detection failed. Falling back to custom >>WebPlotDigitizer-4.2<< dialect.')
    return autodialect

# Checks if reader function is getting data
def guard_output():
    if (len(list(csvreader)) == 0):
        print('Warning: csv.reader produces no output!')
    else
        print('CSV detection and reading attempt complete.')
    finally
        fin.seek(0)

with open(infile, 'r') as fin:
    csvreader = csv.reader(fin, dialect=dialect_detector(), quoting=csv.QUOTE_NONNUMERIC)
    guard_output()
    spd_raw = {row[0]: row[1] for row in csvreader}

# Transfer data to pandas DataFrame
# =================================

spd_print = pd.DataFrame.from_dict(list(spd_raw.items()))
spd_print.columns = ['wavelength', 'intensity']
print('Spectral Power Distribution extracted from CSV file: \n', spd_print)



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

#spd = colour.SpectralDistribution(spd_dict_new)
#colour.plotting.plot_single_sd(spd)
#cri = colour.colour_rendering_index(spd)
#print('Calculated CRI from SPD=', cri)

# Output
# ======

#fout = open('cri_data.csv', 'w')
#fieldnames = ['year', 'product', 'cri']
#csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)