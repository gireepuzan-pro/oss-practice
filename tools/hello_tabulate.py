import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["Name", args.name],
    ["Country", "Nepal"],
    ["Library", "tabulate"],
    ["Goal", "Learn Python and open source"]
]

print(tabulate(rows, tablefmt="grid"))
