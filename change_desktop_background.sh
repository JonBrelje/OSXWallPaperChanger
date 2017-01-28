#!/bin/sh

# First argument must be absolute file path to desired image
image_path=$1
echo $
echo $1
#Call apple script to change the background image of each desktop
osascript << EOF
tell application "System Events"
set desktopCount to count of desktops
repeat with desktopNumber from 1 to desktopCount
tell desktop desktopNumber
set picture to POSIX file "$1"
end tell
end repeat
end tell
EOF
