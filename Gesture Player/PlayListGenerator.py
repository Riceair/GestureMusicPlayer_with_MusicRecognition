import random

class PlayListGenerator:
    def __init__(self) -> None:
        self.record_path = "doc/"
        self.class_name = ('Blue', 'Classical', 'Country', 'Disco', 'EDM', 'Hiphop', 'Jazz', 'Metal', 'Pop', 'Reggae')

    def getPlayList(self):
        index = random.randint(0,9)
        play_list = self.__getNameInRecord(index)

        if len(play_list) == 0: #該類別沒有歌
            self.getPlayList()
        random.shuffle(play_list) #打亂順序(增加隨機性)
        return self.class_name[index], play_list
        
    def __getNameInRecord(self,index):
        file_name = self.record_path+self.class_name[index]+".txt"
        play_list = []
        with open(file_name,'r') as f:
            for line in f.readlines():
                play_list.append(line[:-1])
        return play_list


if __name__=="__main__":
    play_list_generator = PlayListGenerator()
    play_list = play_list_generator.getPlayList()
    print(play_list)