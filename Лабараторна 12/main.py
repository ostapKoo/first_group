import json

def add_team(data):
    print("Додати нову команду:")
    Name = input("Назва команди:")
    Score = int(input("Набрані очки команди:"))
    data.append({"Назва": Name, "Очки": Score})
    return data

def find_team(teams, team_name):
    for index, team in enumerate(teams):
        if team["Назва"] == team_name:
            return index, team
    return None, None

def find_teams(teams, new_team_score):
    all_teams = [(team["Назва"], team["Очки"]) for team in teams]
    all_teams.append(("Нова команда", new_team_score))
    sorted_teams = sorted(all_teams, key=lambda x: x[1], reverse=True)
    new_team_position = sorted_teams.index(("Нова команда", new_team_score)) + 1
    lesser_teams = [team for team in sorted_teams[:new_team_position-1]]

    return new_team_position, lesser_teams

teams = [
    {"Назва": "Команда 1", "Очки": 90},
    {"Назва": "Команда 2 ", "Очки": 81},
    {"Назва": "Команда 3", "Очки": 78},
    {"Назва": "Команда 4", "Очки": 92},
    {"Назва": "Команда 5 ", "Очки": 84},
    {"Назва": "Команда 6", "Очки": 76},
    {"Назва": "Команда 7", "Очки": 93},
    {"Назва": "Команда 8 ", "Очки": 84},
    {"Назва": "Команда 9", "Очки": 79}
]

with open("lab12.json", "wt") as file:
    json.dump(teams, file)

while True:
    print("Оберіть:\n 1 - Додати нову команду \n 2 - Показати команди \n 3 - Знайти команду\n 0 - Вийти")
    choice = input("Ваш вибір:  ")
    if choice == "1":
        with open("lab12.json", "rt") as file:
            teams = json.load(file)
        teams = add_team(teams)
        teams = sorted(teams, key=lambda x: x['Очки'], reverse=True)  # Сортування за кількістю очок
        with open("lab12.json", "wt") as file:
            json.dump(teams, file)
    elif choice == "2":
        with open("lab12.json", "rt") as file:
            teams = json.load(file)
        print("Команди:")
        for team in teams:
            print(f"{team['Назва']}: {team['Очки']}")
    elif choice == "3":
        with open("lab12.json", "rt") as file:
            teams = json.load(file)
        team_name = input("Введіть назву команди:")
        index, team = find_team(teams, team_name)
        if team:
            print(f"Команда '{team_name}' має позицію: {index + 1}")
            print("Команди з більшою кількістю очок:")
            new_team_position, lesser_teams = find_teams(teams, team["Очки"])
            for lesser_team_name, score in lesser_teams:
                print(f"{lesser_team_name}: {score}")
        else:
            print(f"Команда '{team_name}' не знайдена.")
    elif choice == "0":
        break
