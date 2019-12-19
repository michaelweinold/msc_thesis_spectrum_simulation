# SPD to CRI Script

The CRI is calculated using the Python module [colour-science 0.3.14](https://www.colour-science.org/)
based on equations in the [NIST CQS simulation 7.4](https://drive.google.com/file/d/1PsuU6QjUJjCX6tQyCud6ul2Tbs8rYWW9) by  _Y. Ohno and W. Davis_ given in [the source code for the 'colour_quality_cri' class](https://colour.readthedocs.io/en/develop/_modules/colour/quality/cri.html).

_This script was used to ectract CRI data from publications dating to the early days of light-emitting diodes. This data was used to better understand the advancements of light-emitting diode technology. The research project was jointly undertaken by teams of the University of Minnesota, the University of Harvard and the University of Cambridge. It was [funded by the Alfred P. Sloan foundation](https://sloan.org/grant-detail/8567)._

#### CRI Calculation

The CRI associated with a given SPD of an LED luminaire can be calculated using the [`colour.colour_rendering_index.cri`](https://github.com/colour-science/colour/blob/develop/colour/quality/cri.py) module of the [`colour-science`](https://www.colour-science.org/) package.

#### CRI Illumination Simulation

The effect of a certain CRI value associated with a given SPD of an LED luminaire can be simulated  using the [`luxpy.toolboxes.hypspcim.hyperspectral_img_simulator`](https://ksmet1977.github.io/luxpy/build/html/_modules/luxpy/toolboxes/hypspcim/hyperspectral_img_simulator.html) module of the [`luxpy`](https://ksmet1977.github.io/luxpy/build/html/index.html) package. 

1. Spectral data is loaded from CSV files into Pandas DataFrames
2. Negative values are set to zero
3. Values are sorted by wavelength
4. DataFrames are written to a dictionary

   `{'csv_name':DataFrame,…}`

#### Caveats

- Check for large discontinuities in the provided SPD to avoid errors like `cri = nan`
- The `luxpy.spd()` function does not return an array of correct dimensions
- Difference in CRI definitions between colour-science and luxpy


Michael Weinold \
University of Cambridge \
2019-2020
