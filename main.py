import random as rng
import time

class Team:
    global organizer
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

    def __init__(self):
        pass

    def choose_team(self):
        rng_conf = rng.choice(list(self.divisions.keys()))
        rng_div = rng.choice(list(self.divisions[rng_conf].keys()))

        return rng_conf, rng_div

    def setMatch(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def getMatch(self):
        return self.team_one, self.team_two

def play_game():
    teamClass = Team()
    conf, div = teamClass.choose_team()

    # rng_team_one = rng.choice(list(teamClass.divisions[conf][div].values()))
    rng_team_conf_one = rng.choice(list(teamClass.divisions[conf].values()))
    rng_team_one = rng.choice(list(rng_team_conf_one))
    # rng_team_two = rng.choice(list(teamClass.divisions[conf][div].values()))
    rng_team_conf_two = rng.choice(list(teamClass.divisions[conf].values()))
    rng_team_two = rng.choice(list(rng_team_conf_two))

    print(f"{rng_team_one} vs. {rng_team_two}")
    print("Kickoff!")

    quarterone_score_one = rng.randint(0, 10)
    quarterone_score_two = rng.randint(0, 10)
    print(f"{rng_team_one} scored {quarterone_score_one}, and {rng_team_two} scored {quarterone_score_two} in the first quarter.")
    time.sleep(2)
    quartertwo_score_one = rng.randint(0, 20)
    quartertwo_score_two = rng.randint(0, 20)
    print(f"{rng_team_one} scored {quartertwo_score_one}, and {rng_team_two} scored {quartertwo_score_two} in the second quarter.")
    print("\nHalftime!\n")
    time.sleep(2)
    quarterthree_score_one = rng.randint(0, 10)
    quarterthree_score_two = rng.randint(0, 10)
    print(f"{rng_team_one} scored {quarterthree_score_one}, and {rng_team_two} scored {quarterthree_score_two} in the third quarter.")
    time.sleep(2)
    quarterfour_score_one = rng.randint(0, 20)
    quarterfour_score_two = rng.randint(0, 20)
    print(f"{rng_team_one} scored {quarterfour_score_one}, and {rng_team_two} scored {quarterfour_score_two} in the fourth quarter.")

    first_total = 0
    second_total = 0
    first_total = quarterone_score_one + quartertwo_score_one + quarterthree_score_one + quarterfour_score_one
    second_total = quarterone_score_two + quartertwo_score_two + quarterthree_score_two + quarterfour_score_two
    print(f"FINAL: {rng_team_one} scored {first_total}, and {rng_team_two} scored {second_total}!")
    if first_total > second_total:
        if first_total == 0:
            print(f"{rng_team_two} had a shutdown against {rng_team_one}!")
        print(f"{rng_team_one} wins!")
    elif first_total < second_total:
        if first_total == 0:
            print(f"{rng_team_two} had a shutdown against {rng_team_one}!\n")
        print("\n"f"{rng_team_two} wins!")

def play_randomized_game():
    teamClass = Team()
    conf, div = teamClass.choose_team()

    rng_team_conf_one = rng.choice(list(teamClass.divisions[conf].values()))
    rng_team_one = rng.choice(list(rng_team_conf_one))
    rng_team_conf_two = rng.choice(list(teamClass.divisions[conf].values()))
    rng_team_two = rng.choice(list(rng_team_conf_two))

    print(f"{rng_team_one} vs. {rng_team_two}")

def main():
    choice = input("Would you like to play a game? (y/n)\n")
    if choice == "y":
        type_of_game = input("Would you like a randomized team, or randomized game? (r/g)\n")
        if type_of_game == "r":
            play_randomized_game()
        elif type_of_game == "g":
            play_game()
    else:
        print("Bye!")

main()
