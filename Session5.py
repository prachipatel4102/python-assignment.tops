#Q1 Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.
playlist_ids=[101,102,103,104,105]
print(playlist_ids)

#Q2 Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>
playlist_ids=[101,102,103,104,105]
playlist_ids.append(106)
playlist_ids.extend([107,108])
print(playlist_ids)

#Q3 Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.
playlist_ids=[101,102,103,104,105,106,107,108]
removed_ids=playlist_ids.pop()
print("removed id:",removed_ids)
print("remaining playlist id :",playlist_ids)

#Q4 Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>
# insta_filters= ("Clarendon", "Juno", "Lark", "Valencia")
# insta_filters[0]="Gingham"
# print(insta_filters)

#Q5 Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.
recent_Zomato_order=["Pizza","burger","garlic bread"]
fixed_ipl_team=("Chennai super kings",
                "Royal challengers bengaluru,"
                "Gujarat titans",
                "Mumbai indians")
print("Recent orders:",recent_Zomato_order)
print("Ipl team:",fixed_ipl_team)
# Use List when data can be added, removed, or modified.
# Use Tuple when data is fixed and should not be changed.