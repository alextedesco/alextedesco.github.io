import requests
from bs4 import BeautifulSoup, Comment
import re
import warnings
import datetime
from teams import NFL_TEAMS

# Suppresses Beautiful Soup warnings due to reading HTML as a string instead of a file
warnings.filterwarnings("ignore", category=UserWarning)

def get_roster(team_name):
    '''
    Function that returns a list of an NFL team's roster
    '''
    roster = []
    for abbr, name in NFL_TEAMS.items():
        if name.lower() == team_name.lower():
            team_abbr = abbr
            break

    if team_abbr is None:
        print("Error: Team not found.")
        return []

    # Uses the datetime package to store the current year
    current_year = datetime.datetime.now().year

    # Configures the URL with the team and year
    url = f"https://www.pro-football-reference.com/teams/{team_abbr.lower()}/{current_year}_roster.htm"

    # Sends GET request to the URL
    response = requests.get(url)
    # Checks if the page loaded, if not print error and return empty list
    if response.status_code != 200:
        print("Error: Unable to fetch roster.")
        return []

    # Parses the HTML content using Beautiful Soup package
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all comments in the soup
    comments = soup(text=lambda text: isinstance(text, Comment))
    # Iterate over comments and find the table within them
    for comment in comments:
        
        comment_soup = BeautifulSoup(comment, 'html.parser')
        # Stores the table as a variable
        table = comment_soup.find('table')
        # Checks if the table exists
        if table:
            # Table found within comments
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                # Splits the row at the table cell delimeter
                row_parts = str(row).split('</td><td')

                # Uses regex to find obtain the players name
                name_match = re.search(r'>(.*?)</a>', str(row_parts))
                # Checks if the name exists
                if name_match:
                    # Stores the line with the players name as additional splitting needed
                    player_name = name_match.group(1)
                    # Splits the string in order to store just the name
                    player_name = player_name.split('.htm">')
                    # Stores the player name to a string variable
                    player_name = player_name[1]
                # If the name doesn't exist, it is likely due to the player not
                # having a pro football reference player webpage in their database
                else:
                    # Uses regex to find obtain the players name
                    name_match = re.search(r'data-stat="player">(.*?)<', str(row_parts))
                    # Checks if the name exists
                    if name_match:
                        # Stores the line with the players name as additional splitting needed
                        player_name = name_match.group(1)
                        # Splits the string in order to store just the name
                        player_name = player_name.split("'")
                        # Stores the player name to a string variable
                        player_name = player_name[0]
                    # If all else fails the player's name is set to a blank string.
                    # We should never get here and it is not expected that we do
                    else:
                        player_name = ''
                
                # Uses regex to find obtain the player's name
                position_match = re.search(r'pos">(.*?)\'', str(row_parts))
                # Checks if the position exists
                if position_match:
                    # Stores the position as a string variable
                    player_position = position_match.group(1)

                # Uses regex to find obtain the player's number
                number_match = re.search(r'scope="row">(.*?)</th>', str(row_parts))
                # Checks if the number exists
                if number_match:
                    # Stores the player number as a string variable
                    player_number = number_match.group(1)
                    # If the player has not been assigned a number by the franchise yet
                    # Then his number does not exist (DNE)
                    if player_number == "":
                        player_number = "DNE"
                
                # Stores the players data into a dictionary which is later added to the roster list
                player_data = {
                    'name': player_name,
                    'position': player_position,
                    'number': player_number
                }

                # Adds player to the roster
                roster.append(player_data)
    return roster


def main ():
    '''
    Main function that takes inputs from the terminal and 
    prints out the roster to standard output
    '''
    input_team = input ("Enter Team Name: ")
    input_position = input ("Enter Position or 'All' for all: ")
    roster = get_roster (input_team)

    for player in roster:
        name = player['name']
        position = player['position']
        number = player['number']

        if input_position == "All":
            print (number, name, position)
        elif input_position != position:
            continue
        else:
            if position == input_position:
                print (number, name, position)

    print("\u001b[31m" + "DISCLAIMER" + "\u001b[37m" + ": If you are wondering why some 2023 rookies aren't included it is because they have not signed their rookie contract and are not officially on the team yet")

if __name__ == "__main__":
    main ()