import librosa
import os

music_path = "Music Classification/music"
folder_names = os.listdir(music_path)

for folder in folder_names:
    for i, file_name in enumerate(os.listdir(music_path+"/"+folder)):
        os.rename(music_path+"/"+folder+"/"+file_name, music_path+"/"+folder+"/"+folder+"{0:02d}".format(i)+".mp3")