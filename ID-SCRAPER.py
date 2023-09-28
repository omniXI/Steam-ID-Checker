import requests
import os
from bs4 import BeautifulSoup

print('Basic Steam ID Checker')
#file_path = input('Enter the location of your username list:\n')
file_path = "usernames.txt"

# This line of code checks if the file exists before continuing
if not os.path.exists(file_path):
    print('The specified file does not exist.')
    exit()

available_usernames = []
taken_usernames = []

usernames = open(file_path).read().splitlines()
invalid_indicator = "The specified profile could not be found."

with open('valid.txt', 'a') as file:
    for username in usernames:
        #This goes through each username in file_path
        url = 'https://steamcommunity.com/id/' + username
        
        #Sends a GET request to the URL.
        response = requests.get(f'{url}', headers={'Accept': 'text/html'})
        
        #Checks if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to fetch data for {username}.")

        found = soup.body.find_all(string=invalid_indicator)
        
        if found:
            available_usernames.append(username)
            file.write(username+"\n")
        else:
            taken_usernames.append(username)
            