import pandas as pd
import glob
import os

# Folder containing your CSVs
folder_path = r"C:\Users\Sam\OneDrive\Documents\football_stats\fixtures\silver"

# Find all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Read and combine
df_list = []
for file in csv_files:
    print(f"Reading {file}")
    df_list.append(pd.read_csv(file))

combined_df = pd.concat(df_list, ignore_index=True)

# Output file
output_path = os.path.join(folder_path, "fixtures_merged.csv")
combined_df.to_csv(output_path, index=False)

print(f"\nMerged file saved to:\n{output_path}")
