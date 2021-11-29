#Import Modules
import os
import csv

#Creates file path, reads the csv and writes the dates and profits to lists
filepath = os.path.join('.', 'Resources', 'budget_data.csv')
date = []
profloss = []
with open(filepath) as csvfile:

    csvread = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvread)
   

    for row in csvread:
        date.append(row[0])
        profloss.append(row[1])
#converts the profits to an integer
profloss = [int(i) for i in profloss ]

#finds the total profit/loss
total = sum(profloss)
#find the number of months    
months = len(date)

#calculates the changes in profit/loss for each month
change = []

for j in range(1, len(profloss)):
    #print(j, profloss[j], profloss[j-1])
    change.append(profloss[j] - profloss[j-1])
#calculates average change in profit
avg = sum(change)/len(change)

#finds the months with the greatest profit and greatest loss
maxprof = 0
for idx in range(0,len(change)):
    if maxprof< change[idx]:
        maxprof=change[idx]
        maxidx = idx

minprof = 0
for idx in range(0,len(change)):
    if minprof> change[idx]:
        minprof=change[idx]
        minidx = idx

#prints the analysis
print('Financial An\alysis')
print('----------------------------')
print(f'Total Months: {months}')

print(f'Total:${total}')

print(f'Average  Change:{round(avg,2)}')

print(f'Greatest Increase in Profits: {date[maxidx+1]} (${maxprof})')

print(f'Greatest Dencrease in Profits: {date[minidx+1]} (${minprof})')

#writes the analysis to a text file
output_path = os.path.join('.', 'Analysis', 'analysis.txt')

with open (output_path,'w') as output:
    output.writelines(
        'Financial Analysis\n'
        '----------------------------\n'
        f'Total Months: {months}\n'
        f'Total:${total}\n'
        f'Average  Change:{round(avg,2)}\n'
        f'Greatest Increase in Profits: {date[maxidx+1]} (${maxprof})\n'
        f'Greatest Dencrease in Profits: {date[minidx+1]} (${minprof})')




