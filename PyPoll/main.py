import os
import csv

#creates a file path and reads the csv, storing the list of votes
file = os.path.join(".","Resources","election_data.csv")

votes = []

with open(file) as datacsv:
     csvread = csv.reader(datacsv, delimiter = ',')
     csv_header = next(csvread)
     #print(csv_header)
     
     for row in csvread:
          votes.append(row[2])


#creates a dictionary with candidates as the key and sets the defualt value to 0
candidates = dict.fromkeys(set(votes),0)

#loops through votes and counts the occurance for each candidate
for i in candidates:
     candidates[i] = votes.count(i)

#finds the winner
winner = max(candidates,key= candidates.get)

#prints results
print(
f'''Election Results 
------------------------- 
Total Votes:{len(votes)} 
-------------------------''')
for i in candidates:
     print(f'{i}: {"{:.2f}".format(candidates[i]/len(votes)*100)}% {candidates[i]}')
print(f'''-------------------------
Winner: {winner}''')

#writes the results to a text file
output_path = os.path.join('.', 'Analysis', 'analysis.txt')

with open (output_path,'w') as output:
     output.writelines(
     f'''Election Results
-------------------------
Total Votes:{len(votes)}
-------------------------
''')
#loops through candidates to write each as a seperate line
     for i in candidates:
          output.writelines(
               f'{i}: {"{:.2f}".format(candidates[i]/len(votes)*100)}% {candidates[i]}\n')
     output.writelines(
          f'''-------------------------
Winner: {winner}''')