from pytube import YouTube
import pytube
import os

class Main:

    def __init__(self, url):
        self.url = url

        if os.name == 'nt':
            self.path = os.getcwd() + "\\"
        else:
            self.path = os.getcwd() + "/"


    def converter(self):
        yt = YouTube(self.url)  
        vid = YouTube(self.url).streams.filter(only_audio=True).first().download(filename=yt.title)
        print("Downloaded")
        location = self.path + yt.title + ".mp4"
        renameLocation = self.path + yt.title + ".mp3"
        
        if os.name == 'nt':
            os.system('ren {0} {1}'.format(location, renameLocation))
        else:
            os.system('mv {0} {1}'.format(location, renameLocation))

if __name__ == "__main__":
    url = input("Enter the url of the video: ")
    Main(url).converter()