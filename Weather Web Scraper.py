import requests
import pandas as pd
import matplotlib.pyplot as pyp
from bs4 import BeautifulSoup
page = requests.get("https://weather.gc.ca/canada_e.html")
soup = BeautifulSoup(page.content, 'html.parser')
items = Table.select("div td")  
cities = [] 
temperatures = []
count = 0 
for element in items: 
    if count % 3 == 0:
        cities.append(element.get_text()) #city
    elif count % 3 == 2:
        temperatures.append(element.get_text()) 
    count += 1
weather = pd.DataFrame({"City": cities, "Temperature(C)": temperatures})
