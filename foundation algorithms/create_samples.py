# Sample Data Generator
# This script creates smaller versions of the large datasets for GitHub

import pandas as pd
import os

# Create datasets directory if it doesn't exist
os.makedirs('datasets/samples', exist_ok=True)

# List of large files to create samples from
large_files = [
    'datasets/train_fe.csv',
    'datasets/train_fe_v2.csv',
    'datasets/test_fe.csv',
    'datasets/test_fe_v2.csv'
]

# Create sample files (first 1000 rows)
for file in large_files:
    if os.path.exists(file):
        print(f"Creating sample for {file}...")
        df = pd.read_csv(file)
        
        # Take first 1000 rows or fewer if file is smaller
        sample_size = min(1000, len(df))
        df_sample = df.head(sample_size)
        
        # Create output filename
        base_name = os.path.basename(file)
        sample_name = os.path.join('datasets/samples', f"{os.path.splitext(base_name)[0]}_sample.csv")
        
        # Save sample
        df_sample.to_csv(sample_name, index=False)
        print(f"Saved sample to {sample_name}")
    else:
        print(f"Warning: {file} not found")

print("Sample generation complete!")
