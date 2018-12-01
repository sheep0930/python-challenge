import os
import csv

election_csv = os.path.join("..","..","RICEHOU201811DATA2","class-mw","03-Python","hw","Instructions","PyPoll","Resources","election_data.csv")
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    total_voter = 0
    election = {}
    for row in csvreader:
        total_voter += 1
        if row[2] in election:
            election[row[2]] += 1
        else:
            election[row[2]] = 1

    max_votes = 0

with open("election_analysis.txt","w") as textfile:
    print ("Election Results")
    print ("-------------------------")
    print (f"Total Votes: {total_voter}")
    print ("-------------------------")
   
    print ("Election Results", file=textfile)
    print ("-------------------------", file=textfile)
    print (f"Total Votes: {total_voter}", file=textfile)
    print ("-------------------------", file=textfile)

    for key in election:
        percent = election[key]/total_voter
        if max_votes < election[key]:
            max_votes = election[key]
            winner = key
        print (f"{key}: {percent:.3%} ({election[key]})")
        print (f"{key}: {percent:.3%} ({election[key]})", file=textfile)
    
    print ("-------------------------")
    print (f"Winner: {winner}")
    print ("-------------------------")
    
    print ("-------------------------", file=textfile)
    print (f"Winner: {winner}", file=textfile)
    print ("-------------------------", file=textfile)
