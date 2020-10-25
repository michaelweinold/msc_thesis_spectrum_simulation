## 🌈 SPD to CRI Script

_This script was used to extract CRI data from publications dating to the early days of light-emitting diodes. This data was used to better understand the advancements of light-emitting diode technology. The research project was jointly undertaken by teams of the University of Minnesota, the University of Harvard and the University of Cambridge. It was [funded by the Alfred P. Sloan foundation](https://sloan.org/grant-detail/8567)._

### CRI Computation

| Package | Function | Input Type* | Default CRI Version | Documentation |
| ------- | -------- | ----- | ----------- | ------------- |
| [luxpy 1.4.14.](https://github.com/ksmet1977/luxpy) | [`luxpy.color.cri.spd_to_cri`](https://ksmet1977.github.io/luxpy/build/html/color.html?highlight=spd_to_cri#luxpy.color.cri.spd_to_cri) | `ndarray`, dim=(Ax2)** | [IES-TM30](https://web.archive.org/web/20191220085010/https://www.ies.org/product/ies-method-for-evaluating-light-source-color-rendition/) |[readthedocs.io](https://ksmet1977.github.io/luxpy/build/html/index.html) |
| [colour-science 0.3.14](https://www.colour-science.org/) | [`colour.colour_rendering_index`](https://colour.readthedocs.io/en/develop/generated/colour.colour_rendering_index.html#colour.colour_rendering_index) | [Dictionary](https://colour.readthedocs.io/en/develop/generated/colour.SpectralDistribution.html#colour.SpectralDistribution) | [NIST CQS Simulation 7.4](https://drive.google.com/file/d/1PsuU6QjUJjCX6tQyCud6ul2Tbs8rYWW9) |[readthedocs.io](https://colour.readthedocs.io/en/develop/index.html)|

\*Assuming a SPD with of A discrete data tuples \
\**Note that as of version 1.X.X. the `luxpy.spectrum.spd` function does _not_ return the spectrum in the correct format when reading from a Pandas DataFrame or another array like structure.

### CRI Illumination Simulation

| Package | Function | Input Type* | Default CRI Version | Documentation |
| ------- | -------- | ----- | ----------- | ------------- |
| [luxpy 1.4.14.](https://github.com/ksmet1977/luxpy) | [`luxpy.toolboxes.hypspcim.hyperspectral_img_simulator`](https://ksmet1977.github.io/luxpy/build/html/_modules/luxpy/toolboxes/hypspcim/hyperspectral_img_simulator.html) | `ndarray`, dim=(Ax2)** | [IES-TM30](https://web.archive.org/web/20191220085010/https://www.ies.org/product/ies-method-for-evaluating-light-source-color-rendition/) |[readthedocs.io](https://ksmet1977.github.io/luxpy/build/html/toolboxes.html#hypspcim) |

[List of CIE standard illuminants in the luxpy source code](https://github.com/ksmet1977/luxpy/blob/master/luxpy/spectrum/basics/spectral_databases.py) \
[List of CIE standard illuminants on Wikipedia](https://en.wikipedia.org/wiki/Standard_illuminant)

### Luminous Efficacy Computation

| Package | Function | Source | Documentation |
| ------ | -------- | ------ | ------------- |
| [colour-science 0.3.14](https://www.colour-science.org/) | [`colour.luminous_efficacy`](https://www.colour-science.org/) | [Source](https://colour.readthedocs.io/en/latest/_modules/colour/colorimetry/photometry.html#luminous_efficacy) | [readthedocs.io](https://ksmet1977.github.io/luxpy/build/html/index.html) |

### Color Temperature (CCT) Computation

| Package | Function | Source | Documentation |
| ------ | -------- | ------ | ------------- |
| [colour-science 0.3.14](https://www.colour-science.org/) | [`xy_to_CCT` or `colour.temperature.xy_to_CCT_Kang2002(xy)`](https://colour.readthedocs.io/en/latest/colour.temperature.html?highlight=color%20temperature#correlated-colour-temperature) | [Source](https://colour.readthedocs.io/en/latest/_modules/colour/temperature.html#xy_to_CCT) | [readthedocs.io](https://colour.readthedocs.io/en/latest/index.html) |

Note: Limitations on max. CCT [K] apply, depending on method used. \
[Method *Kang (2002)*](https://github.com/michaelweinold/colour/blob/develop/colour/temperature/kang2002.py): 1,667<CCT<25,000K. \
[Method *CIE D*](https://github.com/michaelweinold/colour/blob/develop/colour/temperature/cie_d.py): 4,000<CCT<25,000K.

### CCT Gradient Rendering

[`luxpy.color.cct.cct_to_xyz`](https://ksmet1977.github.io/luxpy/build/html/color.html?highlight=color%20temperature#luxpy.color.cct.cct_to_xyz)
[`luxpy.color.ctf.colortransforms.xyz_to_srgb`](https://ksmet1977.github.io/luxpy/build/html/color.html?highlight=rgb#luxpy.color.ctf.colortransforms.xyz_to_srgb)

[Similar Wikipedia CCT figure](https://commons.wikimedia.org/wiki/File:Color_temperature_black_body_800-12200K.svg)

[`matplotlib.colors.ListedColormap()`](https://matplotlib.org/2.0.2/api/colors_api.html#matplotlib.colors.ListedColormap)

[`matplotlib.pyplot.imshow`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib-pyplot-imshow)
