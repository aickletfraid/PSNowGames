import requests
import json
import html
from html2json import collect
from bs4 import BeautifulSoup
from bs2json import bs2json
import csv
import ast
import time
import unicodedata

url = "https://www.playstation.com/en-en/explore/playstation-now/ps-now-games/"

payload = {}
headers = {
  'authority': 'www.playstation.com',
  'cache-control': 'max-age=0',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
#   'referer': 'https://www.playstation.com/de-de/explore/playstation-now/ps-now-games/',
  'accept-language': 'de-DE,de;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5,fr;q=0.4',
  'cookie': 'psnowuuid=tmPMxnXlpgThnpySm6it; s_fid=32709406EC60097D-055562D76AF8141D; _fbp=fb.1.1590410407201.907884392; sat_track=true; pdc_custage=m; said=300ef6d3-cf9e-4304-8ef3-dde09d70543b; dcm2=null%7Cnull%7Cnull%7Cnull%7Cnull%7Cnull; at_check=true; AMCVS_BD260C0F53C9733E0A490D45%40AdobeOrg=1; s_cc=true; DisableCookieAlert=YES; eu-auth=true; eucookiepreference=accept; sbPlatformPrivacyLevel=all; check=true; _evidon_consent_cookie={"consent_date":"2020-06-03T20:31:40.498Z","consent_type":1}; userinfo=c36a38b3a46326c5d923de20bf18552b2c38b29aeee2add712381395584e792c; ag_US=m; ph=denzoned; PDCUserDecrypt=%7B%22avatarUrl%22%3A%22http%3A%2F%2Fstatic-resource.np.community.playstation.net%2Favatar%2FWWS_A%2FUP90001209G03_BAEDE4B3D72B495E02D4_L.png%22%2C%22dob%22%3A%221993-07-09%22%2C%22avatar_url_large%22%3A%22%2F%2Fstatic-resource.np.community.playstation.net%2Favatar%2FWWS_A%2FUP90001209G03_BAEDE4B3D72B495E02D4_L.png%22%2C%22avatar_url_medium%22%3A%22%2F%2Fstatic-resource.np.community.playstation.net%2Favatar_m%2FWWS_A%2FUP90001209G03_F350D1CDDCBDE7930BD2_M.png%22%2C%22legalCountry%22%3A%22de%22%2C%22handle%22%3A%22denzoned%22%2C%22avatar_url_small%22%3A%22%2F%2Fstatic-resource.np.community.playstation.net%2Favatar_s%2FWWS_A%2FUP90001209G03_4E7B1FD9A94A93943B8C_S.png%22%2C%22originalId%22%3A%22denzoned%22%2C%22sub_account%22%3Afalse%2C%22region%22%3A%22SCEE%22%2C%22age%22%3A26%2C%22isPlusUser%22%3A1%7D; dcm=null%7Cnull%7Cnull%7Cnull%7Cnull%7Cnull; __lt__cid=22fecdae-6fa9-4040-805c-beb1a87e82c3; _ga=GA1.2.2128346606.1591234798; _gid=GA1.2.1841338534.1591234798; JSESSIONID=node0p3eodkv4nppcb8vrxvufvvw211036.node0; AWSELB=BD87EDB90E7E5EC1FE3D0497C5EE8FE6334A3A64CC76523C0B46185D0C336E01789A9A9E061186757BC9C4A8DC36B9261FAA2B29E66C405AAD4DF0B84D7E51FE5D04602A88; AWSELBCORS=BD87EDB90E7E5EC1FE3D0497C5EE8FE6334A3A64CC76523C0B46185D0C336E01789A9A9E061186757BC9C4A8DC36B9261FAA2B29E66C405AAD4DF0B84D7E51FE5D04602A88; AKA_A2=A; mboxEdgeCluster=35; AMCV_BD260C0F53C9733E0A490D45%40AdobeOrg=-408604571%7CMCIDTS%7C18417%7CMCMID%7C08323882302273719087648349596693384028%7CMCAID%7CNONE%7CMCOPTOUT-1591270700s%7CNONE%7CvVersion%7C4.6.0%7CMCAAMLH-1591868300%7C6%7CMCAAMB-1591868300%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; ps_auth=sess_start_time=2020-06-04T09:39:09+00:00&psn_ticket=&psn_token=51a2fb5f-02dd-400b-a2aa-55cfe990587f; ps_profile=ct=2020-06-04T09:39:09+00:00&avatar_url_large=https%3A%2F%2Fstatic-resource.np.community.playstation.net%2Favatar%2FWWS_A%2FUP90001209G03_BAEDE4B3D72B495E02D4_L.png&psnbeta=false&avatar_url_medium=https%3A%2F%2Fstatic-resource.np.community.playstation.net%2Favatar_m%2FWWS_A%2FUP90001209G03_F350D1CDDCBDE7930BD2_M.png&psplus=true&avatar_url_small=https%3A%2F%2Fstatic-resource.np.community.playstation.net%2Favatar_s%2FWWS_A%2FUP90001209G03_4E7B1FD9A94A93943B8C_S.png&aid=z83ydqg5mZNRkXh947FHdk34zxSA1Al6PHwizgE/geg=&online_id=denzoned; uh=c36a38b3a46326c5d923de20bf18552b2c38b29aeee2add712381395584e792c; pid_ps=a2b0ad054af9f196946cde05fad502f7; mbox=PC#97411ab27e1d47b6a02ae6c632c4fea0.35_0#1654508353|session#6ec1738f7ab543ea81f09b7175f04450#1591265357; euconsent=BO0cFVZO0d4ySASABAENDM-AAAAv6AAA; s_sq=%5B%5BB%5D%5D'
}

