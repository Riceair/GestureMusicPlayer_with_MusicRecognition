from MusicClassifier import *
from DataChecker import *

class DataRecorder:
    def __init__(self):
        self.record_path = "doc/"
        datachecker = DataChecker()
        self.unrec = datachecker.getUnRecordedMusic()
        self.music_classifier = MusicClassifier()
    
    def startRecord(self):
        if len(self.unrec) == 0:
            return
        predict_result = self.music_classifier.getPredictByPath(self.unrec)
        for i in range(len(self.unrec)):
            record_file = self.record_path+predict_result[i]+".txt"
            music_name = self.unrec[i]
            with open(record_file, 'a') as f:
                f.write(music_name+"\n")

if __name__=="__main__":
    dr = DataRecorder()
    dr.startRecord()