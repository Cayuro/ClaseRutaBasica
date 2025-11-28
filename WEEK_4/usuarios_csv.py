import csv

archivo = "usuarios.csv"
archivo_f= "futbol.csv"
encabezados = ["User", "Password"]
usuarios = [{"User": "Andres", "Password": "1234"},{"User": "Maria","Password": "abcd"},{"User": "Pedro", "Password": "1"}]
encabezados_equip = ["Soccer_team", "PJ", "PG", "PE", "PP", "Pts"]
soccer_teams = [
    {"Soccer_team": "Barcelona", "PJ": 10, "PG": 7, "PE": 2, "PP": 1, "Pts": 23},
    {"Soccer_team": "Real Madrid", "PJ": 10, "PG": 6, "PE": 3, "PP": 1, "Pts": 21},
    {"Soccer_team": "Atlético Madrid", "PJ": 10, "PG": 5, "PE": 4, "PP": 1, "Pts": 19},
    {"Soccer_team": "Sevilla", "PJ": 10, "PG": 4, "PE": 3, "PP": 3, "Pts": 15},
    {"Soccer_team": "Valencia", "PJ": 10, "PG": 3, "PE": 4, "PP": 3, "Pts": 13}
]

def downloading_csv(archivo):
    with open(archivo, "r") as file:
        reader = csv.DictReader(file)
        usuarios = list(reader)
    return usuarios

def preload_user_csv(archivo,encabezados, usuarios):
    with open(archivo, "w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(encabezados)
        for user in usuarios:
            writer.writerow([user["User"],user["Password"]])

def preload_soccer(archivo,encabezados_equip, soccer_teams):
    with open(archivo, "w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(encabezados_equip)
        for team in soccer_teams:
            writer.writerow([team["Soccer_team"], team["PJ"], team["PG"], team["PE"], team["PP"], team["Pts"]])

def save_csv_soccer(soccer_teams):
    with open("futbol.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(encabezados_equip)
        for team in soccer_teams:
            writer.writerow([team["Soccer_team"], team["PJ"], team["PG"], team["PE"], team["PP"], team["Pts"]])

preload_soccer(archivo_f,encabezados_equip, soccer_teams)

