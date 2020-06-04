import requests
import json
import html
from html2json import collect
from bs4 import BeautifulSoup
from bs2json import bs2json
import csv
import ast
import time

with open('psnowgamelist.csv', mode='w', encoding="utf-8", newline='') as gamelist_file:
    fieldname = ['Game', 'Console', 'Until']
    gamelist = csv.DictWriter(gamelist_file, fieldnames=fieldname)
    gamelist.writeheader()
    url = "https://psvrtrophy.software.eu.playstation.com/ps-now/data_sync"

    headers = {
      'Connection': 'keep-alive',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#       'Origin': 'https://www.playstation.com',
#       'Sec-Fetch-Site': 'same-site',
#       'Sec-Fetch-Mode': 'cors',
#       'Sec-Fetch-Dest': 'empty',
#       'Referer': 'https://www.playstation.com/de-de/explore/playstation-now/playstation-now-spiele-katalog/',
#       'Accept-Language': 'de-DE,de;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5,fr;q=0.4'
    }
    for i in range(0,99):
        payload = "genre=&platform=&sorting=alphabetical&search=&ajax_action=filter_games&page_num=" + str(i)
        try:
            response = requests.request("POST", url, headers=headers, data = payload)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        games = json.loads(response.text)
        if games['action_queue'][0][1]:
            games = games['action_queue'][0][1]['value']
            converter = bs2json()
            soup = BeautifulSoup(games, "lxml")

            for j in soup.findAll('div', class_="cc_psnow_game_item"):
                for s in j.findAll('h3'):
                    m = s.extract()
                    extracter = converter.convert(m)
                    gametitle = extracter['h3']['text']
                if j.find('img', alt="PS3"):
                    console = "PS3"
                elif j.find('img', alt="PS4"):
                    console = "PS4"
                elif j.find('img', alt="PS2"):
                    console = "PS2"
                print(gametitle+console)
                gamelist.writerow({'Game': gametitle,'Console': console, 'Until': 'TBD'})
