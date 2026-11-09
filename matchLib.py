# -----------------------------------------------------------------------------------------------------------

def home_or_away(data, fav_team):
    if data[1] == fav_team:
        return "Home"
    elif data[2] == fav_team:
        return "Away"
    else:
        return "Unknown"


# -----------------------------------------------------------------------------------------------------------

def home_vs_away(matches):
    home_games = 0
    away_games = 0

    for match in matches:
        data = match.strip().split("|")
        location = home_or_away(data)

        if location == "Home":
            home_games += 1
        elif location == "Away":
            away_games += 1
        else:
            return "Unknown"

    return home_games, away_games
    
# -----------------------------------------------------------------------------------------------------------

def win_percent(matches):
    no_of_wins = 0
    for match in matches:
        data = match.strip().split("|")
        if data[7].lower() == "win":
            no_of_wins += 1
    win_percent = (no_of_wins / len(matches)) * 100
    
    return round(win_percent, 1), no_of_wins
    
# -----------------------------------------------------------------------------------------------------------

def total_goals(matches):
    tot_goals = 0
    tot_team_goals = 0
    
    for match in matches:
        data = match.strip().split("|")
        location = home_or_away(data)

        goals_in_game = int(data[3]) + int(data[4])
        tot_goals += goals_in_game
        
        if location == "Home":
            tot_team_goals += int(data[3])
        elif location == "Away":
            tot_team_goals += int(data[4])
        else:
            continue

    average_goals = (tot_team_goals / tot_goals) * 100
    
    return tot_goals, tot_team_goals, round(average_goals, 1)
    
# -----------------------------------------------------------------------------------------------------------

def average_rating(matches):
    total_rating = 0

    for match in matches:
        data = match.strip().split("|")
        total_rating += float(data[8])

    avg_rating = total_rating / len(matches)

    return round(avg_rating, 1)
# -----------------------------------------------------------------------------------------------------------

def stadiums_visited(matches):
    stadiums = {}

    for match in matches:
        data = match.strip().split("|")

        stadium = data[5]

        if stadium in stadiums:
            stadiums[stadium] += 1
        else:
            stadiums[stadium] = 1
            
    return sorted(stadiums.items(), key=lambda item:item[1], reverse = True)

# -----------------------------------------------------------------------------------------------------------

def total_mileage(matches):
    total_miles = 0
    
    for match in matches:
        data = match.strip().split("|")
        total_miles += float(data[6])
        
    avg_miles = total_miles / len(matches)
    
    return total_miles, round(avg_miles, 1)

# -----------------------------------------------------------------------------------------------------------

