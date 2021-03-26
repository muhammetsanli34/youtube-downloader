from __future__ import unicode_literals
import youtube_dl

count=input("Enter the song count: ")

links=[]

for i in range(0,int(count)):
    enter = input ("Enter the link: ")
    links.append(enter)
    


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

for link in links:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
