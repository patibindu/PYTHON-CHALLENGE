# First we will import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading csv files
import csv

# Path to collect data from the Resource folder
election_data_filepath = os.path.join("Resources", "election_data.csv")

with open(election_data_filepath, newline='') as electionfile:
    csv_reader = csv.reader(electionfile, delimiter=',')
    
    # store the header row
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    
    # declare variables
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # read each row of data after header
    for row in csv_reader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # count the number of votes
    total_votes = (len(votes))
    # print(total_votes)

    # votes by person
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
    # Percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
    
    # Winner 
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles Casper Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        winner = "Diana DeGette"  
    else:
        winner = "Raymon Anthony Doane"

    # Print Statements
    print(f'''Election Results
------------------------------------------------
Total Votes: {total_votes}
------------------------------------------------
Charles Casper Stockham: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon Anthony Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
------------------------------------------------
Winner: {winner}
------------------------------------------------''')

    # Output to a text file
    output_filepath = os.path.join("Analysis", "Results.txt")
    outputfile = open(output_filepath,"w")
    outputfile.write(f'''Election Results
------------------------------------------------
Total Votes: {total_votes}
------------------------------------------------
Charles Casper Stockham: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon Anthony Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
------------------------------------------------
Winner: {winner}
------------------------------------------------''')

    outputfile.close()
