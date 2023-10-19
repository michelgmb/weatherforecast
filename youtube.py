import pytube
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=bGVfAa-Ixmg'
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download('/Downloads')