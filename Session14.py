songs=[
    "kesariya",
    "apna bana le",
    "chaleya",
    "bairan",
    "tum hi ho"
]
with open("plylist.txt","w")as file:
    for song in songs:
        file.write(song +"\n")

print("songs written succesfully")

#Q2
with open("plylist.txt","r")as file:
    songs=file.readlines()

print("my playlist")
for song in songs:
    print(song.strip().upper())

#Q3
import csv 
with open("ipl_matches.csv","r")as file:
    reader=csv.DictReader(file)

for row in reader:
    print("match",row["match_id"],"winner:",row["winner"])

#Q4
import json
with open("movies.json","r")as file:
    movies=json.load(file)

for movie in movies:
    print("title:",movie["title"])
    print("rating:",movie["rating"])
    print()

#Q5
from pathlib import Path
import json
file_path = Path("my_fav_apps.json")
if not file_path.exists():
    apps = [
        {
            "name": "Instagram",
            "category": "Social Media"
        },
        {
            "name": "Zomato",
            "category": "Food Delivery"
        },
        {
            "name": "Paytm",
            "category": "Finance"
        }
    ]

    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)
    print("my_fav_apps.json created successfully!")
else:
    print("my_fav_apps.json already exists.")

