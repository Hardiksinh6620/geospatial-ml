import numpy as np
from src.hotspot import zscore_grid,hotspots
def test_constant_values(): assert np.array_equal(zscore_grid([2,2,2]),[0,0,0])
def test_value_outlier(): assert 4 in hotspots([1,1,1,1,100])
