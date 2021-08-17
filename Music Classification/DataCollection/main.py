from Mp4ToMp3Converter import Mp4ToMp3Converter
from YTDownloader import YTDownloader
from FolderViewer import FolderViewer
import os

ytd = YTDownloader()
converter = Mp4ToMp3Converter()

video_path="video/Classical"
music_path="music/Classical"
if not os.path.isdir(video_path): #若沒有video_path資料夾則產生
    os.mkdir(video_path)
if not os.path.isdir(music_path): #若沒有music_path資料夾則產生
    os.mkdir(music_path)

# Classical https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PL2788304DC59DBEB4&index=1
# Jazz https://www.youtube.com/watch?v=CWzrABouyeE&list=PLw-VjHDlEOgtzDGfrQ9QEvbEppw_35yaj
# Reggae https://www.youtube.com/watch?v=K6oYyG0KcvQ&list=PLwY9l4M25GOJqIx-Dn-PmYs1KjPd80-1N&index=1
# Disco https://www.youtube.com/watch?v=I_izvAbhExY&list=PLEXox2R2RxZKUmrWKNF61K-kZSov14Snr&index=1
# EDM https://www.youtube.com/watch?v=gCYcHz2k5x0&list=PLw6eTMMKY24QLYfmrU2rB8x-lP5Fas2dY

titles = ytd.downloadList("https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PL2788304DC59DBEB4&index=1",20,video_path)

fv = FolderViewer(video_path)
titles = fv.getFileListTitle()
for title in titles:
    print(title)
    converter(video_path+"/"+title+".3gpp", music_path+"/"+title+".mp3")