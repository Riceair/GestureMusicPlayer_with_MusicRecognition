import matplotlib.pyplot as plt
import librosa.display
import numpy as np

#取得音訊的array
def getAudio(audio_path):
    data, sample_rate = librosa.load(audio_path) #讀成 array
    if len(data.shape)==2: #若為雙通道則相加平均
        data = data.T
        data = (data[0]+data[1])/2
    return sample_rate, data #回傳sample rate 與 array

def getLogMelScale(sample_rate, signals, frame_length, frame_step, num_mel_bins): #傳入取樣率 訊號(聲音矩陣) frame長度 frame移動距離
    melspec = librosa.feature.melspectrogram(signals,sample_rate,n_fft=frame_length,\
                                                            hop_length=frame_step,n_mels=num_mel_bins) #取得mel的filterbank
    logmelspec = librosa.amplitude_to_db(melspec) #取對數
    return logmelspec

def saveImg(sample_rate, logmelspec, save_path, show=False):
    fig = plt.figure(figsize = (8, 4))
    librosa.display.specshow(logmelspec, sr=sample_rate)
    fig.savefig(save_path, bbox_inches='tight', pad_inches=0.0)
    if show: #設定顯示圖片顯示，反之不顯示
        plt.show()
    else:
        plt.close('all')

if __name__=="__main__":
    sample_rate, data = getAudio(music_folders[0][0])
    logmelspec = getLogMelScale(sample_rate, data, 1024, 512, 256)
    saveImg(sample_rate, logmelspec, "mel_test.png", True)
    mfccs = librosa.feature.mfcc(S = logmelspec)
    saveImg(sample_rate, mfccs, "mfcc_test.png", True)