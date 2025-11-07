"""Non-spatial value outlier screening via z-scores."""
import numpy as np

def zscore_grid(values):
    v = np.asarray(values, dtype="float64")
    mu, sd = v.mean(), v.std()
    if sd == 0:
        return np.zeros_like(v)
    return (v - mu) / sd

def hotspots(values, z_threshold=1.96):
    """Return value outliers; this is not a spatial Getis-Ord statistic."""
    z = zscore_grid(values)
    return np.where(np.abs(z) >= z_threshold)[0]
