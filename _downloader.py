from __future__ import unicode_literals
import youtube_dl

links=[]

for i in range(1,3):
    enter = input ("Enter the link")
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
