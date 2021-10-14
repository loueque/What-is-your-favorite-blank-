import random as rng

organizer = "NFL"

divisions = {
    "AFC": {
        "North": {
            "CIN": "Cincinnati Bengals",
            "CLE": "Cleveland Browns",
            "PIT": "Pittsburgh Steelers",
            "BAL": "Baltimore Ravens",
        },

        "East": {
            "NE": "New England Patriots",
            "BUF": "Buffalo Bills",
            "MIA": "Miami Dolphins",
            "NYJ": "New York Jets",
        },

        "South": {
            "HOU": "Houston Texans",
            "IND": "Indianapolis Colts",
            "JAX": "Jacksonville Jaguars",
            "TEN": "Tennessee Titans",
        },

        "West": {
            "LAC": "Los Angeles Chargers",
            "OAK": "Oakland Raiders",
            "DEN": "Denver Broncos",
            "KC": "Kansas City Chiefs",
        }
    },

    "NFC": {
        "North": {
            "GB": "Green Bay Packers",
            "MIN": "Minnesota Vikings",
            "DET": "Detroit Lions",
            "CHI": "Chicago Bears",
        },

        "East": {
            "NYG": "New York Giants",
            "PHI": "Philadelphia Eagles",
            "WAS": "Washington Redskins",
            "DAL": "Dallas Cowboys",
        },

        "South": {
            "ATL": "Atlanta Falcons",
            "CAR": "Carolina Panthers",
            "NO": "New Orleans Saints",
            "TB": "Tampa Bay Buccaneers",
        },

        "West": {
            "ARI": "Arizona Cardinals",
            "LAR": "Los Angeles Rams",
            "SF": "San Francisco 49ers",
            "SEA": "Seattle Seahawks",
        },
    }
}

def print_team():
    rng_conf = rng.choice(list(divisions.keys()))
    rng_div = rng.choice(list(divisions[rng_conf].keys()))

    return rng_conf, rng_div

print(print_team())

def play_game():
    # using print_team(), chose out a random team in the conference and division
    conf, div = print_team()
    rng_team_one = rng.choice(list(divisions[conf][div].values()))
    rng_team_conf_one = rng.choice(list(divisions[conf].values()))
    rng_team_two = rng.choice(list(divisions[conf][div].values()))
    rng_team_conf_two = rng.choice(list(divisions[conf].values()))

    # print the teams
    print(f"{rng_team_one} vs. {rng_team_two}")
    print("Kickoff!")

    score_one = rng.randint(0, 52)
    score_two = rng.randint(0, 52)
    print(f"{rng_team_one} scored {score_one}, and {rng_team_two} scored {score_two}")
    if score_one > score_two:
        if score_two == 0:
            print(f"{rng_team_two} from {rng_team_conf_two} had a shutdown against {rng_team_one} from {rng_team_conf_one}!")
        print(f"{rng_team_one} wins!")
    elif score_one < score_two:
        if score_one == 0:
            print(f"{rng_team_two} from {rng_team_conf_two} had a shutdown against {rng_team_one} from {rng_team_conf_one}!")
        print(f"{rng_team_two} wins!")

def main():
    choice = input("Would you like to play a game? (y/n) ")
    if choice == "y":
        play_game()
    else:
        print("Bye!")

main()
