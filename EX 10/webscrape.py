# Grace Foster
# ITP 100-01
# EXERCISE: 09
# webscrape.py
# ----------------------------------------------------------------

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://www.centralvirginia.edu"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

linz = "---" * 35
images = soup.find_all('img')
for img in images:
    print(img["src"])
print(linz)

linz = "---" * 35
for img in images:
    if re.search("KenArt", img["src"]):
        print(img["src"])
print(linz)
print("The Program Has Terminated Normally!")
