import os
from bs4 import BeautifulSoup
from steam import Steam
from decouple import config


print("Basic ID checker")
#file_path = input("Enter the location of your username list:\n")
file_path = "usernames.txt"
if not os.path.exists(file_path):
    print("The specified file does not exist.")
    exit()
    
usernames = open(file_path).read().splitlines()

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

available_usernames = []
taken_usernames = []

with open('valid.txt', 'a') as file:
    for i, username in enumerate(usernames, start=1):
        user = steam.users.get_steamid(f"{username}")
        
        print(f"Checked {i}/{len(usernames)}", end='\r')
        #print(f"Available: {len(available_usernames)}", end='\n')
        
        if 'message' in user and user['message'] == "No match":
            available_usernames.append(username)
        else:
            taken_usernames.append(username)
            
    for available in available_usernames:
        file.write(available+"\n")

print("\nAll usernames are checked")
print(f"Usernames Available: {len(available_usernames)} / {len(usernames)}")
print("Available usernames are in the valid text file.")