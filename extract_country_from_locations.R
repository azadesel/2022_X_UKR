# ----------------------------------------------------------
# Extract Countries from Twitter User Locations (R Script)
# ----------------------------------------------------------
# Author: [Your Name]
# Date: [YYYY-MM-DD]
#
# Description:
# This script processes user-provided Excel files containing
# manually entered Twitter profile locations and extracts
# country names by matching them with the world.cities dataset.
#
# Input:
#   - An Excel (.xlsx) file with a column named 'location'
#
# Output:
#   - A cleaned list of matched countries saved as an Excel file
#
# Requirements:
#   - R packages: tmaptools, tmap, dplyr, readxl, stringr, maps, writexl
#
# Usage:
#   1. Place your .xlsx file in the project directory.
#   2. Set the input file name below.
#   3. Run the script.
# ----------------------------------------------------------

# Load required packages
library(tmaptools)
library(tmap)
library(dplyr)
library(readxl)
library(stringr)
library(maps)
library(writexl)

# -------- USER INPUT --------

# Replace this with your actual input file name
input_file <- "your_file.xlsx"

# Output file (auto-generated)
output_file <- paste0("countries_from_", tools::file_path_sans_ext(basename(input_file)), ".xlsx")

# -------- LOAD DATA --------

# Check file existence
if (!file.exists(input_file)) {
  stop("❌ Input file not found. Please place your .xlsx file in the project directory and update 'input_file'.")
}

# Read input file
origin <- read_xlsx(input_file)

# Ensure required column exists
if (!"location" %in% names(origin)) {
  stop("❌ The input file must contain a column named 'location'.")
}

# Load country & city data
data(world.cities)

# -------- CLEAN AND MATCH --------

# Remove punctuation and line breaks
location_info <- gsub("[[:punct:]\n]", "", origin$location)

# Split into words
location_words <- strsplit(location_info, " ")

# Match to countries in maps::world.cities
CountryList_raw <- lapply(location_words, function(x) {
  matches <- x[which(toupper(x) %in% toupper(world.cities$country.etc))]
  return(matches)
})

# Flatten into data frame
country_list <- do.call(rbind, lapply(CountryList_raw, as.data.frame))
colnames(country_list) <- c("Country")

# -------- EXPORT OUTPUT --------

# Save results
write_xlsx(country_list, output_file)
cat(paste0("✅ Extraction complete. File saved as: ", output_file, "\n"))
