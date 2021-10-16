import random as rng
import time

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

    quarterone_score_one = rng.randint(0, 17)
    quarterone_score_two = rng.randint(0, 17)
    print(f"{rng_team_one} scored {quarterone_score_one}, and {rng_team_two} scored {quarterone_score_two} in the first quarter.")
    time.sleep(2)
    quartertwo_score_one = rng.randint(0, 17)
    quartertwo_score_two = rng.randint(0, 17)
    print(f"{rng_team_one} scored {quartertwo_score_one}, and {rng_team_two} scored {quartertwo_score_two} in the second quarter.")
    print("Halftime!")
    time.sleep(2)
    quarterthree_score_one = rng.randint(0, 17)
    quarterthree_score_two = rng.randint(0, 17)
    print(f"{rng_team_one} scored {quarterthree_score_one}, and {rng_team_two} scored {quarterthree_score_two} in the third quarter.")
    time.sleep(2)
    quarterfour_score_one = rng.randint(0, 17)
    quarterfour_score_two = rng.randint(0, 17)

    first_total = 0
    second_total = 0
    first_total = quarterone_score_one + quartertwo_score_one + quarterthree_score_one + quarterfour_score_one
    second_total = quarterone_score_two + quartertwo_score_two + quarterthree_score_two + quarterfour_score_two
    print(f"{rng_team_one} scored {first_total}, and {rng_team_two} scored {second_total}!")
    if first_total > second_total:
        if first_total == 0:
            print(f"{rng_team_two} had a shutdown against {rng_team_one}!")
        print(f"{rng_team_one} wins!")
    elif first_total < second_total:
        if first_total == 0:
            print(f"{rng_team_two} had a shutdown against {rng_team_one}!")
        print(f"{rng_team_two} wins!")

def main():
    choice = input("Would you like to play a game? (y/n) ")
    if choice == "y":
        play_game()
    else:
        print("Bye!")

main()
