# how to find the title using regular expressions
import re
from urllib.request import urlopen
# * make sure to always use the urrlib.request *
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf=8")
# print(html)
# -------
pattern = "<title.*?>.*</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
print(title)

title = re.sub("<.*?>", "", title)
print(title)
