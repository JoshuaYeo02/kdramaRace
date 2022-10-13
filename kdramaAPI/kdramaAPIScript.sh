#!/usr/bin/bash

python3 kdramaAPI.py &>/dev/null &
kdramaAPIPID=$!
echo "KDRAMA API is running"
ngrok http 7777 &>/dev/null &
echo "ngrok is running"
sleep 1
curl -s http://127.0.0.1:4040/api/tunnels | grep "http://[^,.]*.ngrok.io" -oh
read -p "Press any key to close" -n1 -s
echo ""

kill -9 $(pgrep ngrok)
kill -9 $kdramaAPIPID
