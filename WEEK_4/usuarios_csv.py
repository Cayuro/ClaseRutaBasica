import csv

archivo = "usuarios.csv"
archivo_f= "futbol.csv"
encabezados = ["User", "Password"]
usuarios = [{"User": "Andres", "Password": "1234"},{"User": "Maria","Password": "abcd"},{"User": "Pedro", "Password": "1"}]
encabezados_equip = ["Soccer_team", "PJ", "PG", "PE", "PP", "GF", "GC", "Pts"]
soccer_teams = [
    {"Soccer_team": "Barcelona", "PJ": 10, "PG": 7, "PE": 2, "PP": 1, "GF": 20, "GC": 8, "Pts": 23},
    {"Soccer_team": "Real Madrid", "PJ": 10, "PG": 6, "PE": 3, "PP": 1, "GF": 18, "GC": 10, "Pts": 21},
    {"Soccer_team": "Atlético Madrid", "PJ": 10, "PG": 5, "PE": 4, "PP": 1, "GF": 15, "GC": 7, "Pts": 19},
    {"Soccer_team": "Sevilla", "PJ": 10, "PG": 4, "PE": 3, "PP": 3, "GF": 12, "GC": 11, "Pts": 15},
    {"Soccer_team": "Valencia", "PJ": 10, "PG": 3, "PE": 4, "PP": 3, "GF": 10, "GC": 12, "Pts": 13}
]

def cargar_csv(archivo,encabezados, usuarios):
    with open(archivo, "w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(encabezados)
        for user in usuarios:
            writer.writerow([user["User"],user["Password"]])

def cargar_csv_futbol(archivo,encabezados_equip, soccer_teams):
    with open(archivo, "w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(encabezados_equip)
        for team in soccer_teams:
            writer.writerow([team["Soccer_team"], team["PJ"], team["PG"], team["PE"], team["GF"], team["GC"], team["Pts"]])

cargar_csv_futbol(archivo_f,encabezados_equip, soccer_teams)

