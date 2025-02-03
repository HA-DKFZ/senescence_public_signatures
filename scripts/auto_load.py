import pandas as pd

# Fetch Google Sheet as CSV
sheet_id = "1jRNdz9G1G_UCHGRIUpRx5AThk25h8gNtT2LsBMED9cE"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

try:
    data = pd.read_csv(url)
except Exception as e:
    print(f"Error fetching Google Sheet: {e}")
    exit(1)

# Convert DataFrame to Markdown Table
markdown_table = data.to_markdown(index=False, tablefmt="pipe")  # Ensures correct GitHub format

# Read README.md
readme_path = "README.md"
with open(readme_path, "r") as file:
    lines = file.readlines()

# Define markers
start_marker = "<!-- START_TABLE -->"
end_marker = "<!-- END_TABLE -->"

# Check if markers exist
try:
    start_index = next(i for i, line in enumerate(lines) if start_marker in line) + 1
    end_index = next(i for i, line in enumerate(lines) if end_marker in line)
    
    # Update table between markers (preserve correct formatting)
    updated_lines = (
        lines[:start_index] +
        ["\n", markdown_table, "\n"] +  # Ensures no extra spacing
        lines[end_index:]
    )
    
    # Write back to README.md
    with open(readme_path, "w") as file:
        file.writelines(updated_lines)

    print("README.md updated successfully!")

except StopIteration:
    print("Error: One or both markers (`<!-- START_TABLE -->` and `<!-- END_TABLE -->`) are missing.")
    print("Please add the following markers manually in `README.md`:")
    print(f"\n{start_marker}\n(Your table here)\n{end_marker}")
    exit(1)