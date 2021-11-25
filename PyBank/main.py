#Import Modules
import os
import csv

#Create file path
filepath = os.path.join('.', 'Resources', 'budget_data.csv')
#Read csv file
date = []
profloss = []
with open(filepath) as csvfile:

    csvread = csv.reader(csvfile, delimiter = ',')
    print(csvread)

    csv_header = next(csvread)
    print(f"CSV Header: {csv_header}")

    for row in csvread:
        date.append(row[0])
        profloss.append(row[1])

profloss = [int(i) for i in profloss ]

total = sum(profloss)
    
months = len(date)

#finds the changes
change = []

for j in range(1, len(profloss)):
    #print(j, profloss[j], profloss[j-1])
    change.append(profloss[j] - profloss[j-1])

avg = sum(change)/len(change)

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

#print

print(f'Total Months: {months}')

print(f'Total:${total}')

print(f'Average  Change:{round(avg,2)}')

print(f'Greatest Increase in Profits: {date[maxidx+1]} (${maxprof})')

print(f'Greatest Dencrease in Profits: {date[minidx+1]} (${minprof})')


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




