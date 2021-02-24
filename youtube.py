import pytube
from moviepy.editor import VideoFileClip
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
        self.path = os.path.dirname(os.path.abspath(__file__)) + '\youtube_downloads'
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

    def download_video(self, filename=None):
        video = pytube.YouTube(self.url)
        stream = video.streams.filter(resolution=self.resolution).first()
        stream.download(output_path=self.path, filename=filename)
        self.filename = stream.default_filename


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
        self.download_video(filename='music_download')
        old = os.path.join(self.path, 'music_download.mp4')
        new = os.path.join(self.path, self.filename[:-4] + '.mp3')
        video = VideoFileClip(old)
        video.audio.write_audiofile(new)
        video.close()
        time.sleep(0.5)
        os.remove(old)