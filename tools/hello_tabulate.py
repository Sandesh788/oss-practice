import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
args = parser.parse_args()

data = [
    ["Name", args.name],
    ["Country", "Nepal"],
    ["Subject", "Computer Science"],
    ["Programming", "Python"]
]

print(tabulate(data, headers=["Category", "Details"], tablefmt="grid"))