from pytube import Playlist
py=Playlist("https://www.youtube.com/watch?v=ui4LLFPccs0&list=PLsDu33Q_p-uQFHqnTvcIDne1FzeK19JDg")
print(f'Downloading:{py.title}')
for video in py.videos:
    video.streams.first().download()