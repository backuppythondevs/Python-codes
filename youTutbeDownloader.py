from pytube import YouTube
from pytube.cli import on_progress

def getVideo(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    video = yt.streams.filter(progressive=True, file_extension='mp4')
    for i in range(len(video)):
        print(i+1,'-',video[i].resolution)
    return video, yt

def downloadVideo(video, choice, title):
    print('Downloading: ', video[choice-1].title)
    video[choice-1].download()
    print('Download complete!')

if __name__ == '__main__':
    url = input('Enter the url of the video: ')
    video,title = getVideo(url)
    print('Enter the number of the resolution you want to download')
    choice = int(input('Enter your option: '))
    downloadVideo(video, choice, title)
