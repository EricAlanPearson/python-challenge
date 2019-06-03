#PyPoll
import os
import sys
import csv
# open file and write to file
election_data = os.path.join(".", "election_data.csv")
election_analysis = os.path.join(".", "election_analysis.txt")
# loop
def checkCandidate(name, candidate_list):
    for i in range(len(candidate_list)):
        if name == candidate_list[i]["name"]:
            index = i
            break
        else:
            index = -9999
    return index
# create a list
candidate_list = []
with open (election_data, "r", newline="") as filehandle:
    next(filehandle)
    csvreader = csv.reader(filehandle)
    total_votes = 0
    #loop
    for row in csvreader:
        total_votes += 1
        name = row[2]
        if len(candidate_list) == 0:
            candidate = {
                "name":name,
                "votes":1
                }
            candidate_list.append(candidate)
        else:
            index = checkCandidate(name, candidate_list)
            if index == -9999:
                candidate = {
                    "name":name,
                    "votes":1
                    }
                candidate_list.append(candidate)
            else:
                candidate_list[index]["votes"] += 1
# analyze file
with open (election_analysis, "w+") as filehandle:
    winner = {
        "name":"null",
        "votes":0
        }
    filehandle.write("Election results\n")
    filehandle.write("-"*32 +"\n")
    filehandle.write(f"Total Votes: {total_votes}\n")
    # loop
    for candidate in candidate_list:
        name = candidate["name"]
        votes = candidate["votes"]
        percentage = votes/total_votes
        filehandle.write(f"{name}: {percentage: .3%} ({votes})\n")
        # find the winner
        if candidate["votes"] > winner["votes"]:
            winner["name"] = candidate["name"]
            winner["votes"] = candidate["votes"]
    filehandle.write("-"*32 +"\n")
    filehandle.write(f"Winner: {winner['name']}\n")
    filehandle.write("-"*32 +"\n")
# print
with open (election_analysis, "r") as filehandle:
    print(filehandle.read())
