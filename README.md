# 🌈 SPD to CRI Script 

_This script was used to extract CRI data from publications dating to the early days of light-emitting diodes. This data was used to better understand the advancements of light-emitting diode technology. The research project was jointly undertaken by teams of the University of Minnesota, the University of Harvard and the University of Cambridge. It was [funded by the Alfred P. Sloan foundation](https://sloan.org/grant-detail/8567)._

### CRI Calculation

| Package | Function | Input Type* | Default CRI Version | Documentation |
| ------- | -------- | ----- | ----------- | ------------- |
| [luxpy 1.4.11.](https://github.com/ksmet1977/luxpy) | [`luxpy.color.cri.spd_to_cri`](https://ksmet1977.github.io/luxpy/build/html/color.html?highlight=spd_to_cri#luxpy.color.cri.spd_to_cri) | `ndarray` of dim. Ax2** | [IES-TM30](https://web.archive.org/web/20191220085010/https://www.ies.org/product/ies-method-for-evaluating-light-source-color-rendition/) |[readthedocs.io](https://ksmet1977.github.io/luxpy/build/html/index.html) |
| [colour-science 0.3.14](https://www.colour-science.org/) | [`colour.colour_rendering_index`](https://colour.readthedocs.io/en/develop/generated/colour.colour_rendering_index.html#colour.colour_rendering_index) | [Dictionary](https://colour.readthedocs.io/en/develop/generated/colour.SpectralDistribution.html#colour.SpectralDistribution) | [NIST CQS Simulation 7.4](https://drive.google.com/file/d/1PsuU6QjUJjCX6tQyCud6ul2Tbs8rYWW9) |[readthedocs.io](https://colour.readthedocs.io/en/develop/index.html)|

\*Assuming a SPD with of A discrete data tuples
\**Note that as of version 1.X.X. the `luxpy.spectrum.spd` function does _not_ return the spectrum in the correct format when reading from a Pandas DataFrame or another array like structure.

#### Caveats

- Check for large discontinuities in the provided SPD to avoid errors like `cri = nan`
- Differences in CRI definitions between colour-science and luxpy