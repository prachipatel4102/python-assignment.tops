#Q1
import playlist_utilis
import math
result=math.sqrt(255)
print("square root of 255 is",result)

#Q2
import os
folder_name="Mydownload"
os.makedirs(folder_name,exist_ok=True)
folder_path=os.path.abspath(folder_name)
print("folder created successfully")
print("absolute path",folder_path)

#Q3
from datetime import datetime
current_datetime=datetime.now()
formmated_datetime=current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("current date and time",formmated_datetime)

#Q4
import playlist_utilis
playlist=[]
playlist_utilis.add_song(playlist,"Kesariya")
playlist_utilis.add_song(playlist,"bairan")
playlist_utilis.add_song(playlist,"chaleya")
print("final playlist")
print(playlist)

#Q5
import requests
print("requests version",requests.__version__)