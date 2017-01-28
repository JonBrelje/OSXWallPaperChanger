import datetime
import subprocess

time = datetime.datetime.now()
hour = time.hour

if hour <= 8:
	subprocess.call(['./change_desktop_background.sh', '/Users/JonBrelje/Pictures/Background Photos/Grand Tetons.jpg'])
elif hour <= 12:
	subprocess.call(['./change_desktop_background.sh', '/Users/JonBrelje/Pictures/Background Photos/great smoky mountains.jpg'])
elif hour <= 16:
	subprocess.call(['./change_desktop_background.sh', '/Users/JonBrelje/Pictures/Background Photos/Mt. Hood.jpg'])
elif hour <= 20:
	subprocess.call(['./change_desktop_background.sh', '/Users/JonBrelje/Pictures/Background Photos/mt hood snow.jpg'])
else:
	subprocess.call(['./change_desktop_background.sh', '/Users/JonBrelje/Pictures/Background Photos/Mt. Hood at Dusk.jpg'])
