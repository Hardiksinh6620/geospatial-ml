"""Spatial clustering."""
import numpy as np
import geopandas as gpd
from sklearn.cluster import DBSCAN

def cluster_points(gdf, eps_m=500, min_samples=5):
    """DBSCAN on projected coordinates. Reprojects to EPSG:3857 first."""
    g = gdf.to_crs("EPSG:3857")
    coords = np.column_stack([g.geometry.x, g.geometry.y])
    labels = DBSCAN(eps=eps_m, min_samples=min_samples).fit_predict(coords)
    out = gdf.copy()
    out["cluster"] = labels
    return out
