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

# Read input folder and list all relevant files
# =============================================

indir = os.path.join(os.getcwd(), "data/input")
inlist = os.listdir(indir)

print('Files in input directory:', inlist), print()

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
        print('CSV-file dialect detection failed, falling back to >> WebPlotDigitizer-4.2 << dialect')
    return autodialect

# Sets new x-axis data point intervall
#def intervall_finder(X_list, step_size):
#
#    x_min = X_list.min()
#    x_max = X_list.max()
#
#    #Convert float values to integers
#    x_start = int(math.ceil(x_min))
#    x_stop = int(math.floor(x_max))
#
#    print('x_min=', x_min, 'x_max=', x_max)
#    print('x_start=', x_start, 'x_stop=', x_stop)
#
#    X_new = list()
#    for i in range(x_start, x_stop):
#        X_new.append(i)
#
#    return X_new

# Calculates spline and outputs data according to new axis point intervall


#    # Tells the sorted function to sort by the x-values
#    def getkey (element):
#        return element[0]
#    sorted(zip(X,Y), key=getkey)

def spline_calculator(X, Y, X_spectrum):

    global spd_new

    spd_spline = interpolate.splrep(X, Y, k=3)
    spd_new = interpolate.splev(X_spectrum, spd_spline)


# Plots old vs new data points for visula inspection
#def spline_inspector():
#    plt.scatter()
#    plt.plot()

# Custom exceptions
# =================

class exception_csvreader(Exception):
    pass
class exception_cri_value(Exception):
    pass

# Main loop to read all CSV files
# =================================™

# Prepares empty dataframe with correct index
X_spectrum = [i for i in range(380, 740, 1)] # New x-axis points in the visible spectrum
output_master = pd.DataFrame(index=X_spectrum, columns=[infile])

for infile in inlist:

    print('Reading file: >>', infile, '<<')

    abs_infile = os.path.join(indir, infile)

    try:

        with open(abs_infile, 'r') as fin:

            csvreader = csv.reader(fin,
                                   dialect=dialect_detector(),
                                   quoting=csv.QUOTE_NONNUMERIC)

            # Checks for csvreader errors
            if len(list(csvreader)) == 0:
                inlist.remove(infile)
                raise exception_csvreader
            fin.seek(0)

            print('Successfully read file >>', infile, '<<'), print()

            # Writes CSV file columns to lists
            X = []
            Y = []

            for row in csvreader:
                X.append(row[0])
                Y.append(row[1])

            X_sorted = [x for x, _ in sorted(zip(X, Y))]
            Y_sorted = [y for _, y in sorted(zip(X, Y))]

            # Calculates interpolated SPD
            spline_calculator(X_sorted,Y_sorted, X_spectrum)

            # Appends interpolated SPD to master sheet
            output_master[infile] = spd_new

    except exception_csvreader:
        print('Warning: Skipped file because csv.reader produces no output for  >>', infile, '<<'), print()

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