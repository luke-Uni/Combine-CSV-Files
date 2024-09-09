import os
import glob
import pandas as pd

# Set directory where CSV files are located
csv_dir = "Path to directory containing CSV files"

# Get all CSV files in directory
csv_files = glob.glob(os.path.join(csv_dir, '.csv'))

# Combine all CSV files into one DataFrame
combined_df = pd.concat([pd.read_csv(f, skiprows=1) for f in csv_files])

# Write combined DataFrame to CSV file
combined_df.to_csv('combined_data.csv', index=False)