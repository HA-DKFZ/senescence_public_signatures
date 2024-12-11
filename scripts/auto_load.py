import pandas as pd

# Fetch Google Sheet as CSV
sheet_id = "1jRNdz9G1G_UCHGRIUpRx5AThk25h8gNtT2LsBMED9cE"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
data = pd.read_csv(url)

# Convert DataFrame to Markdown Table
markdown_table = data.to_markdown(index=False)

# Update the Markdown File
with open("README.md", "r") as file:
    lines = file.readlines()

# Replace existing table (assuming it's between specific markers)
start_marker = "<!-- START_TABLE -->"
end_marker = "<!-- END_TABLE -->"

start_index = lines.index(f"{start_marker}\n") + 1
end_index = lines.index(f"{end_marker}\n")

updated_lines = lines[:start_index] + [markdown_table + "\n"] + lines[end_index:]

with open("README.md", "w") as file:
    file.writelines(updated_lines)