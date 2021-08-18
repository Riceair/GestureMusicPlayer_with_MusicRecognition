import os

#確認現有音樂
#檢查紀錄的資料是否要更新

class DataChecker:
    def __init__(self):
        self.music_path = "music/"
        self.record_path = "doc/"
        self.class_name = ('Blue', 'Classical', 'Country', 'Disco', 'EDM', 'Hiphop', 'Jazz', 'Metal', 'Pop', 'Reggae')
        self.__confirmDocExist() #確認紀錄檔是否存在
        if len(os.listdir(self.record_path)) != len(self.class_name): #確認是否有多餘資料
            self.__removeOtherData()

        self.record_list = [self.record_path+file for file in os.listdir(self.record_path)] #所有記錄檔的位置
        #確認是否有記錄到不存在的檔案(可能被使用者刪除)
        not_exist_list = self.__getRecordNotExist()
        if len(not_exist_list) != 0:
            self.__cleanRecord(not_exist_list) #去除該紀錄
    
    def getUnRecordedMusic(self): #取得尚未記錄到的音樂
        unrecorded = []
        music = self.getMusic()
        record_music = self.getRecordedMusic()
        for m in music:
            if m not in record_music:
                unrecorded.append(m)
        return unrecorded

    def getMusic(self): #取得現有音樂
        path_list = os.listdir(self.music_path)
        music_path = [self.music_path+path for path in path_list]
        return music_path

    def getRecordedMusic(self): #取得已經記錄到的音樂
        recorded_music = []
        for file_name in self.record_list:
            with open(file_name,'r') as f:
                for line in f.readlines():
                    recorded_music.append(line[:-1])
        return recorded_music

    def __confirmDocExist(self): #確認紀錄檔是否存在
        for name in self.class_name:
            file_name = self.record_path+name+".txt"
            if not os.path.exists(file_name):
                file = open(file_name,'w')
                file.close()
    
    def __removeOtherData(self): #去除多餘資料(若有的話)
        path_list = os.listdir(self.record_path)
        valid_data = [name+".txt" for name in self.class_name] #有效檔案
        for path in path_list:
            if path not in valid_data:
                os.remove(self.record_path+path)
    
    def __cleanRecord(self, not_exist_list):
        for file_name in self.record_list:
            isChange=False
            recorded_music = [] #先記下已經記錄了甚麼
            with open(file_name,'r') as f:
                for line in f.readlines():
                    recorded_music.append(line)

            for not_exist in not_exist_list:
                if not_exist in recorded_music: #確認不存在檔案是否在此之中
                    recorded_music.remove(not_exist) #若有則清除
                    isChange=True
            
            if not isChange: #未更動，不需重新寫
                continue

            recorded_music.sort()
            with open(file_name,'w') as f: #全部重新寫回去
                for rm in recorded_music:
                    f.write(rm)

    def __getRecordNotExist(self): #取得記錄到不存在的檔案
        wrong_record = []
        music = self.getMusic()
        record_music = self.getRecordedMusic()
        for rm in record_music:
            if rm not in music: #去除換行字元
                wrong_record.append(rm+"\n")
        return wrong_record

if __name__=="__main__":
    datachecker = DataChecker()
    unrec = datachecker.getUnRecordedMusic()
    print(unrec)