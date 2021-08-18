from tensorflow import keras
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import cv2
import os
import sys
import warnings

#顧名思義，就是進行音樂辨識

class MusicClassifier:
    def __init__(self, load_model_path="music_classificaiton_model.h5"):
        if not sys.warnoptions: #忽視librosa讀mp3出現的warning
            warnings.simplefilter("ignore")
        self.class_name = ('Blue', 'Classical', 'Country', 'Disco', 'EDM', 'Hiphop', 'Jazz', 'Metal', 'Pop', 'Reggae')
        self.model = keras.models.load_model(load_model_path)

    def getPredictByPath(self, paths):
        if not isinstance(paths, list): #輸入希望為list
            if isinstance(paths, str): #若只有一個輸入為string的內容自動變為list
                paths = [paths]
            else:
                print("Error: input must as type list or str")
                return

        img_features = []
        for path in paths:
            if not isinstance(path, str): #輸入為路徑，期望輸入type為str
                print("Error: element in list must as type str")

            try:
                img = self.getMelImg(path) #取得影像(224, 224, 3)
                img_features.append(img) #合併成list
            except:
                print("Error on path: ",path)
        if len(img_features) == 0: #沒有成功轉成img的檔案
            print("All paths are invalid.")
            return
        img_features = np.array(img_features) #轉成array
        preds = self.model.predict(img_features) #預測
        result = []
        for pred in preds:
            class_index = np.argmax(pred) #取得最大值得index
            result.append(self.class_name[class_index])
        return result

    def getPredictByArray(self, arrays):
        pred = self.model.predict(arrays)
        class_index = np.argmax(pred)
        result = self.class_name[class_index]
        return result

    def getMelImg(self, music_path):
        save_img_path = "mel.png"
        #產生mel scale spectrogram圖片
        sample_rate, data = self.__getAudio(music_path)
        logmelspec = self.__getLogMelScale(sample_rate, data, 1024, 512, 256)
        self.__saveImg(sample_rate, logmelspec, save_img_path)
        #利用cv2讀檔
        img = cv2.imread(save_img_path) #shape=(220, 449, 3)
        img = cv2.resize(img, (224, 224))
        os.remove(save_img_path) #由於不希望儲存大量圖片，因此讀完後就刪除
        return img

    #取得音訊的array
    def __getAudio(self, audio_path):
        data, sample_rate = librosa.load(audio_path) #讀成 array
        if len(data.shape)==2: #若為雙通道則相加平均
            data = data.T
            data = (data[0]+data[1])/2
        return sample_rate, data #回傳sample rate 與 array

    def __getLogMelScale(self, sample_rate, signals, frame_length, frame_step, num_mel_bins): #傳入取樣率 訊號(聲音矩陣) frame長度 frame移動距離
        melspec = librosa.feature.melspectrogram(signals,sample_rate,n_fft=frame_length,\
                                                                hop_length=frame_step,n_mels=num_mel_bins) #取得mel的filterbank
        logmelspec = librosa.amplitude_to_db(melspec) #取對數
        return logmelspec

    def __saveImg(self, sample_rate, logmelspec, save_path):
        fig = plt.figure(figsize = (8, 4))
        librosa.display.specshow(logmelspec, sr=sample_rate)
        fig.savefig(save_path, bbox_inches='tight', pad_inches=0.0)
        plt.close('all')

if __name__=="__main__":
    mc = MusicClassifier()
    predict = mc.getPredictByPath(["music/Hiphop18.mp3", "music/Blue00.mp3"])
    print(predict)