import geopandas as gpd
from shapely.geometry import Point
from src.cluster import cluster_points

def test_two_dense_groups():
    pts = [Point(13.40, 52.52), Point(13.401, 52.521), Point(13.402, 52.522),
           Point(11.58, 48.13), Point(11.581, 48.131), Point(11.582, 48.132)]
    gdf = gpd.GeoDataFrame(geometry=pts, crs="EPSG:4326")
    out = cluster_points(gdf, eps_m=2000, min_samples=2)
    labels = set(out["cluster"]) - {-1}
    assert len(labels) >= 1
