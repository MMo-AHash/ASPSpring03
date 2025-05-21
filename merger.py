# In The Name Of Allah
import nbformat
from pathlib import Path

# List of notebooks to merge (relative paths)
notebook_files = [
    "BMTGaussianRealization.ipynb",
]

# Create a new notebook object
merged = nbformat.v4.new_notebook()
merged.cells = []

merged.cells.append(nbformat.v4.new_markdown_cell("<center><img src=\"unnamed.png\" width=\"40%\"></center>"))

for filename in notebook_files:
    with open(filename, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Append all cells from this notebook
    merged.cells.extend(nb['cells'])

# Write out the merged notebook
output_path = "main.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    nbformat.write(merged, f)

print(f"Merged notebook saved to: {output_path}")