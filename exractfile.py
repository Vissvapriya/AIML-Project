from google.colab import files
import zipfile
import os
import pandas as pd

# 1. Upload file
uploaded = files.upload()

# 2. Get the uploaded filename automatically
zip_path = list(uploaded.keys())[0]
print("Uploaded file:", zip_path)

# 3. Extract the zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("buildingnet_data")

# 4. List extracted files
extracted_files = []
for root, dirs, files_ in os.walk("buildingnet_data"):
    for file in files_:
        extracted_files.append(os.path.join(root, file))

print("Extracted files:", extracted_files)