import csv
import os

#files to load and output
input_file = os.path.join("Resources","election_data.csv")
output_file = os.path.join("Analysis", "election_analysis.txt")

#total vote count
total_votes = 0

#candidates
list_candidate_khan = 0
list_candidate_correy = 0
list_candidate_li = 0
list_candidate_otooley = 0
khan_percentage = 0
correy_percentage = 0
li_percentage = 0
otooley_percentage = 0

with open(input_file) as election_data:
    csvreader = csv.reader(election_data, delimiter =",")
    header = next(csvreader)
   
       
 # To find the list of candidate
    if row[2] not in CandidateList:
        CandidateList.append(row[2])

#print(CandidateList)
    total_votes += 1
        if row[2] == 'Khan':
            list_candidate_khan += 1
        if row[2] == 'Correy':
            list_candidate_correy += 1
        if row[2] == 'Li':
            list_candidate_li += 1
        if row[2] == "O'Tooley":
            list_candidate_otooley += 1

    khan_percentage = round((1-((total_votes - list_candidate_khan)/total_votes))*100,0)
    correy_percentage = round((1-((total_votes - list_candidate_correy)/total_votes))*100,0)
    li_percentage = round((1-((total_votes - list_candidate_li)/total_votes))*100,0)
    otooley_percentage = round((1-((total_votes - list_candidate_otooley)/total_votes))*100,0)

    if list_candidate_khan > list_candidate_correy:
        winner = "Khan"
        elif list_candidate_correy > list_candidate_li:
        winner = "Correy"
        elif list_candidate_li > list_candidate_otooley:
        winner = "Li"
        else:
        winner = "O'Tooley"

       output = (with open(output_file, "w") as txt_file:
        	election_results = (
                f"\nElection Results\n"
                f"------------------------\n"
                f"Total Votes: {total_votes}\n"
                f"------------------------\n"


            print("Election Results", end = "")

            txt_file.write (election_results)

            for i in range (len(candidate_df)):
                voter output = (
                    f"{candidate_df.loc[i, Çandidate']}:"
                    f"{candidate_df.loc[i, 'Percentage of Total']:3f}%"
                    f"({candidate_df.loc[i, 'Votes']})\n"
                )
                print (voter_output, end = "") 
                txt_file.write (voter_output)

                winning_candidate_summary = (
                    f"------------------------\n"
                    f"Winner: {candidate_df.loc[0, `candidate`]}\n"
                    f"------------------------"
                )

            print (winning_candidate_summary)
            txt_file.write(winning_candidate_summary)
            