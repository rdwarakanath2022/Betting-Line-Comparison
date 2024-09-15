import csv
# Creates output.csv
# def computed_column(csvfile):
#     with open(csvfile,newline='') as f:
#         with open('input.csv','w',newline='') as f2:
#             writer = csv.writer(f2)
#             rows = csv.reader(f)
#             for row in rows:
#                 y=[]
#                 y.append(int(row[3]) - int(row[8]))
#                 writer.writerow(row+y)
                
# def keep_last_column(csvfile):
#     with open(csvfile, newline='') as f:
#         with open('new_input.csv', 'w', newline='') as f2:
#             reader = csv.reader(f)
#             writer = csv.writer(f2)
            
#             for row in reader:
#                 if row:  # Ensure the row is not empty
#                     last_column = [row[-1]]  # Keep only the last column
#                     writer.writerow(last_column)
                    
# def combine_columns_side_by_side(csvfile1, csvfile2, outputfile):
#     with open(csvfile1, newline='') as f1, open(csvfile2, newline='') as f2, open(outputfile, 'w', newline='') as fout:
#         reader1 = csv.reader(f1)
#         reader2 = csv.reader(f2)
#         writer = csv.writer(fout)
        
#         # Read all rows from both files into lists
#         rows1 = list(reader1)
#         rows2 = list(reader2)
        
#         # Determine the maximum number of rows
#         max_rows = max(len(rows1), len(rows2))
        
#         # Write the combined rows
#         for i in range(max_rows):
#             row1 = rows1[i] if i < len(rows1) else []  # Get row from file1 or empty if out of range
#             row2 = rows2[i] if i < len(rows2) else []  # Get row from file2 or empty if out of range
#             combined_row = row1 + row2  # Combine columns side-by-side
#             writer.writerow(combined_row)

# combine_columns_side_by_side('/Users/rishabh/Betting-Line-Comparison/input3.csv', '/Users/rishabh/Betting-Line-Comparison/input2.csv', 'input.csv')
                
# computed_column('/Users/rishabh/Betting-Line-Comparison/sports/nfl_game_scores_1g_2023_sample.csv')
# keep_last_column('/Users/rishabh/Betting-Line-Comparison/input.csv')

# Creates input.csv

# def process_csv(input_file, output_file):
#     with open(input_file, 'r', newline='') as infile, open(output_file, 'a', newline='') as outfile:
#         reader = csv.reader(infile)
#         writer = csv.writer(outfile)

#         for row in reader:
#             if len(row) > 2:
#                 modified_column = ' '.join(word.capitalize() for word in row[2].replace('_', ' ').split())
#                 writer.writerow([modified_column])

# # Example usage
# input_csv = '/Users/rishabh/Betting-Line-Comparison/nfl_game_scores_1g_2023_sample.csv'
# output_csv = '/Users/rishabh/Betting-Line-Comparison/input3.csv'
# process_csv(input_csv, output_csv)

from collections import defaultdict

# def count_names_in_csv(file_path, output_file_path):
#     name_counts = {}
#     updated_rows = []

#     # Read the CSV file and process the rows
#     with open(file_path, mode='r', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         headers.append('Count')
#         updated_rows.append(headers)
        
#         for row in reader:
#             name = row[0]
#             if name in name_counts:
#                 name_counts[name] += 1
#             else:
#                 name_counts[name] = 1
#             row.append(str(name_counts[name]))
#             updated_rows.append(row)

#     # Write the updated rows to a new CSV file
#     with open(output_file_path, mode='w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(updated_rows)

# # Example usage
# file_path = '/Users/rishabh/Betting-Line-Comparison/input.csv'
# output_file_path = '/Users/rishabh/Betting-Line-Comparison/input2.csv'
# count_names_in_csv(file_path, output_file_path)

# teamScores = {} # team: [[pts, ptsAllowed],...]

# def processTeam(team, opponent):
#     teamScores[team[0]].append([int(team[1]),int(opponent[1])])

# def getAvg(team, numGames= None): # -> [pts, ptsAllowed]
#     length = len(teamScores[team])
#     if numGames == None:
#         numGames = length
#     if length == 0:
#         return [0,0]
#     if length < numGames:
#         return getAvg(team, length)
    
#     # hopefully gives the last numGames elements of the list
#     games = teamScores[team][-numGames:length]
    
#     # average
#     out = [0,0]
#     for g in games:
#         out[0] += g[0]
#         out[1] += g[1]
#     out[0] /= numGames
#     out[1] /= numGames
#     return out
    
    
# def getUpdatedRow(homeTeam, awayTeam):
#     # add both teams to teamScores
#     if homeTeam not in teamScores:
#         teamScores[homeTeam] = []
#     if awayTeam not in teamScores:
#         teamScores[awayTeam] = []
    
#     return [awayTeam, homeTeam, len(teamScores[awayTeam]), len(teamScores[homeTeam]), "prevYearAwayPts", "prevYearHomePts", getAvg(awayTeam)[0], getAvg(homeTeam)[0], getAvg(awayTeam, 3)[0], getAvg(homeTeam, 3)[0], getAvg(awayTeam, 1)[0], getAvg(homeTeam, 1)[0],"prevYearAwayPtsAllowed", "prevYearHomePtsAllowed", getAvg(awayTeam)[1], getAvg(homeTeam)[1], getAvg(awayTeam, 3)[1], getAvg(homeTeam, 3)[1], getAvg(awayTeam, 1)[1], getAvg(homeTeam, 1)[1]]

# def count_names_in_csv(file_path, output_file_path):
#     #name_counts = {}
#     updated_rows = []
    

#     # Read the CSV file and process the rows
#     with open(file_path, mode='r', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         headers.append('Count')
#         updated_rows.append(headers)
        
#         for row in reader:
            
#             awayTeam = row[2:4]
#             homeTeam = row[7:9]
            
#             updated_rows.append(getUpdatedRow(homeTeam[0],awayTeam[0]))
            
#             processTeam(homeTeam,awayTeam)
#             processTeam(awayTeam,homeTeam)

            
            

#     # Write the updated rows to a new CSV file
#     with open(output_file_path, mode='w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(updated_rows)

# count_names_in_csv("/Users/rishabh/Betting-Line-Comparison/nfl_game_scores_1g_2023_sample.csv", "/Users/rishabh/Betting-Line-Comparison/new.csv")

# import pandas as pd
# df = pd.read_csv('/Users/rishabh/Betting-Line-Comparison/new.csv') 
# df2 = pd.read_csv('/Users/rishabh/Betting-Line-Comparison/input.csv')
# df['5'] = df2['5']
# df['6'] = df2['6']
# df['13'] = df2['7']
# df['14'] = df2['8']
# df.to_csv('/Users/rishabh/Betting-Line-Comparison/input2.csv', index=False)