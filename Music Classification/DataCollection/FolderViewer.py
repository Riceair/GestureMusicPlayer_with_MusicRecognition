#本程式目的為檢視資料夾內有甚麼資料
import os

class FolderViewer:
    def __init__(self,root_path):
        self.root_path = root_path
        self.file_list = os.listdir(root_path)

    def getFileList(self):
        return self.file_list

    def getFileListTitle(self): #沒有附檔名(去除.mp4 .mp3....)
        file_title=[]
        for file in self.file_list:
            title = file[:file.rindex('.')]
            file_title.append(title)
        return file_title

if __name__=="__main__":
    fv = FolderViewer("video/Classical")
    print(fv.getFileListTitle())