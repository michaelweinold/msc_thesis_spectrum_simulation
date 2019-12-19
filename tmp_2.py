import os
import pandas as pd
import colour

spd_dataframe = pd.read_csv(os.getcwd()+'/data/input/spd_test_red.csv',
                            names=['wavelength', 'intensity'])

spd_dataframe[spd_dataframe < 0]=0

spd_dict = dict(zip(spd_dataframe['wavelength'],spd_dataframe['intensity']))

spd = colour.SpectralDistribution(spd_dict)
cri = colour.colour_rendering_index(spd)

