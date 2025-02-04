#!/bin/bash

rsync -av --delete "/path/to/markdown/directory/" "/path/to/blog/directory/content/posts/"
sleep 2
echo "source is coppied now"

cd /path/to/blog/directory/

hugo server -t terminal &
PID=$!
sleep 3
kill $PID
echo "the website was build"

rsync -av "/path/to/blog/directory/public/" "/path/to/GitHub/directory/"
sleep 3
echo "The website is coppied now"

cd /path/to/GitHub/directory/

python3 /path/to/correct.py
sleep 2
python3 /path/to/correct-link.py
sleep 2
echo "All error's are corrected now"

git add .
sleep 1
git commit -m "update"
sleep 1
git push
echo "Your blog is updated now."

cd