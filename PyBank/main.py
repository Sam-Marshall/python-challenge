import os
import csv

totalRows = 0
netProfit = 0
allData = []
revChangeArray = []

currentMonth = ""
currentRevenue = 0
prevRevenue = 0

greatestInc = {}
greatestDec = {}
avProfitChange = 0

csv_input = os.path.join("budget_data.csv")
txt_output = os.path.join("budget_summary.txt")

def monthInfo(month, revenue, change):
	rowData = {
		'month' : '',
		'revenue' : 0,
		'revChange' : 0
	}
	rowData["revenue"] = revenue
	rowData["month"] = month
	rowData["revChange"] = change
	return rowData

with open(csv_input, 'r') as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_header = next(csv_reader)
	
	for row in csv_reader:
		
		totalRows += 1
		currentMonth = row[0]
		currentRevenue = int(row[1])
		netProfit += currentRevenue

		if totalRows > 1:
			revenueChange = currentRevenue - prevRevenue
			allData.append(monthInfo(currentMonth, currentRevenue, revenueChange))
			revChangeArray.append(revenueChange)

		prevRevenue = currentRevenue

greatestDec = allData[revChangeArray.index(min(revChangeArray))]
greatestInc = allData[revChangeArray.index(max(revChangeArray))]
avProfitChange = sum(revChangeArray) / len(revChangeArray)

with open(txt_output, 'w') as file:
	file.write("Financial Analysis\n")
	file.write("------------------------------------\n")
	file.write("Total Months: " + str(totalRows) + "\n")
	file.write("Total: $" + str(netProfit) + "\n")
	file.write("Average Change: $" + str(avProfitChange) + "\n")
	file.write("Greatest Increase in Profits: " + greatestInc["month"] + " ($" + str(greatestInc["revChange"]) + ")" + "\n")
	file.write("Greatest Decrease in Profits: " + greatestDec["month"] + " ($" + str(greatestDec["revChange"]) + ")" + "\n")

print "Financial Analysis"
print "------------------------------------"
print "Total Months: " + str(totalRows)
print "Total: $" + str(netProfit)
print "Average Change: $" + str(avProfitChange)
print "Greatest Increase in Profits: " + greatestInc["month"] + " ($" + str(greatestInc["revChange"]) + ")"
print "Greatest Decrease in Profits: " + greatestDec["month"] + " ($" + str(greatestDec["revChange"]) + ")"
