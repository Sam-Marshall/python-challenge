import os
import csv

csv_input = os.path.join("budget_data.csv")

with open(csv_input) as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_header = next(csv_reader)
	print(csv_header)