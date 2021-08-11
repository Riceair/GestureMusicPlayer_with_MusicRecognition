# -*- coding: utf-8 -*-
from pytube import Playlist, YouTube

class YTDownloader:
    def __init__(self):
        pass

    def download(self,url,save_path="video"): #下載歌曲
        YouTube(url).streams.first().download(save_path)
        return YouTube(url).title

    def downloadList(self,url,count=10,save_path="video"): #下載已建立的播放清單
        playlist = Playlist(url)
        print('Number of videos in playlist: %s' % len(playlist.video_urls))

        names=[] #紀錄儲存影片的檔名
        if count>len(playlist.videos):
            count = len(playlist.videos)
        print("Download Count: ",count)

        c = 0
        # Loop through all videos in the playlist and download them
        for video in playlist.videos:
            try:
                video.streams.first().download(save_path)
                print(video.title)
                c+=1
            except:
                print("error on: ", video.title)
            
            if c==count:
                break
        # for i in range(count):
        #     print(playlist.videos[i].title)
        #     playlist.videos[i].streams.first().download(save_path)

if __name__=="__main__":
    ytd = YTDownloader()
    video_path="video/Metal"
    titles = ytd.downloadList("https://www.youtube.com/watch?v=m6EBgBTs7yg&list=PLm7wnjUQm_FAMNxPGqLKZnuu5PAMhHkb-&index=1",20,video_path)