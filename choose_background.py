import datetime
import subprocess

time = datetime.datetime.now()
hour = time.hour

if hour <= 8:
	subprocess.call(["""./change_desktop_background.sh '/Users/JonBrelje/Pictures/Grand Tetons.jpg'"""])
elif hour <= 16:
	subprocess.call(["""./change_desktop_background.sh '/Users/JonBrelje/Pictures/Mt. Hood.jpg'"""])
else:
	subprocess.call(["""./change_desktop_background.sh '/Users/JonBrelje/Pictures/Mt. Hood at Dusk.jpg'"""])