r = requests.request("GET", url, headers=headers, data = payload)

r = response.text.encode('utf8')
soup = BeautifulSoup(r, "lxml")
converter = bs2json()
allgames = []
with open('psnowgamelist3-1.csv', mode='w', encoding="utf-8", newline='') as gamelist_file:
    fieldname = ['Game', 'Console', 'Until']
    gamelist = csv.DictWriter(gamelist_file, fieldnames=fieldname)
    gamelist.writeheader()
    for s in soup.findAll('div', class_='copyblock parbase section'):
        m = s.extract()
        extracter = converter.convert(m)
        if m.find('h3', class_='tier3Header default '):
            x = m.find('h3', class_='tier3Header default ')
            x = x.extract()
            extracter = converter.convert(x)
            if extracter['h3']['text']=='PS4':

                for j in m.findAll('div', class_="richtext default counter-continue"):
                    linenum = int(len(j.text.split('\n')))
                    for i in range(1,linenum-1):
                        gametitle = j.text.split("\n")[i]
                        gametitle = "".join(gametitle.splitlines())
                        if "PS2" in gametitle:
                            console = "PS2/PS4"
                        else:
                            console = "PS4"
                        if len(gametitle)!=0:
                            game = [gametitle, console]
                            allgames.append(game)
            if extracter['h3']['text']=='PS3':
                console = 'PS3'
                for j in m.findAll('div', class_="richtext default counter-continue"):
                    linenum = int(len(j.text.split('\n')))
                    for i in range(1,linenum-1):
                        gametitle = j.text.split("\n")[i]
                        gametitle = "".join(gametitle.splitlines())
                        if len(gametitle)!=0 and gametitle!= " ":
                            game = [gametitle, console]
                            allgames.append(game)
    allgames.sort()
    print(allgames)
    for i in allgames:
        gametitle = unicodedata.normalize("NFKD", i[0])
        if gametitle != " ":
            print(gametitle)
            console = i[1]
            gamelist.writerow({'Game': gametitle,'Console': console, 'Until': 'TBD'})
