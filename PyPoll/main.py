import os
import csv

csv_input = os.path.join("election_data.csv")
txt_output = os.path.join("election_results.txt")

totalRows = 0
candidateList = []
allData = []
percentArray = []

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
			candidateList.append(row[2])
			allData.append(dataSummary(row[2], 1))

	for data in allData:
		data['votePercent'] = round(((data['voteAmount'] / totalRows) * 100))
		percentArray.append(data['votePercent'])

winner = allData[percentArray.index(max(percentArray))]

with open(txt_output, "w") as txtfile:
	txtfile.write("Election Results" + "\n")
	txtfile.write("-----------------------------" + "\n")
	txtfile.write("Total Votes: " + str(totalRows) + "\n")
	txtfile.write("-----------------------------" + "\n")
	for data in allData:
		txtfile.write(data['candidate'] + ": " + str(data['votePercent']) + "% (" + str(data['voteAmount']) + ")"  "\n")
	txtfile.write("-----------------------------" + "\n")
	txtfile.write("Winner: " + winner['candidate'] + "\n")
	txtfile.write("-----------------------------" + "\n")

print ("Election Results")
print ("-----------------------------")
print ("Total Votes: " + str(totalRows))
print ("-----------------------------")
for data in allData:
	print (data['candidate'] + ": " + str(data['votePercent']) + "% (" + str(data['voteAmount']) + ")")
print ("-----------------------------")
print ("Winner: " + winner['candidate'])
print ("-----------------------------")
