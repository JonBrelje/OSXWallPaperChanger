 #!/usr/bin/env bash
echo -n "Enter the path to a picture > "
read picture_path
sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = $picture_path";
killall Dock;