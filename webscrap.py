# Extracting data from a website programmatically.

# Importing the modules
from bs4 import BeautifulSoup
import requests, openpyxl

# To save the scraped data in an excel sheet
excel = openpyxl.Workbook()
sheet = excel.active

sheet.title = 'Top Batsmen'

sheet.append(['rank', 'name', 'matches', 'inns', 'runs', 'avg', 'strike_rate', 'fours', 'sixes'])

try:
    source = requests.get('https://www.cricbuzz.com/cricket-series/7476/icc-mens-t20-world-cup-2024/stats')
    # Request module to access the website

    soup = BeautifulSoup(source.text, 'html.parser')

    players = soup.find('tbody').find_all('tr')

    for batter in players:
        name = batter.find('td', class_= 'cb-srs-stats-td text-left').a.text
        stats = batter.find_all('td', class_= 'cb-srs-stats-td text-right')
        rank = stats[0].text
        matches = stats[1].text
        inns = stats[2].text
        runs = stats[3].text
        avg = stats[4].text
        strike_rate = stats[5].text
        fours = stats[6].text
        sixes = stats[7].text

        print(rank, name, matches, inns, runs, avg, strike_rate, fours, sixes)

        sheet.append([rank, name, matches, inns, runs, avg, strike_rate, fours, sixes])
        # Creating headings on the empty sheet

except Exception as e: 
    print(e)

excel.save('Top Batsmen SA Tour 2024.xlsx')
# Saving the scrapped data in an excel sheet

