from MusicPlayerUI import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_GesturePlayer()

ui.setupUi(MainWindow) 
MainWindow.show()
sys.exit(app.exec_())