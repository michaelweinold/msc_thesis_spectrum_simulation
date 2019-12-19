import luxpy
import os
import pandas as pd
import colour
'''
spd_dataframe = pd.read_csv(os.getcwd()+'/data/input/spd_test_red.csv',
                            names=['wavelength', 'intensity'])

spd_dataframe[spd_dataframe < 0]=0

pd.DataFrame.sort_values(spd_dataframe,
                         by='wavelength',
                         inplace=True)

spd_spectrum = luxpy.spectrum.spd(data=spd_dataframe,
                                  norm_type='lambda',
                                  )

testspd = colour.read_spectral_data_from_csv_file(os.getcwd()+'/data/input/spd_test_red.csv')
cri = colour.colour _rendering_index(testspd)
'''

luxpy.plotDL(