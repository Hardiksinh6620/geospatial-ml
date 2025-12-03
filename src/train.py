"""CLI entry point."""
import argparse
import geopandas as gpd
from .cluster import cluster_points

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--eps", type=float, default=500)
    args = ap.parse_args()
    gdf = gpd.read_file(args.input)
    out = cluster_points(gdf, eps_m=args.eps)
    print(out["cluster"].value_counts())

if __name__ == "__main__":
    main()
