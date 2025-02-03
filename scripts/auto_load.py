import pandas as pd

# Fetch Google Sheet as CSV
sheet_id = "1jRNdz9G1G_UCHGRIUpRx5AThk25h8gNtT2LsBMED9cE"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
data = pd.read_csv(url)

# Convert DataFrame to Markdown Table
markdown_table = data.to_markdown(index=False)

# Read README.md
readme_path = "README.md"
with open(readme_path, "r") as file:
    lines = file.readlines()

# Define markers
start_marker = "<!-- START_TABLE -->\n"
end_marker = "<!-- END_TABLE -->\n"

if start_marker not in lines or end_marker not in lines:
    print("Markers not found in README.md. Add them manually.")
    exit(1)

# Locate markers and update table
start_index = lines.index(start_marker) + 1
end_index = lines.index(end_marker)
updated_lines = lines[:start_index] + [markdown_table + "\n"] + lines[end_index:]

# Write back to README.md
with open(readme_path, "w") as file:
    file.writelines(updated_lines)

print("README.md updated successfully!")