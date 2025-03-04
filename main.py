!pip install yt-dlp ffmpeg

import yt_dlp

video_url = "https://www.youtube.com/watch?v=GGJOC1FNqn8" 
# Replace with song of your choice

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'song.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Download the song
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

from IPython.display import Audio
Audio("song.mp3", autoplay=True)


import time

# Function to print a heart shape
def print_heart():
    for y in range(15, -15, -1):
        for x in range(-30, 30):
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        time.sleep(0.1)


print_heart()
