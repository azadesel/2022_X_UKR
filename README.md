# 2022_X_UKR

---extract_country_from_locations.R---

This R script extracts country names from a list of user-entered Twitter locations in an Excel file. It:

Reads an Excel file containing a location column.

Cleans the text by removing punctuation.

Splits each location into words.

Matches those words to known country names using the maps::world.cities dataset.

Collects the matched country names.

Exports the results to a new Excel file.

It's designed to help analyze where users who retweeted a tweet are likely from, based on their self-declared profile location.

💡 To use this script:

Install the required R packages listed in the script.

Rename or update the input_file path to match your own .xlsx file.

Ensure your file has a column named location.

Run the script to extract and save the list of matched countries.

---Mapping_X_Locations.py---
# Description:
# This script reads a dataset of retweets, extracts country-level counts
# for each "issue", and generates choropleth maps showing global distribution.
# The map uses a log scale for color but labels legend in raw counts.
#
# Input:
#   - Excel file with 'Issues' and 'Countries' columns
#   - Shapefile for world country borders
#
# Output:
#   - JPEG maps for each issue saved in /output directory
#
# Dependencies: pandas, geopandas, matplotlib, numpy
# --------------------------------------------

