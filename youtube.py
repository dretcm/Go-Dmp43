import pytube
import subprocess
from PyQt5.QtCore import QThread
import pyautogui
import os
import time


def showDialog(title='Error!', 
    text='''
    POSIBLES ERRORES:
    \n* Ingreso mal el url o link de YT.
    \n* Hubo un error a la hora de descargar o convertir un archivo.
    \n* Cierre la app o intentelo de nuevo.
    '''):

    pyautogui.alert(text, title, button='OK')

class Download_YT(QThread):
    def __init__(self, url=None, resolution=None, state = None):
        super().__init__()
        self.url = url
        self.resolution = resolution
        self.filename = ''
        self.path = os.path.dirname(os.path.abspath(__file__)) + '\downloads'
        self.state = state

    def run(self):
        try:
            if self.state == 1:
                self.download_video()
            elif self.state == 2:
                self.download_playlist()
            elif self.state == 3:
                self.download_mp3()
            else:
                self.download_playlist_mp3()
        except:
            showDialog()

    def download_video(self):
        video = pytube.YouTube(self.url)
        
        stream1 = video.streams.filter(resolution=self.resolution, only_video=True).first()
        stream1.download(output_path=self.path, filename='video')
        
        stream2 = video.streams.get_audio_only()
        stream2.download(output_path=self.path, filename='audio')       

        videofile = self.path + '/video.mp4'
        audiofile = self.path + '/audio.mp4'
        outputfile = self.path + '/output.mp4'
        
        subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c copy -y {outputfile}")

        file  = self.path + '/' + stream2.default_filename
        os.rename(outputfile, file)
        os.remove(videofile)
        os.remove(audiofile)

    def download_playlist(self):
        playlist = pytube.Playlist(self.url)
        for url in playlist.video_urls:
            self.url = url
            self.download_video()


    def download_playlist_mp3(self):
        playlist = pytube.Playlist(self.url)
        for url in playlist.video_urls:
            self.url = url
            self.download_mp3()

    def download_mp3(self):
        video = pytube.YouTube(self.url)
        stream = video.streams.get_audio_only()
        stream.download(output_path=self.path, filename='music_download')
        
        outputfile = self.path + '/output.mp3'
        videofile = os.path.join(self.path, 'music_download.mp4')
        
        subprocess.run(f"ffmpeg -i {videofile} -y {outputfile}")
        file = self.path + '/' + stream.default_filename[:-4] + '.mp3'
        os.rename(outputfile, file)
        os.remove(videofile)
