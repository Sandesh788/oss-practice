
import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

# Get CSV file path from command line
parser = argparse.ArgumentParser(description="Filter server data from a CSV file")
parser.add_argument("csv_path", help="Path to the CSV file")
args = parser.parse_args()

# Read CSV file
df = pd.read_csv(args.csv_path)

# Custom filter: Select servers with CPU usage greater than 80
result = df[df["cpu"] > 80]

# Create Rich table
table = Table(title="Servers with CPU Usage Above 80%")

for column in result.columns:
    table.add_column(column)

for row in result.itertuples(index=False):
    table.add_row(*[str(value) for value in row])

# Display table
console = Console()
console.print(table)

# Save filtered data to Excel
result.to_excel("result.xlsx", index=False)
print("Saved result.xlsx")
