from flask import *
import json, time
# bypassing cloudflare anti-bot
import cloudscraper

from kdramaAPIUtils import search_func, fetch_func



r = fetch_func(query=f"people/13855-kim-se-jung", t="person")
print(r)

