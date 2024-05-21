import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)

while True:
    project_name = input('Enter your project name: ')
    if project_name != "":
        break

list_of_files = [
    "Artifacts/data/raw_data/",
    "Artifacts/data/split_data/",
    "Artifacts/data/feature_engineered_data/",
    "Artifacts/data/final_data/",
    "Artifacts/Model/",
    "Documents/",
    "Notebooks/",
    f"{project_name}/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_injection.py",
    f"{project_name}/components/cleaning_feature_engineering.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_building.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/utils/__init__.py",
    "setup.py",
    "params.yaml",
    "config.yaml",
    "main.py",
    "requirements.txt",
    "logging.py",
    "exception.py",
]

# Sort the list based on the length of the paths
list_of_files_sorted = sorted(list_of_files, key=lambda x: len(x))

# Create directories
for file_path in list_of_files_sorted:
    file_path = Path(file_path)
    if file_path.suffix == '':
        os.makedirs(file_path, exist_ok=True)

# Create files
for file_path in list_of_files_sorted:
    file_path = Path(file_path)
    if file_path.suffix != '':
        filedir = file_path.parent
        os.makedirs(filedir, exist_ok=True)
        if not file_path.exists() or file_path.stat().st_size == 0:
            with open(file_path, 'w') as f:
                pass
        else:
            logging.info(f"{file_path.name} already exists at {file_path.parent}")
