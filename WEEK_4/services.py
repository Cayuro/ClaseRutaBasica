from usuarios_csv import downloading_csv, save_csv_soccer
from validator import valid_only_txt, valid_num

def add_soccer(file_soccer):
    teams = downloading_csv(file_soccer)
    new_team = valid_only_txt("Name of the team: ")
    while True: 
        pj = valid_num("Matches played: ")
        pg = valid_num("Matches won: ")
        pe = valid_num("Matches drawn: ")
        pp = valid_num("Matches lost: ")
        if (pg + pe + pp) != pj:
            continue
        pts = (pg*3) + (pe) 
        break
 

    new_soccer ={"Soccer_team" : new_team,
    "PJ": pj,
    "PG": pg,
    "PE": pe,
    "PP": pp,
    "Pts": pts 
    }

    teams.append(new_soccer)
    print(f"This is the new soccer team \n{new_soccer}")
    save_csv_soccer(teams)

def show_soccer(file_soccer):
    teams = downloading_csv(file_soccer)
    print(teams)

def update_soccer(file_soccer):
    print(f"We are working to update the {file_soccer}")

def delete_soccer(file_soccer):
    print(f"We are working to improve the {file_soccer}")
