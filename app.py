import os
from random import randint
from datetime import datetime, timedelta

# --- SET YOUR CONFIGURATION HERE ---
start_date = datetime(2025, 1, 8)
end_date = datetime(2025, 1, 12)
# ------------------------------------

# Loop through each day in your specified range
delta = end_date - start_date
for i in range(delta.days + 1):
    current_date = start_date + timedelta(days=i)
    
    # For each day, decide how many commits to make (from 1 to 80)
    num_commits = randint(1, 80)
    
    for j in range(num_commits):
        # Format the date for the git commit command
        d = current_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Make a change to the file
        with open('file.txt', 'a') as file:
            file.write(f"{d}\n") # Appending the date string itself
        
        # Git commands
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "commit"')

# Push all the created commits at the very end
# Note: I corrected the typo from 'orgin' to 'origin'
print("Pushing all commits to the remote repository...")
os.system('git push -u origin main')

print("Done!")