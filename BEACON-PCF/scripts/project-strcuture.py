from pathlib import Path

# Project name
PROJECT_NAME = "BEACON-PCF"

# Folder structure
folders = [
    "data",
    "notebooks",
    "src",
    "figures",
    "results",
    "scripts"
]

files = {}

# Create project directory
project = Path(PROJECT_NAME)
project.mkdir(exist_ok=True)

# Create folders
for folder in folders:
    (project / folder).mkdir(parents=True, exist_ok=True)

# Create files
for filename, content in files.items():
    filepath = project / filename
    if not filepath.exists():
        filepath.write_text(content, encoding="utf-8")

print(f" '{PROJECT_NAME}' project structure created ")