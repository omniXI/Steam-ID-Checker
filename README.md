# Steam-ID-Checker

Please don't use this, it's trash. I'm practicing Python right now.

ID-API.py -
This script uses the Steam API and tells if a username is available or taken

1. You provide a list of usernames in a text file called "usernames.txt."
2. The script reads this list and uses the Steam API to check each username.
3. For each username, it tells you whether it's "available" (not taken) or "taken" (already in use on Steam).
4. It prints the results, so you can quickly see which usernames are available for you to use on Steam.

ID-SCRAPER.py -
This script uses a scraping method to tell if a username is available or not by reading a text on steam's website.

1. You provide a list of usernames in a text file, which you specify when you run the script.
2. The script reads this list and checks each username by attempting to access their Steam profiles on the Steam Community website.
3. For each username, it tells you whether it's "taken" (the Steam profile exists) or "not taken" (the Steam profile doesn't exist).
4. It prints the results, allowing you to quickly see which usernames are available on Steam and which ones are already in use.


### Will implement multiprocessing on both tools soon
