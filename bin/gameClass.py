from random import randint,shuffle
import operator
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from functools import partial
import passLevel
class game:
    # 初始化
    def __init__(self,ui,setting,app):
        self.app = app
        self.mode = 2 # 1 是随机模式 2 是选关模式
        self.moded = 1
        self.reseted = 0
        # 默认选中的复选框
        if(self.mode==1):
            setting.randomMode.setChecked(True)
            setting.levelMode.setChecked(False)
        elif (self.mode == 2):
            setting.randomMode.setChecked(False)
            setting.levelMode.setChecked(True)
        self.level = 0 # 等级
        self.time = 0 # 用时
        self.counter = 0 # 步数
        self.match = [0,1,2,3,4,5,6,7,8] # 图片位置index 值是图的编号
        self.orientMatch = [0,1,2,3,4,5,6,7,8] # 图片位置index 值是图的编号
        self.levelStack = [] # 图片位置用于闯关模式的重置缓存
        self.loc = [-1,-1,-1,-1,-1,-1,-1,-1,-1] # 当前index是位置 对应数字数可以移到的位置
        self.src = "../ui/bob_" # 资源路径
        self.dispair = -1 # 置空消失块，也是刚打开时候画面完整
        # 设置图片的函数字典
        self.labelMatch = {
            0: ui.label_0.setPixmap,
            1: ui.label_1.setPixmap,
            2: ui.label_2.setPixmap,
            3: ui.label_3.setPixmap,
            4: ui.label_4.setPixmap,
            5: ui.label_5.setPixmap,
            6: ui.label_6.setPixmap,
            7: ui.label_7.setPixmap,
            8: ui.label_8.setPixmap,
        }
        ui.level.setText("")  # 标签初始化置空
        # 图片自适应
        ui.label_0.setScaledContents(True)
        ui.label_1.setScaledContents(True)
        ui.label_2.setScaledContents(True)
        ui.label_3.setScaledContents(True)
        ui.label_4.setScaledContents(True)
        ui.label_5.setScaledContents(True)
        ui.label_6.setScaledContents(True)
        ui.label_7.setScaledContents(True)
        ui.label_8.setScaledContents(True)
    # 设置模式
    def setMode(self,ui,setting, flag): # 复选框的操作逻辑
        if(flag==1 and setting.randomMode.isChecked()):
            # 选中随机模式
            setting.levelMode.setChecked(False)
            self.level = 0
            if(self.mode == 2):
                self.moded = 2
                self.mode = 1
        elif(flag==2 and setting.levelMode.isChecked()):
            # 选中闯关模式
            setting.randomMode.setChecked(False)
            self.level = 1 # 设置关数
            # TODO 添加选关复选框的设置
            if(self.mode==1):
                self.moded = 1
                self.mode = 2
    # 开始键
    def start(self,ui): # 开始键
        self.time = 0
        self.counter = 0
        if(self.moded != self.mode):
            self.moded = self.mode
            if(self.mode==1):
                self.randomStart(ui)
            elif(self.mode==2):
                self.levelStart(ui)
        elif(self.reseted == 1):
            self.reseted = 0
            if(self.mode==1):
                self.randomStart(ui)
            elif(self.mode==2):
                self.levelStart(ui)
    # 随机模式
    def randomStart(self,ui):
        self.level = randint(1,20)
        self.seqGen()
        self.level = 0
        self.reflush(ui)
    # 闯关模式
    def levelStart(self,ui):
        if(self.level == 0): # 设置等级，不升级
            self.level = 1
        self.seqGen()
        self.levelStack = []
        self.reflush(ui)
    # 迭代2*level次，产生match数组
    def seqGen(self):
        dispair = 8  # 消失图片的位置
        self.dispair = dispair
        self.gen(dispair)
        i = 0
        index = randint(1,4)
        while(i<self.level*2):
            if(self.autoRun(index)==1):
                i = i + 1
            index = randint(1,4)
    # 自动play，返回方向代码可否走
    def autoRun(self,flag):
        # u d l r
        # 1 2 3 4
        map = [0, 0, 0, 0]  # index是操作， 1表示可以操作
        dict = [-1, -1, -1, -1]  # 键是操作，值是可以移动的方块
        i = 0
        for i in range(9):
            if(self.loc[i] == self.dispair):  # 找到可以移动到dispair的方块
                id = i - self.dispair
                if(id == 3):
                    map[0] = 1
                    dict[0] = i
                if(id == -3):
                    map[1] = 1
                    dict[1] = i
                if (id == 1):
                    map[2] = 1
                    dict[2] = i
                if (id == -1):
                    map[3] = 1
                    dict[3] = i
            i = i + 1
        if(map[flag-1] == 1):  # 操作存在
            raw = dict[flag-1]  # 要移动的位置（有图片）
            temp = self.match[raw]
            self.match[raw] = self.match[self.dispair]
            self.match[self.dispair] = temp
            self.dispair = raw
            self.gen(self.dispair) # 现在是空
            print("空的块"+str(self.dispair))
            print(self.match)
            if(operator.eq(self.match, self.orientMatch)==True):
                return 0
            else:
                return 1
        else:
            return 0
    # 刷新ui
    def reflush(self,ui):
        src = []
        for i in range(9):
            src.append(self.src_gen(i)) # 生成资源列表
        if(self.dispair != -1):
            src[self.dispair] = "" # 清除dispair位置的图片
        for i in range(9): # 刷新显示
            self.labelMatch[i](QPixmap(src[i]))
        ui.counter.setText("步数 " + str(self.counter))
        ui.timer.setText("用时 " + str(self.time))
        if(self.level != 0):
            ui.level.setText("关数 " + str(self.level))
        else:
            ui.level.setText("")  # 标签初始化置空
    # 重置键 随机模式图片重置 闯关模式回退到关卡开始
    def reset(self,ui):
        if(self.level==0):
            self.match = self.orientMatch
            self.dispair = -1
            self.loc = [-1,-1,-1,-1,-1,-1,-1,-1,-1] # 当前index是位置 对应数字数可以移到的位置
        else:
            while(len(self.levelStack)!=0):
                self.autoRun(self.levelStack.pop())
        self.counter = 0
        self.time = 0
        self.reseted = 1
        self.reflush(ui)
    # 生成图片地址
    def src_gen(self,i): # 位置对应图片资源
        return self.src + str(self.match[i]) + ".png"
    # 方向键的运行
    def play(self,ui,flag):
        # u d l r
        # 1 2 3 4
        if(self.dispair == -1):
            return
        map = [0, 0, 0, 0] # index是操作， 1表示可以操作
        dict = [-1,-1,-1,-1]# 键是操作，值是可以移动的方块
        i = 0
        for i in range(9):
            if(self.loc[i] == self.dispair): # 找到可以移动到dispair的方块
                id = i - self.dispair
                if(id==3):
                    map[0] = 1
                    dict[0] = i
                if(id==-3):
                    map[1] = 1
                    dict[1] = i
                if (id ==1):
                    map[2] = 1
                    dict[2] = i
                if (id ==-1):
                    map[3] = 1
                    dict[3] = i
            i = i + 1
        if(map[flag-1] == 1): # 操作存在
            self.counter = self.counter + 1
            ui.counter.setText("步数 "+str(self.counter))
            raw = dict[flag-1] # 要移动的位置(原来有图片)
            src = self.src_gen(raw) # 获取原位置的图片资源
            dispair = self.dispair
            self.labelMatch[dispair](QPixmap(src)) # 移动到空白块
            self.labelMatch[raw](QPixmap(""))
            self.dispair = raw # 更新缺失的图片位置
            # 更新match数组
            temp = self.match[raw]
            self.match[raw] = self.match[dispair]
            self.match[dispair] = temp
            if(flag in [1,3]):
                self.levelStack.append(flag+1)
            elif(flag in [2,4]):
                self.levelStack.append(flag-1)
            # 更新位置数组
            self.gen(self.dispair)
            if(operator.eq(self.match,self.orientMatch)==True):
                lastSrc = self.src_gen(self.dispair)
                self.labelMatch[self.dispair](QPixmap(lastSrc))
                self.levelStack = []
                self.passLevel(ui)
    # 创建设置窗口对象
    def passLevel(self,ui):
        self.log = QDialog()
        self.passLog = passLevel.Ui_Dialog()
        self.passLog.setupUi(self.log)
        self.log.show()
        self.passLog.label.setText("恭喜你！通过第"+str(self.level)+"关")
        # time = "用时 "+str(self.time)+"s"
        # counter = "步数 "+str(self.counter)+"s"
        self.passLog.useTime.setText("")
        self.passLog.useCount.setText("")
        self.level = self.level + 1 # level加一
        self.listener(ui)
    # 通关窗体设置
    def listener(self,ui):
        self.passLog.next.clicked.connect(partial(self.upLevel,ui))
        self.passLog.quit.clicked.connect(self.exit)
    # 通关窗口
    def upLevel(self,ui):
        self.reseted = 1
        self.start(ui)
        self.log.close()
    # 退出
    def exit(self):
        sys.exit(self.app.exec_())
    # 生成位置数组
    def gen(self,loc):
        self.loc = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        if (loc == 0):
            self.loc[1] = loc
            self.loc[3] = loc
        if (loc == 1):
            self.loc[0] = loc
            self.loc[2] = loc
            self.loc[4] = loc
        if (loc == 2):
            self.loc[1] = loc
            self.loc[5] = loc
        if (loc == 3):
            self.loc[0] = loc
            self.loc[4] = loc
            self.loc[6] = loc
        if (loc == 4):
            self.loc[1] = loc
            self.loc[3] = loc
            self.loc[5] = loc
            self.loc[7] = loc
        if (loc == 5):
            self.loc[2] = loc
            self.loc[4] = loc
            self.loc[8] = loc
        if (loc == 6):
            self.loc[3] = loc
            self.loc[7] = loc
        if (loc == 7):
            self.loc[4] = loc
            self.loc[6] = loc
            self.loc[8] = loc
        if (loc == 8):
            self.loc[5] = loc
            self.loc[7] = loc