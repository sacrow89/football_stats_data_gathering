import json
import pandas as pd
from pathlib import Path

# Season year
season_year = 2025

# Base directory where the JSON files live
base_dir = Path(r"C:\Users\Sam\OneDrive\Documents\football_stats\fixtures\raw")

# Output directory where the CSV files will live
out_dir = Path(r"C:\Users\Sam\OneDrive\Documents\football_stats\fixtures\silver")

# Input / output files
input_file = base_dir / f"fixtures_{season_year}.json"
output_file = out_dir / f"fixtures_{season_year}_flattened.csv"

# Load the JSON file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract the list of fixtures
fixtures = data["response"]

# Flatten the JSON into a DataFrame
df = pd.json_normalize(
    fixtures,
    sep="_"
)

# ✅ Add season column
df["season"] = season_year

# Save to CSV
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"Flattened data saved to {output_file}")
print("Preview of data:")
print(df.head())
