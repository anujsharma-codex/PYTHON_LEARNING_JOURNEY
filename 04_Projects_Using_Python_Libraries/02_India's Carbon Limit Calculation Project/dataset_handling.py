import numpy as np
import pandas as pd

# Loading data into the dataframa variable for further extraction of required information
# Load dataset from the local project folder.
# This prevents “file not found” errors when running from a different working directory.
ds = pd.read_csv("files/carbon_emission_record.csv")

# Filter India (case-insensitive)
India = ds[ds['country'].astype(str).str.lower() == 'india']


# Extracting the required columns for our project
# Keep columns needed for intensity calculations (co2/gdp) plus a few extras for analysis.
# If you want just trend of co2, you can remove gdp.
Indian_ds = India[
    ['country', 'year', 'co2', 'gdp', 'co2_per_capita',
     'cumulative_co2', 'share_global_co2',
     'share_global_cumulative_co2', 'co2_growth_prct',
     'consumption_co2', 'trade_co2', 'total_ghg']
]


# Checking the extracted dataframe
print(Indian_ds)
