import requests
import sys
import pprint
from bs4 import BeautifulSoup
import json
import youtube_dl

#Link scraper
searchtext = ''
for arg in sys.argv[1:]:
    searchtext+=str(arg)+'%20'
searchtext = searchtext.rstrip('%20')
URL = URL= "http://youtube-scrape.herokuapp.com/api/search?q=" + searchtext + "&page=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
headers = {"user-agent" : USER_AGENT} 
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
try:    
    dict_res = json.loads(soup.text)
    for result in dict_res['results']:
        try:
            link = result['video']['url']
            first_result=result
            break
        except:
            continue
    duration=first_result['video']["duration"].split(':')
    # print(link)
    if len(duration)<3 and int(duration[-2])<=10:
        file_name ='song'
        # for arg in sys.argv[1:]:
        #     file_name+=str(arg)
        outtmpl = "D:\\maymay\\whatsapp-utility-bot\\imageToSticker\\media\\audio\\" + file_name + '.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'ffmpeg_location' : 'D:\\maymay\\whatsapp-utility-bot\\imageToSticker\\utils',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    else:
        print("Too long")
except KeyError:
    print("You fucked up")

#Downloader

