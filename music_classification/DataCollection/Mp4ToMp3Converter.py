# -*- coding:utf-8 -*-
from moviepy.editor import *

class Mp4ToMp3Converter:
    def __init__(self) -> None:
        pass

    def __call__(self,file_path,target_path):
        video=VideoFileClip(file_path)
        video.audio.write_audiofile(target_path)

if __name__=="__main__":
    converter = Mp4ToMp3Converter()
    video_path="video/Classical"
    music_path="music/Classical"