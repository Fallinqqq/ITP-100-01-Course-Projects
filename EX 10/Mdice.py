# importing mechanicalsoup to show the sites API Dice
import mechanicalsoup
browser = mechanicalsoup.Browser()

# -------

page = browser.get("http://olympus.realpython.org/login")
tag = page.soup.select("#result")[0]
result = tag.text
print(f"The result of your dice roll is: {result}")
# ------

"""import time
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    if 1 < 3:
        time.sleep(5)
"""""
