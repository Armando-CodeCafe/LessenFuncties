import requests as rq
import json
title = input("Title ")
key = "dd557394"
url = f"https://www.omdbapi.com/?apikey={key}&t={title}"

result = rq.get(url)
with open("test.json","w") as file:

    file.write(str(result.json()))



