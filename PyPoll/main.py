import os
import csv

csv_input = os.path.join("election_data.csv")

totalRows = 0
candidateList = []
countyList = []
allData = []
candidateCounter = 0
countyCounter = 0

def dataSummary(candidate, voteTotal):
	data = {
		'candidate': '',
		'voteAmount': 0,
		'votePercent': 0
	}
	data['candidate'] = candidate
	data['voteAmount'] = voteTotal
	return data

with open(csv_input, "r") as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_header = next(csv_reader)

	for row in csv_reader:
		totalRows += 1
		for data in allData:
			if data['candidate'] == row[2]:
				data['voteAmount'] += 1
		if row[2] not in candidateList:
			candidateCounter = 0
			candidateList.append(row[2])
			candidateCounter += 1
			allData.append(dataSummary(row[2], candidateCounter))
		if row[1] not in countyList:
			countyCounter = 0
			countyList.append(row[1])
			countyCounter += 1

	for data in allData:
		print (int(data['voteAmount'])/totalRows) * 100

print allData
print totalRows
