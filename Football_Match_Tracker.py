import sys
from datetime import datetime

# -----------------------------------------------------------------------------------------------------------

print("\nWelcome to the football match tracker app!").upper()
fav_team = input("Please enter the team you support: ")
print("Good choice! \n")

# -----------------------------------------------------------------------------------------------------------

class Match:
    def __init__(self, date, homeTeam, awayTeam, homeScore, awayScore, stadium, distance, result, rating):
        self.date = date
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.stadium = stadium
        self.distance = distance
        self.result = result
        self.rating = rating
        
# -----------------------------------------------------------------------------------------------------------

def display_match(match):
    data = match.strip().split("|")

    print(f"Date: {data[0]}")
    print(f"Match: {data[1]} {data[3]}-{data[4]} {data[2]}")
    print(f"Travel: {data[6]} miles to {data[5]} stadium")
    print(f"Team Rating: {data[8]}")
    print("\n-------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------

def simple_display(match):
    data = match.strip().split("|")

    print(f"Match: {data[0]}: {data[1]} {data[3]}-{data[4]} {data[2]}")
    print("\n-------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------

def add_match():
    date = input("Please enter the date in the form dd/mm/yyyy: ")
    homeT = input("Please enter the home team: ")
    awayT = input("Please enter the away team: ")
    homeS = int(input("Please enter the home score: "))
    awayS = int(input("Please enter the away score: "))
    stadium = input("Please enter the stadium visited: ")
    distance = float(input("Please enter the distance travelled to the stadium in miles: "))
    result = input("Did your team win, lose or draw: ").lower()
    rating = float(input("please rate your team's performance from 1 to 10: "))


    match = Match(date, homeT, awayT, homeS, awayS, stadium, distance, result, rating)
    with open("matches_Tracker.txt", "a") as f:
        f.write(
            f"{match.date}|{match.homeTeam}|{match.awayTeam}|"
            f"{match.homeScore}|{match.awayScore}|"
            f"{match.stadium}|{match.distance}|"
            f"{match.result}|{match.rating}\n"
        )

    print("\n---- Match saved successfully! ----")

# -----------------------------------------------------------------------------------------------------------

def view_match():
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()

    for match in matches:
        #data = match.strip().split("|")
        display_match(match)

# -----------------------------------------------------------------------------------------------------------

def sort_match():
    print("1. Date Asc \n2. Date Desc\n3. Rating Asc \n4. Rating Desc \n5. Distance Asc \n6. Distance Desc \n")
    sort_by = int(input("Please select a sorting option by typing the relevant number: "))

    match sort_by:
        case 1:
            print("\n---- Date Ascending ----\n")
            sort_date(False)
        case 2:
            print("\n---- Date Descending ----\n")
            sort_date(True)
        case 3:
            print("\n---- Rating Ascending ----\n")
            sort_rating(False)
        case 4:
            print("\n---- Rating Descending ----\n")
            sort_rating(True)
        case 5:
            print("\n---- Distance Ascending ----\n")
            sort_distance(False)
        case 6:
            print("\n---- Distance Descending ----\n")
            sort_distance(True)
        case _:
            print("\n---- Invalid entry ----")

# -----------------------------------------------------------------------------------------------------------

def sort_date(reverse_order):
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()

    matches.sort(key=lambda match: datetime.strptime(match.split("|")[0], "%d/%m/%Y"), reverse=reverse_order)

    for match in matches:
        simple_display(match)

# -----------------------------------------------------------------------------------------------------------

def sort_rating(reverse_order):
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()
    matches.sort(key=lambda match: float(match.split("|")[8]),reverse=reverse_order)

    for match in matches:
        display_match(match)

# -----------------------------------------------------------------------------------------------------------

def sort_distance(reverse_order):
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()
    matches.sort(key=lambda match: float(match.split("|")[6]),reverse=reverse_order)
    
    for match in matches:
        display_match(match)

# -----------------------------------------------------------------------------------------------------------

#def search_match():


# -----------------------------------------------------------------------------------------------------------

#def view_stats():


# -----------------------------------------------------------------------------------------------------------

def edit_match():
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()
        
    for match in matches:
        simple_display(match)

    edit = input("\nPlease enter the date of the game you want to delete (in the form dd/mm/yyyy): ")
    
    print("\n1. Date \n2. Home Team  \n3. Away Team \n4. Home Score \n5. Away Score \n6. Stadium \n7. Distance \n8. Result \n9. Rating \n")
    change = int(input("Please select the variable you would like to change by typing the relevant number: "))

    for i in range(len(matches)):
        if matches[i].startswith(edit):
            data = matches[i].strip().split("|")

            if change in [4,5,7,9]:
                new_value = int(input("Enter the new data: "))
            else:
                new_value = input("Enter the new data: ")

            data[change - 1] = str(new_value)
            matches[i] = "|".join(data) + "\n"

            break
            
    with open("matches_Tracker.txt", "w") as f:
        f.writelines(matches)


    print("\n---- Match edited successfully! ----")

# -----------------------------------------------------------------------------------------------------------

def delete_match():
    with open("matches_Tracker.txt", "r") as f:
        matches = f.readlines()
        
    for match in matches:
        simple_display(match)

    delete = input("\nPlease enter the date of the game you want to delete (in the form dd/mm/yyyy): ")

    for i in range(len(matches)):
        if matches[i].startswith(delete):
            del matches[i]

        break

    with open("matches_Tracker.txt", "w") as f:
        f.writelines(matches)

    print("\n---- Match deleted successfully! ----")

# -----------------------------------------------------------------------------------------------------------

while True:

    print("1. Add Match \n2. View Matches \n3. Sort Matches \n4. Search Matches \n5. View Statistics \n6. Edit Match \n7. Delete Match \n8. Exit Application \n")
    functions = int(input("Please select an option by typing the relevant number: "))

    match functions:
        case 1:
            print("\n---- Create a new match entry! ----\n")
            add_match()
        case 2:
            print("\n---- View match entries ----\n")
            view_match()
        case 3:
            print("\n---- Sort match entries ----\n")
            sort_match()
        case 4:
            print("Search")
            #search_match()
        case 5:
            print("stats")
            #view_stats()
        case 6:
            print("\n---- Edit match entries ----\n")
            edit_match()
        case 7:
            print("\n---- Delete match entries ----\n")
            delete_match()
        case 8:
            print("\n---- Thankyou, Goodbye! ----\n")
            sys.exit()
        case _:
            print("\n---- Invalid entry ----")



