import random as rng

organizer = "NFL"

# table of NFl teams and division title
# NFL teams and division title

teams = {
    "ARI": "Arizona Cardinals",
    "ATL": "Atlanta Falcons",
    "BAL": "Baltimore Ravens",
    "BUF": "Buffalo Bills",
    "CAR": "Carolina Panthers",
    "CHI": "Chicago Bears",
    "CIN": "Cincinnati Bengals",
    "CLE": "Cleveland Browns",
    "DAL": "Dallas Cowboys",
    "DEN": "Denver Broncos",
    "DET": "Detroit Lions",
    "GB": "Green Bay Packers",
    "HOU": "Houston Texans",
    "IND": "Indianapolis Colts",
    "JAX": "Jacksonville Jaguars",
    "KC": "Kansas City Chiefs",
    "LAC": "Los Angeles Chargers",
    "LAR": "Los Angeles Rams",
    "MIA": "Miami Dolphins",
    "MIN": "Minnesota Vikings",
    "NE": "New England Patriots",
    "NO": "New Orleans Saints",
    "NYG": "New York Giants",
    "NYJ": "New York Jets",
    "OAK": "Las Vegas Raiders",
    "PHI": "Philadelphia Eagles",
    "PIT": "Pittsburgh Steelers",
    "SF": "San Francisco 49ers",
    "SEA": "Seattle Seahawks",
    "TB": "Tampa Bay Buccaneers",
    "TEN": "Tennessee Titans",
    "WAS": "Washington Redskins",
}

def play_game():
    rng_team = rng.choice(list(teams.keys()))
    rng_team_one = teams[rng_team]
    rng_team_ = rng.choice(list(teams.keys()))
    rng_team_two = teams[rng_team_]
    print(f"{rng_team_one} vs {rng_team_two}")
    print("Kickoff!")
    score_one = rng.randint(0, 70)
    score_two = rng.randint(0, 70)
    print(f"{rng_team_one} scored {score_one}, and {rng_team_two} scored {score_two}")
    if score_one > score_two:
        if score_two == 0:
            print(f"{rng_team_two} had a shutdown against {rng_team_one}!")
        print(f"{rng_team_one} wins!")
    elif score_one < score_two:
        if score_one == 0:
            print(f"{rng_team_two} had a shutout against {rng_team_one}!")
        print(f"{rng_team_two} wins!")

def main():
    choice = input("Would you like to play a game? (y/n) ")
    if choice == "y":
        play_game()
    else:
        print("Bye!")

main()
