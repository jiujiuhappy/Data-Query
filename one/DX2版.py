# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DX2版.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
'''
还需完成：
    1、其他、全选、空白的值的获取
    2、筛选的优化
    3、全目录的整理
    4、整理全部的业务量到一张表
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from one.datefarm import DateFarm
from one.getalltime import GetAllTime
import pandas as pd
from one.pandasmodel import pandasModel

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.zhanghao_box = []  # 存储选择账号的列表
        self.passwd = {'kezhe': 'kezhe1990','123':'qwqwqw'}  # 存储验证信息（字典形式）
        self.sheet = []  # 存储获取的表名
        self.filename = None  # 存储打开按钮获取的文件名
        self.filename_save = None  # 存储保存时的新建文件名
        self.yzpass = False  # 验证开关
        self.df = None  # 存储表

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dakai = QtWidgets.QPushButton(self.frame)
        self.dakai.setObjectName("dakai")
        self.horizontalLayout.addWidget(self.dakai)
        self.baocun = QtWidgets.QPushButton(self.frame)
        self.baocun.setObjectName("baocun")
        self.horizontalLayout.addWidget(self.baocun)
        self.chongzhi = QtWidgets.QPushButton(self.frame)
        self.chongzhi.setObjectName("chongzhi")
        self.horizontalLayout.addWidget(self.chongzhi)
        self.yuliu1 = QtWidgets.QPushButton(self.frame)
        self.yuliu1.setObjectName("yuliu1")
        self.horizontalLayout.addWidget(self.yuliu1)
        self.yuliu2 = QtWidgets.QPushButton(self.frame)
        self.yuliu2.setObjectName("yuliu2")
        self.horizontalLayout.addWidget(self.yuliu2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lable_3 = QtWidgets.QLabel(self.frame)
        self.lable_3.setObjectName("lable_3")
        self.gridLayout_3.addWidget(self.lable_3, 0, 0, 1, 1)
        self.yonghu = QtWidgets.QLineEdit(self.frame)
        self.yonghu.setObjectName("yonghu")
        self.gridLayout_3.addWidget(self.yonghu, 0, 1, 1, 1)
        self.lable_4 = QtWidgets.QLabel(self.frame)
        self.lable_4.setObjectName("lable_4")
        self.gridLayout_3.addWidget(self.lable_4, 1, 0, 1, 1)
        self.mima = QtWidgets.QLineEdit(self.frame)
        self.mima.setInputMask("")
        self.mima.setText("")
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")
        self.gridLayout_3.addWidget(self.mima, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.yanzheng = QtWidgets.QPushButton(self.frame)
        self.yanzheng.setObjectName("yanzheng")
        self.horizontalLayout.addWidget(self.yanzheng)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.xiafa = QtWidgets.QRadioButton(self.frame_2)
        self.xiafa.setObjectName("xiafa")
        self.gridLayout.addWidget(self.xiafa, 0, 0, 1, 1)
        self.jieshou = QtWidgets.QRadioButton(self.frame_2)
        self.jieshou.setObjectName("jieshou")
        self.gridLayout.addWidget(self.jieshou, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.qishi = QtWidgets.QDateEdit(self.frame_2)
        self.qishi.setAcceptDrops(False)
        self.qishi.setAutoFillBackground(False)
        self.qishi.setWrapping(False)
        self.qishi.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.qishi.setAccelerated(False)
        self.qishi.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.qishi.setProperty("showGroupSeparator", False)
        self.qishi.setCalendarPopup(True)
        self.qishi.setDate(QtCore.QDate(year, month, day))
        self.qishi.setObjectName("qishi")
        self.gridLayout.addWidget(self.qishi, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.zhongzhi = QtWidgets.QDateEdit(self.frame_2)
        self.zhongzhi.setCalendarPopup(True)
        self.zhongzhi.setDate(QtCore.QDate(year, month, day))
        self.zhongzhi.setObjectName("zhongzhi")
        self.gridLayout.addWidget(self.zhongzhi, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dianshang = QtWidgets.QCheckBox(self.frame_2)
        self.dianshang.setObjectName("dianshang")
        self.gridLayout_2.addWidget(self.dianshang, 0, 0, 1, 1)
        self.hangye = QtWidgets.QCheckBox(self.frame_2)
        self.hangye.setObjectName("hangye")
        self.gridLayout_2.addWidget(self.hangye, 0, 1, 1, 1)
        self.kzyx = QtWidgets.QCheckBox(self.frame_2)
        self.kzyx.setObjectName("kzyx")
        self.gridLayout_2.addWidget(self.kzyx, 0, 2, 1, 1)
        self.YJDX = QtWidgets.QCheckBox(self.frame_2)
        self.YJDX.setObjectName("YJDX")
        self.gridLayout_2.addWidget(self.YJDX, 0, 3, 1, 1)
        self.Gateway = QtWidgets.QCheckBox(self.frame_2)
        self.Gateway.setObjectName("Gateway")
        self.gridLayout_2.addWidget(self.Gateway, 1, 0, 1, 1)
        self.guwanght = QtWidgets.QCheckBox(self.frame_2)
        self.guwanght.setObjectName("guwanght")
        self.gridLayout_2.addWidget(self.guwanght, 1, 1, 1, 1)
        self.localgate2 = QtWidgets.QCheckBox(self.frame_2)
        self.localgate2.setObjectName("localgate2")
        self.gridLayout_2.addWidget(self.localgate2, 1, 2, 1, 1)
        self.ocs_smc2 = QtWidgets.QCheckBox(self.frame_2)
        self.ocs_smc2.setObjectName("ocs_smc2")
        self.gridLayout_2.addWidget(self.ocs_smc2, 1, 3, 1, 1)
        self.openet = QtWidgets.QCheckBox(self.frame_2)
        self.openet.setObjectName("openet")
        self.gridLayout_2.addWidget(self.openet, 2, 0, 1, 1)
        self.zxsmg = QtWidgets.QCheckBox(self.frame_2)
        self.zxsmg.setObjectName("zxsmg")
        self.gridLayout_2.addWidget(self.zxsmg, 2, 1, 1, 1)
        self.jifei = QtWidgets.QCheckBox(self.frame_2)
        self.jifei.setObjectName("jifei")
        self.gridLayout_2.addWidget(self.jifei, 2, 2, 1, 1)
        self.mmsc = QtWidgets.QCheckBox(self.frame_2)
        self.mmsc.setObjectName("mmsc")
        self.gridLayout_2.addWidget(self.mmsc, 2, 3, 1, 1)
        self.qita = QtWidgets.QCheckBox(self.frame_2)
        self.qita.setObjectName("qita")
        self.gridLayout_2.addWidget(self.qita, 3, 0, 1, 1)
        self.zongliang = QtWidgets.QCheckBox(self.frame_2)
        self.zongliang.setObjectName("zongliang")
        self.gridLayout_2.addWidget(self.zongliang, 3, 1, 1, 1)
        self.kongbai = QtWidgets.QCheckBox(self.frame_2)
        self.kongbai.setObjectName("kongbai")
        self.gridLayout_2.addWidget(self.kongbai, 3, 2, 1, 1)
        self.yuliu = QtWidgets.QCheckBox(self.frame_2)
        self.yuliu.setObjectName("yuliu")
        self.gridLayout_2.addWidget(self.yuliu, 3, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.chaxun = QtWidgets.QPushButton(self.frame_2)
        self.chaxun.setObjectName("chaxun")
        self.horizontalLayout_2.addWidget(self.chaxun)
        self.verticalLayout.addWidget(self.frame_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.maintext = QtWidgets.QTableView(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintext.sizePolicy().hasHeightForWidth())
        self.maintext.setSizePolicy(sizePolicy)
        self.maintext.setMinimumSize(QtCore.QSize(579, 339))
        self.maintext.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.maintext.setObjectName("maintext")
        self.maintext.horizontalHeader().resizeSection(0, 100)  # 调整第一列的大小为100像素
        self.horizontalLayout_3.addWidget(self.maintext)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logtext = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logtext.sizePolicy().hasHeightForWidth())
        self.logtext.setSizePolicy(sizePolicy)
        self.logtext.setMinimumSize(QtCore.QSize(600, 339))
        self.logtext.setMaximumSize(QtCore.QSize(600, 16777215))
        self.logtext.setObjectName("logtext")
        self.horizontalLayout_5.addWidget(self.logtext)
        self.horizontalLayout_6.addWidget(self.frame_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.shuoming = QtWidgets.QLineEdit(self.frame_4)
        self.shuoming.setObjectName("shuoming")
        self.horizontalLayout_4.addWidget(self.shuoming)
        self.verticalLayout.addWidget(self.frame_4)
        font = QtGui.QFont()  # 创建QFont()对象
        font.setPointSize(10)  # 设置编辑框字体大小的值
        self.maintext.setFont(font)  # 设置编辑框字体
        self.maintext.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.logtext.setFont(font)  # 设置编辑框字体
        self.logtext.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.shuoming.setFont(font)  # 设置编辑框字体
        self.shuoming.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "短信业务量查询工具1.0"))
        self.dakai.setText(_translate("MainWindow", "打开"))
        self.baocun.setText(_translate("MainWindow", "保存"))
        self.chongzhi.setText(_translate("MainWindow", "重置"))
        self.yuliu1.setText(_translate("MainWindow", "预留1"))
        self.yuliu2.setText(_translate("MainWindow", "预留2"))
        self.lable_3.setText(_translate("MainWindow", "账号："))
        self.lable_4.setText(_translate("MainWindow", "密码:"))
        self.yanzheng.setText(_translate("MainWindow", "验证"))
        self.xiafa.setText(_translate("MainWindow", "下发"))
        self.jieshou.setText(_translate("MainWindow", "接收"))
        self.label.setText(_translate("MainWindow", "起始时间："))
        self.label_2.setText(_translate("MainWindow", "结束时间："))
        self.dianshang.setText(_translate("MainWindow", "dianshang"))
        self.hangye.setText(_translate("MainWindow", "hangye"))
        self.kzyx.setText(_translate("MainWindow", "kzyx"))
        self.YJDX.setText(_translate("MainWindow", "YJDX"))
        self.Gateway.setText(_translate("MainWindow", "Gateway"))
        self.guwanght.setText(_translate("MainWindow", "guwanght"))
        self.localgate2.setText(_translate("MainWindow", "localgate2"))
        self.ocs_smc2.setText(_translate("MainWindow", "ocs_smc2"))
        self.openet.setText(_translate("MainWindow", "openet"))
        self.zxsmg.setText(_translate("MainWindow", "zxsmg"))
        self.jifei.setText(_translate("MainWindow", "jifei"))
        self.mmsc.setText(_translate("MainWindow", "mmsc"))
        self.qita.setText(_translate("MainWindow", "其他"))
        self.zongliang.setText(_translate("MainWindow", "全选"))
        self.kongbai.setText(_translate("MainWindow", "空白"))
        self.yuliu.setText(_translate("MainWindow", "预留"))
        self.chaxun.setText(_translate("MainWindow", "查询"))

        # 绑定按钮
        self.dakai.clicked.connect(self.choice_file)
        self.baocun.clicked.connect(self.save_df)
        self.chongzhi.clicked.connect(self.update_all)

        self.xiafa.toggled.connect(self.get_sheet)  # 复选框下发按钮绑定事件
        self.jieshou.toggled.connect(self.get_sheet)  # 复选框接收按钮绑定事件

        self.chaxun.clicked.connect(self.chaxun_main)

        self.dianshang.stateChanged.connect(self.get_zhanghao)
        self.hangye.stateChanged.connect(self.get_zhanghao)
        self.kzyx.stateChanged.connect(self.get_zhanghao)
        self.YJDX.stateChanged.connect(self.get_zhanghao)
        self.Gateway.stateChanged.connect(self.get_zhanghao)
        self.guwanght.stateChanged.connect(self.get_zhanghao)
        self.localgate2.stateChanged.connect(self.get_zhanghao)
        self.ocs_smc2.stateChanged.connect(self.get_zhanghao)
        self.openet.stateChanged.connect(self.get_zhanghao)
        self.zxsmg.stateChanged.connect(self.get_zhanghao)
        self.jifei.stateChanged.connect(self.get_zhanghao)
        self.zongliang.stateChanged.connect(self.get_all)
        self.kongbai.stateChanged.connect(self.get_zhanghao)
        self.qita.stateChanged.connect(self.get_zhanghao)
        self.mmsc.stateChanged.connect(self.get_zhanghao)

        self.yanzheng.clicked.connect(self.yanzheng_pass)

    # 打开按键方法（已完成）
    def choice_file(self):
        self.filename, openfile_type = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        # self.logtext.append(self.filename)
        if self.filename != '':
            file_name = self.filename.split('/')[-1:]
            self.logtext.append(f'文件<{file_name[0]}>打开成功')
        else:
            self.logtext.append('<font color=\"#FF0000\">未识别到文件</font>')

    # 保存按键的方法(已完成)
    def save_df(self):
        self.filename_save = QFileDialog.getSaveFileName(self, caption='另存为', filter='*.xlsx', initialFilter='.xlsx')
        if self.filename_save[0] != '':  # 此判断用于取消保存不会闪退
            self.df.to_excel(self.filename_save[0], index=False)
            self.logtext.append('保存成功')

    # 重置按键的方法（已完成）
    def update_all(self):
        self.check_all('off')  # 清空账号复选框
        self.logtext.clear()  # 清空日志栏
        self.filename = None  # 清空打开的文件路径
        self.zhongzhi.setDate(QtCore.QDate(year, month, day))  # 重置起始时间到今天
        self.qishi.setDate(QtCore.QDate(year, month, day))  # 重置终止时间
        # 将一个空的表传入（清空表栏）
        df = pd.DataFrame()
        model = pandasModel(df)
        self.maintext.setModel(model)

    # 账号密码的验证方法（已完成）
    def yanzheng_pass(self):
        user = self.yonghu.text()
        passwd = self.mima.text()

        if user in self.passwd:
            if self.passwd[user] == passwd:
                self.logtext.append('<font color=\"#0000FF\">用户{0}{1}{2}验证通过</font>'.format('(', user, ')'))
                self.yzpass = True
            else:
                self.logtext.append('<font color=\"#FF0000\">用户{0}{1}{2}密码错误</font>'.format('(', user, ')'))
        else:
            self.logtext.append('<font color=\"#FF0000\">用户{0}{1}{2}不存在</font>'.format('(', user, ')'))

    # 下发接收的选择获取（已完成，返回值的确认）
    def get_sheet(self):
        radiocheck = self.sender()
        if radiocheck.isChecked() == True:
            self.logtext.append('<' + radiocheck.text() + '>被选中')
            if radiocheck.text() == '下发':
                self.sheet.clear()
                self.sheet.append('0')
            elif radiocheck.text() == '接收':
                self.sheet.clear()
                self.sheet.append('1')

    # 获取时间的方法（已完成）
    def get_time(self):
        starttime = self.qishi.text()
        endtime = self.zhongzhi.text()
        return [starttime, endtime]

    # 复选框的方法1(获取勾选的账号，除全选框)
    def get_zhanghao(self, state):
        g_zhanghao = self.sender()
        if state == QtCore.Qt.Checked:
            self.zhanghao_box.append(g_zhanghao.text())
        else:
            self.zhanghao_box.remove(g_zhanghao.text())

    # 复选框的方法2（获取全选的方法）
    def get_all(self, state):
        if state == QtCore.Qt.Checked:
            self.check_all('on')
        else:
            self.check_all('off')


    # 查询按钮的方法（总体文件未上传）
    def chaxun_main(self):
        time_box = self.get_time()
        dtimes = GetAllTime(time_box[0], time_box[1])

        if self.sheet == []: #判断是否选择了下发或者接收
            self.logtext.append('<font color=\"#FF0000\">请选择下发还是接收</font>')
        else:
            sheet = int(self.sheet[0])
            if self.filename == None: # 判断如果没有选择特定文件就需要进行验证，读取数据库文件
                if self.yzpass == True:
                    path = '全年数据.xlsx' # 模拟数据库文件
                else:
                    self.logtext.append('<font color=\"#FF0000\">请进行验证或打开文件</font>')
                    path = None
            else: # 如果选择了文件则优先查询选择文件
                path = self.filename
                file_name = self.filename.split('/')[-1:]
                self.logtext.append(f'文件<{file_name[0]}>,数据查询成功')

            if path != None:
                dictywl = DateFarm(path, sheet, dtimes, self.zhanghao_box)
                self.df = pd.DataFrame(dictywl)
                model = pandasModel(self.df)
                self.maintext.setModel(model)

    #  复选框整体操作事件(传入off等于全关，传入on等于全开）
    def check_all(self,switch):
        check_a = [self.dianshang, self.hangye, self.kzyx, self.YJDX,
                     self.Gateway, self.guwanght, self.localgate2, self.ocs_smc2,
                     self.openet, self.zxsmg, self.jifei, self.mmsc,
                     self.qita, self.zongliang, self.kongbai]
        for i in check_a:
            if switch == 'off':
                i.setChecked(False)
            elif switch == 'on':
                i.setChecked(True)


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 首先必须实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()  # 实例化QtWidgets.QMainWindow类，创建自带menu的窗体类型QMainWindow
    ui = Ui_MainWindow()  # 实例UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 当来自操作系统的分发事件指派调用窗口时，
    # 应用程序开启主循环（mainloop）过程，
    # 当窗口创建完成，需要结束主循环过程，
    # 这时候呼叫sys.exit（）方法来，结束主循环过程退出，
    # 并且释放内存。为什么用app.exec_()而不是app.exec()？
    # 因为exec是python系统默认关键字，为了以示区别，所以写成exec_


if __name__ == "__main__":
    show_MainWindow()  # 调用显示窗体的方法
