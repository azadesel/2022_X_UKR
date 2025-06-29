
"""
plot_retweet_maps.py

This script reads a dataset of retweets tagged with geopolitical 'Issues' and user-provided 'Countries',
and generates world choropleth maps showing the geographic distribution of reposts.

Maps are styled using a log scale for improved visual contrast but retain actual retweet counts in the legend.

Dependencies:
    - pandas
    - geopandas
    - matplotlib
    - numpy

Usage:
    1. Place your Excel file (with 'Issues' and 'Countries' columns) in a data/ directory.
    2. Place a shapefile of country borders (e.g., Natural Earth) in a shapefiles/ directory.
    3. Run the script. JPEG maps will be saved in the output/ directory.
"""


import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


# ------------------ Config ------------------ #

DATA_PATH = "data/data.xlsx"
SHAPEFILE_PATH = "shapefiles/ne_110m_admin_0_countries.shp"
OUTPUT_DIR = "output/"

# Country name normalization
name_map = {
    'USA': 'United States of America',
    'UK': 'United Kingdom',
    'Russia': 'Russian Federation',
}

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)




# ------------------ Load Data ------------------ #

df = pd.read_excel(DATA_PATH)
df['Countries'] = df['Countries'].str.strip().replace(name_map)

world = gpd.read_file(SHAPEFILE_PATH)
world = world[world['ADMIN'] != 'Antarctica']



# ------------------ Plotting Function ------------------ #

def plot_issue_map(issue):
    issue_data = df[df['Issues'] == issue]
    country_counts = issue_data['Countries'].value_counts().reset_index()
    country_counts.columns = ['name', 'count']

    # Merge with map and fill missing
    merged = world.merge(country_counts, left_on='ADMIN', right_on='name', how='left')
    merged['count'] = merged['count'].fillna(0)
    merged['log_count'] = np.log1p(merged['count'])

    # Color scale
    cmap = plt.cm.YlGnBu
    norm = mpl.colors.Normalize(vmin=0, vmax=merged['log_count'].max())

    fig, ax = plt.subplots(figsize=(15, 10))
    merged.plot(
        column='log_count',
        cmap=cmap,
        norm=norm,
        linewidth=0.5,
        ax=ax,
        edgecolor='0.6',
        legend=False,
        missing_kwds={'color': 'white'}
    )

    # Legend setup with real counts
    sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    max_count = int(merged['count'].max())

    base_ticks = [0, 1, 5, 10, 25, 50, 100]
    extra_ticks = [v for v in [250, 500, 1000, 2000, 5000] if v <= max_count * 1.1]
    real_ticks = base_ticks + extra_ticks
    log_ticks = np.log1p(real_ticks)

    cbar = fig.colorbar(sm, ax=ax, orientation='vertical', shrink=0.6, aspect=30,
                        pad=0.02, ticks=log_ticks)
    cbar.ax.set_yticklabels([str(v) for v in real_ticks])
    cbar.set_label("Number of Retweets", fontsize=12)

    ax.set_title(f"Distribution of Reposts on:\n{issue}", fontsize=18, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    
    # Save map
    safe_title = issue[:40].replace(' ', '_').replace('/', '_')
    filepath = os.path.join(OUTPUT_DIR, f"{safe_title}.jpeg")
    fig.savefig(filepath, dpi=300, format='jpeg', bbox_inches='tight')
    print(f"Saved: {filepath}")
    plt.close(fig)



# ------------------ Run ------------------ #

for issue in df['Issues'].dropna().unique():
    plot_issue_map(issue)

