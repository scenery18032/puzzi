from functools import partial
import sys,os
from shutil import copy
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QDialog
from PyQt5.QtCore import QTimer
import split,gameClass
import mainWindow,settingWindow,passLevel # 导入自己写的主窗体

def setImage(ui,gameObj): # 设置图片
    openFile = QFileDialog.getOpenFileName()
    src = openFile[0]
    if(src == ''):
        return
    outDict = "../ui/"
    for i in range(9):
        file = '../ui/bob_'+str(i)+'png'
        try:
            os.remove(file)
        except BaseException:
            pass
    try:
        copy(src, "../ui/bob.png")
    except BaseException as e:
        print(e)
    col = 3
    row = 3
    res = split.splitimage("../ui/bob.png", col, row, outDict)
    if(res == False):
        print("ERROR")
        for i in range(9):
            file = '../ui/bob/bob_' + str(i) + 'png'
            try:
                copy(file,'../ui/')
            except BaseException:
                pass
    restart()

def restart(): # 更换图片后重启
    path = sys.executable
    os.execl(path,path,*sys.argv)

def listener(ui,setting,game): # 点击事件监听
    # 方向键
    ui.U.clicked.connect(partial(game.play,ui,1))
    ui.D.clicked.connect(partial(game.play,ui,2))
    ui.L.clicked.connect(partial(game.play,ui,3))
    ui.R.clicked.connect(partial(game.play,ui,4))
    # 开始和重置
    ui.start.clicked.connect(partial(game.start,ui))
    ui.reset.clicked.connect(partial(game.reset,ui))
    ui.file.clicked.connect(partial(setImage,ui,game))
    ui.setting.clicked.connect(partial(Dialog.show))
    # 设置窗体按钮
    setting.randomMode.stateChanged.connect(partial(game.setMode,ui,setting,1))
    setting.levelMode.stateChanged.connect(partial(game.setMode,ui,setting,2))
    setting.comfirm.clicked.connect(partial(returnGame,ui,setting,game))

def returnGame(ui,setting,game):
    Dialog.close()
    if(game.mode == 2):
        game.match = game.orientMatch
        game.dispair = 8
        game.level = 1
        game.gen(8)
    game.start(ui)


def setTime(ui,gameObj): # 显示用时
    gameObj.time = gameObj.time + 1
    ui.timer.setText('用时 '+str(gameObj.time))

if __name__ == '__main__':

    # try:
    #     subprocess.call('pyuic5 -o ./mainWindow.py ./mainWindow.ui')
    #     subprocess.call('pyuic5 -o ./settingWindow.py ./settingWindow.ui')
    # except BaseException:
    #     print("UI升级失败！")
    app = QApplication(sys.argv)
    # 创建主窗口对象
    MainWindow = QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # 创建设置窗口对象
    Dialog = QDialog()
    setting = settingWindow.Ui_Dialog()
    setting.setupUi(Dialog)
    MainWindow.show()
    gameObj = gameClass.game(ui,setting,app)
    timer = QTimer()
    timer.timeout.connect(partial(setTime,ui,gameObj))  # 计时结束调用operate()方法
    timer.start(1000)  # 设置计时间隔并启动
    listener(ui,setting,gameObj)
    sys.exit(app.exec_())

