import pandas as pd


def finding_index(data, teamNum):
    for row in data:
        if teamNum in data.keys():
            return(1)
    return(-1)

scout_data_link = "/Users/haripriyat/Scouting/Sheet1 - Sheet1 (2).csv"
csv_new_list = {}
scout_data_csv = pd.read_csv(scout_data_link)
scout_data_list= scout_data_csv.values.tolist()
for i in range(0, len(scout_data_list)):
    stats_list=[]
    team_number = scout_data_list[i][3]
    if finding_index(csv_new_list, team_number) == -1:
        stats_list.append(scout_data_list[i][7])
        tele_score = str((5*int(scout_data_list[i][15]))+(15*int(scout_data_list[i][16]))+(30*int(scout_data_list[i][17])))
        stats_list.append(tele_score)
        stats_list.append(scout_data_list[i][23])
        stats_list.append(scout_data_list[i][24])
        side_mode = [0, 0, 0]
        if scout_data_list[i][4]=="Depot Side":
            side_mode[2]= side_mode[2]+1
        elif scout_data_list[i][4]=="Middle":
            side_mode[1]= side_mode[1]+1
        else:
            side_mode[0]= side_mode[0]+1
        stats_list.append(side_mode)
        if scout_data_list[i][11] == "Level 1":
            stats_list.append("1")
        elif scout_data_list[i][11] == "Level 2":
            stats_list.append("2")
        elif scout_data_list[i][11] == "Level 3":
            stats_list.append("3")
        else:
            stats_list.append("0")
        csv_new_list[team_number] = stats_list
    else:
        temp_list = csv_new_list[team_number]
        temp_list[0] = str((float(temp_list[0]) + int(scout_data_list[i][7]))/2)
        tele_score = ((5*int(scout_data_list[i][15]))+(15*int(scout_data_list[i][16]))+(30*float(scout_data_list[i][17])))
        temp_list[1] = str((float(temp_list[1]) + tele_score)/2)
        temp_list[2] = str((float(temp_list[2]) + int(scout_data_list[i][23]))/2)
        temp_list[3] = str((float(temp_list[3]) + int(scout_data_list[i][24]))/2)
        if scout_data_list[i][4]=="Outpost Side":
            temp_list[4][0] = temp_list[4][0] +1
        elif scout_data_list[i][4]=="Middle":
            temp_list[4][1] = temp_list[4][1]+1
        else:
            temp_list[4][2]= temp_list[4][2]+1
        if scout_data_list[i][11] == "Level 1":
            temp_list[5] = str((float(temp_list[5]) +1)/2)
        elif scout_data_list[i][11] == "Level 2":
            temp_list[5] = str((float(temp_list[5]) +2)/2)
        elif scout_data_list[i][11] == "Level 3":
            temp_list[5] = str((float(temp_list[5]) +3)/2)
        else:
            temp_list[5] = str((float(temp_list[5]) +0)/2)
        csv_new_list[team_number] = temp_list
for row in csv_new_list.values():
    row[0] = str(round(float(row[0]), 2))
    row[1] = str(round(float(row[1]), 2))
    row[2] = str(round(float(row[2]), 2))
    row[3] = str(round(float(row[3]), 2))
    if row[4][2]>row[4][0] and row[4][2]>row[4][1]:
        row[4]= "Depot Side"
    elif row[4][1]>row[4][0] and row[4][1]>row[4][2]:
        row[4]= "Middle"
    elif row[4][0]>row[4][1] and row[4][0]>row[4][2]:
        row[4]= "Outpost Side"
    else:
        row[4]= "None"
    row[5] = str(round(float(row[5]), 2))
convert= pd.DataFrame.from_dict(csv_new_list,orient="index")
convert.columns = ["Auto Score", "Tele Score", "Passing Skill", "Defense Skill", "Starting Side", "Climb Score"]
convert.to_csv('scouting_csv', index_label='Team Number')

