# Extreme-climate_sen-mk

Introduction：
https://vsp.pnnl.gov/help/Vsample/Design_Trend_Mann_Kendall.htm

# Sen-MK from：
https://github.com/mmhs013/pyMannKendall

All Mann-Kendall test functions have almost similar input parameters. Those are:

- x: a vector (list, numpy array or pandas series) data
- alpha: significance level (0.05 is the default)
- lag: No. of First Significant Lags (Only available in hamed_rao_modification_test and yue_wang_modification_test)
- period: seasonal cycle. For monthly data it is 12, weekly data it is 52 (Only available in seasonal tests)
- And all Mann-Kendall tests return a named tuple which contained:

- trend: tells the trend (increasing, decreasing or no trend)
- h: True (if trend is present) or False (if the trend is absence)
- p: p-value of the significance test
- z: normalized test statistics
- Tau: Kendall Tau
- s: Mann-Kendal's score
- var_s: Variance S
- slope: Theil-Sen estimator/slope
- intercept: intercept of Kendall-Theil Robust Line, for seasonal test, full period cycle consider as unit time step

# Dependencies：
- numpy
- scipy
- gdal
