import pandas as pd

# Path to the CSV inside extracted folder
csv_path = "buildingnet_data/buildingnet-3d_building_models_dataset/3DWarehouse_IDs/3dwarehouse_ids.csv"

# Load the CSV
df = pd.read_csv(csv_path)
print(df.head())   # show first few rows

# Save as a new CSV (if you want a clean copy)
df.to_csv("BuildingNet_Dataset.csv", index=False)

print("✅ CSV file created: BuildingNet_Dataset.csv")
