import pygame

class MusicControler:
    def __init__(self):
        self.music_list=[]
        self.isPlaying=False
        self.isPause=False
        self.pg_mixer=pygame.mixer
        self.current_song_index=-1

    def add_music_list(self,music_list):
        self.current_song_index=-1
        for music in music_list:
            self.music_list.append(music)

    def add_music(self,music):
        self.music_list.append(music)

    def clear_music_list(self):
        self.music_list.clear()

    def music_play(self):
        if len(self.music_list)==0:
            return

        self.current_song_index+=1
        if self.current_song_index>=len(self.music_list) or self.current_song_index<0: #播完了重播 or 播放index<0(一直按上一首)
            self.current_song_index=0

        self.pg_mixer.init()
        self.pg_mixer.music.load(self.music_list[self.current_song_index]) #將歌單第一首歌取出
        self.isPlaying=True
        self.pg_mixer.music.play()

    def is_busy(self):
        return self.pg_mixer.music.get_busy()

    def music_pause(self): #暫停音樂
        if self.isPlaying==False: #若非播放音樂中，返回
            return
        if self.isPause==False: #若非暫停則暫停
            self.pg_mixer.music.pause()
            self.isPause=True
        elif self.isPause==True: #若為暫停則停止暫停
            self.pg_mixer.music.unpause()
            self.isPause=False

    def music_next(self): #播放下一首音樂
        self.pg_mixer.music.stop()
        self.isPlaying=False
        self.isPause=False
        self.music_play()

    def music_prev(self): #播放前一首音樂
        self.current_song_index-=2
        self.pg_mixer.music.stop()
        self.isPlaying=False
        self.isPause=False
        self.music_play()    

    def music_stop(self): #所有音樂停止播放
        self.pg_mixer.music.stop()
        self.isPlaying=False
        self.isPause=False
        self.clear_music_list()

    def get_isPause(self):
        return self.isPause

    def getCurrentName(self):
        return self.music_list[self.current_song_index]
    
if __name__ == "__main__":
    mc=MusicControler()
    mc.add_music_list(["music/Blue01.mp3","music/Pop02.mp3"])
    mc.music_play()
    while True:
        chose=input("Press 1 to pause/unpause, 2 to prev, 3 to next, 4 to stop:\n")
        if chose==str(1):
            mc.music_pause()
        elif chose==str(2):
            mc.music_prev()
        elif chose==str(3):
            mc.music_next()
        elif chose==str(4):
            mc.music_stop()
            break