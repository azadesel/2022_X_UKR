# 2022_X_UKR

This repository contains two scripts to analyze the geospatial spread of retweets related to key diplomatic messages from Ukraine during 2022, based on user-provided location data.

📍 extract_country_from_locations.R
This R script extracts country names from messy, user-entered Twitter profile locations.

🔧 What It Does:
Reads an Excel file containing a location column.

Cleans the text by removing punctuation.

Splits each location string into words.

Matches those words to known country names using the maps::world.cities dataset.

Collects and exports matched countries to a new Excel file.

✅ How to Use:
Install required R packages: tmaptools, maps, readxl, stringr, dplyr, writexl.

Update the file path to point to your own .xlsx file.

Make sure your Excel file has a column named location.

Run the script to generate a cleaned list of user-level countries.

🌍 Mapping_X_Locations.py
This Python script visualizes the distribution of retweeters by country across different "issues" using choropleth maps.

🔧 What It Does:
Reads an Excel dataset with 'Issues' and 'Countries' columns.

Aggregates country-level counts for each issue.

Merges counts with a world shapefile.

Applies a logarithmic color scale for clarity while preserving a legend in actual retweet counts.

Outputs one JPEG map per issue in the /output/ folder.

✅ How to Use:
Install required Python packages: pandas, geopandas, matplotlib, numpy.

Place your Excel file in the /data/ folder and name it data.xlsx.

Add your shapefile to /data/ (e.g., world_shapefile.shp, .shx, .dbf, etc.).

Run the script: python Mapping_X_Locations.py

Output maps will be saved in /output/.

