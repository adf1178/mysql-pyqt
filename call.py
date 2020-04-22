import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QTableWidgetItem
#导入designer工具生成的login模块
from window1 import Ui_loginwindow,Ui_MainWindow
from window2 import Ui_zhuwindow, Ui_SubWindow,Ui_DangerEWindow,Ui_DangerQuery,Ui_shouquan,Ui_history,Ui_PatientQ
from dialog import Ui_DialogFail, Ui_DialogSuccess,Ui_meishiDialog,Ui_wandanDialog

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from basic_ffunc import *
db = pymysql.connect("localhost","root","123456a",database="shiyan3",charset="utf8")
cursor = db.cursor()
current_uid = 0
class chenggong(QDialog, Ui_DialogSuccess):
    def __init__(self, parent=None):
        super(chenggong, self).__init__(parent)
        self.setupUi(self)
class wandan(QDialog, Ui_wandanDialog):
    def __init__(self, parent=None):
        super(wandan, self).__init__(parent)
        self.setupUi(self)
class meishi(QDialog, Ui_meishiDialog):
    def __init__(self, parent=None):
        super(meishi, self).__init__(parent)
        self.setupUi(self)
class shibai(QDialog, Ui_DialogFail):
    def __init__(self, parent=None):
        super(shibai, self).__init__(parent)
        self.setupUi(self)
class reg(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(reg, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reg)

    def reg(self):
        name = self.lineEdit.text()
        passw = self.lineEdit_2.text()
        passwordHash = md5(passw)
        user_id = GetUserCount(cursor)+1
        print(user_id)
        flag = UserReg(cursor,db,[user_id,name,passwordHash])
        if flag==-1:
            print("你来晚了")
        elif flag==1:
            print("成功")
            NewUserAuth(cursor,user_id,db)
        else:
            print("失败")

class MyMainForm(QMainWindow, Ui_loginwindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.login.clicked.connect(self.disp)
        self.register_2.clicked.connect(self.zhuce)

    def disp(self):
        global current_uid
        name = self.user_name.text()
        passw = self.password.text()
        passwordHash = md5(passw)
        flag = UserLogin(cursor,[name,passwordHash])
        if flag==0:
            self.disp1.setText("密码错误")
        elif flag==-1:
            self.disp1.setText("发生了奇怪的错误")
        else:
            current_uid=flag[0]
            UpdateIntimeData(cursor,db)
            self.window_next = zhuwin()
            self.close()
            self.window_next.show()
    def zhuce(self):
        self.the_window = reg()
        self.the_window.show()


class zhuwin(QMainWindow, Ui_zhuwindow):
    def __init__(self, parent=None):
        super(zhuwin, self).__init__(parent)
        self.setupUi(self)
        #self.table1.clearContents()
        current_level = GetUserAuthLevel(cursor,current_uid)
        if current_level<3:
            self.Auth.setVisible(False)
        if current_level<2:
            self.PatientE.setVisible(False)
            self.PatientQ.setVisible(False)
            self.dangerI.setVisible(False)
        self.result = GetUserSub(cursor, current_uid)
        self.initial()
        self.Subp.clicked.connect(self.DispSub)
        self.Wholep.clicked.connect(self.DispWhole)
        self.dangerQ_2.clicked.connect(self.OpenSub)
        self.dangerI.clicked.connect(self.OpenDangerE)
        self.dangerQ.clicked.connect(self.OpenDangerQ)
        self.Auth.clicked.connect(self.OpenAuth)
        self.history.clicked.connect(self.OpenHistory)
        self.PatientQ.clicked.connect(self.OpenPatientQ)
    def initial(self):
        self.DispSub()

    def DispSub(self):
        self.table1.clearContents()
        self.table1.setRowCount(0)
        if self.result==():
            self.DispWhole()
            return

        for provinceid in self.result:
            row = self.table1.rowCount()
            self.table1.setRowCount(row + 1)
            Provincename = ProivinceId_to_name(cursor,provinceid)
            self.table1.setItem(row,0,QTableWidgetItem(Provincename))
            Pinfo = QueryIntimeData(cursor,provinceid)[0]
            n = len(Pinfo)
            for i in range(n):
                self.table1.setItem(row, i+1, QTableWidgetItem(str(Pinfo[i])))
    def DispWhole(self):
        self.table1.clearContents()
        self.table1.setRowCount(0)
        result = list(range(1, 35))
        for provinceid in result:
            row = self.table1.rowCount()
            self.table1.setRowCount(row + 1)
            Provincename = ProivinceId_to_name(cursor,provinceid)
            self.table1.setItem(row,0,QTableWidgetItem(Provincename))
            Pinfo = QueryIntimeData(cursor,provinceid)[0]
            n = len(Pinfo)
            for i in range(n):
                self.table1.setItem(row, i+1, QTableWidgetItem(str(Pinfo[i])))
    def OpenSub(self):
        self.window_sub = Sub()
        self.window_sub.show()
    def OpenDangerE(self):
        self.window_DangerE = DangerEdit()
        self.window_DangerE.show()
    def OpenDangerQ(self):
        self.window_dangerQ = DangerQuery()
        self.window_dangerQ.show()
    def OpenAuth(self):
        self.window_Auth = shouquan()
        self.window_Auth.show()
    def OpenHistory(self):
        self.window_history = history()
        self.window_history.show()
    def OpenPatientQ(self):
        self.window_patientQ = patientQ()
        self.window_patientQ.show()

class Sub(QMainWindow, Ui_SubWindow):
    def __init__(self, parent=None):
        super(Sub, self).__init__(parent)
        self.setupUi(self)
        self.label_36.setVisible(False)
        self.check_box = [self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,
                     self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20,self.c21,self.c22,
                     self.c23,self.c24,self.c25,self.c26,self.c27,self.c28,self.c29,self.c30,self.c31,self.c32,self.c33,self.c34]
        self.Subinfo = GetUserSub(cursor,current_uid)
        for subi in self.Subinfo:
            self.check_box[subi[0]-1].setChecked(True)
        self.pushButton.clicked.connect(self.Subnew)

    def Subnew(self):
        for i in range(34):
            if self.check_box[i].isChecked() and (i+1,) not in self.Subinfo:
                UserSubs(cursor,i+1,current_uid,db)
        self.label_36.setVisible(True)
class DangerEdit(QMainWindow, Ui_DangerEWindow):
    def __init__(self, parent=None):
        super(DangerEdit, self).__init__(parent)
        self.setupUi(self)
        self.Disp()
        self.success = chenggong()
        self.fail = shibai()
        self.pushButton.clicked.connect(self.charu)
        self.pushButton_2.clicked.connect(self.shanchu)
        self.pushButton_3.clicked.connect(self.xiugai)
    def xiugai(self):
        before_number = self.insert1_5.text()
        before_date = self.insert2_5.date().toString("yyyy-MM-dd")
        after_number = self.insert1_4.text()
        after_date = self.insert2_4.date().toString("yyyy-MM-dd")
        flag = ModifyDangerCar(cursor,[before_date,before_number],[after_date,after_number],db)
        if flag==1:
            self.success.show()
        else:
            self.fail.show()
    def shanchu(self):
        number = self.insert1_2.text()
        date = self.insert2_2.date().toString("yyyy-MM-dd")
        flag = deleteDangerousCar(cursor,[date,number],db)
        if flag==1:
            self.success.show()
        else:
            self.fail.show()


    def charu(self):
        number = self.insert1.text()
        date = self.insert2.date().toString("yyyy-MM-dd")
        traffic_id = GetDangerNumber(cursor)+1
        flag = insertdangerousCar(cursor,[traffic_id,date,number],db)
        if flag==1:
            self.success.show()
        else:
            self.fail.show()

    def Disp(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        result = GetDangerCar(cursor)
        for info in result:
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row+1)
            n = len(info)
            for i in range(n):
                ele = str(info[i])
                self.tableWidget.setItem(row,i,QTableWidgetItem(ele))

class DangerQuery(QMainWindow, Ui_DangerQuery):
    def __init__(self, parent=None):
        super(DangerQuery, self).__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.chaxun)

    def chaxun(self):
        number = self.number.text()
        date = self.date.date().toString("yyyy-MM-dd")
        flag = QueryDangerousCar(cursor,date,number)
        if flag==0:
            self.meishi = meishi()
            self.meishi.show()
        else:
            self.wandan = wandan()
            self.wandan.show()

class shouquan(QMainWindow, Ui_shouquan):
    def __init__(self, parent=None):
        super(shouquan, self).__init__(parent)
        self.setupUi(self)
        self.disp()
        self.success = chenggong()
        self.fail = shibai()
        self.pushButton.clicked.connect(self.disp)
        self.button1.clicked.connect(self.giveAuth)
        self.button2.clicked.connect(self.recallAuth)
        self.button2_3.clicked.connect(self.deleteAuth)
    def recallAuth(self):
        uid = self.id2.text()
        Pname = self.xiala2.currentText()
        ProId = ProivinceName_to_Id(cursor,Pname)
        f1 = ExamAuthRepeat(cursor,uid,ProId)
        if f1==0:
            self.fail.show()
        else:
            flag = RecallAuth(cursor,db,uid,ProId)
            if flag==1:
                self.success.show()
            else:
                self.fail.show()
    def deleteAuth(self):
        uid = self.id2_3.text()
        flag = DeleteAuth(cursor,db,uid)
        if flag==1:
            self.success.show()
        else:
            self.fail.show()

    def giveAuth(self):
        uid = self.id1.text()
        Pname = self.xiala1.currentText()
        ProId = ProivinceName_to_Id(cursor,Pname)
        f1 = ExamAuthRepeat(cursor,uid,ProId)
        if f1==0:
            flag = GiveAuth(cursor,db,uid,ProId)
            if flag==1:
                self.success.show()
            else:
                self.fail.show()
        else:
            self.fail.show()

    def disp(self):
        self.table1.clearContents()
        self.table1.setRowCount(0)
        allAuth = GetAllAuth(cursor)
        for auth in allAuth:
            row = self.table1.rowCount()
            self.table1.setRowCount(row + 1)
            uid = auth[0]
            self.table1.setItem(row,0,QTableWidgetItem(str(uid)))
            Uname = UseridToUsername(cursor,uid)
            self.table1.setItem(row, 1, QTableWidgetItem(Uname))
            proId = auth[1]
            if proId == 0:
                self.table1.setItem(row, 2, QTableWidgetItem("NA"))
                self.table1.setItem(row, 3, QTableWidgetItem("NA"))
            else:
                ProName = ProivinceId_to_name(cursor,proId)
                self.table1.setItem(row, 2, QTableWidgetItem(str(proId)))
                self.table1.setItem(row, 3, QTableWidgetItem(ProName))

            authType = auth[2]
            self.table1.setItem(row, 4, QTableWidgetItem(str(authType)))

class history(QMainWindow, Ui_history):
    def __init__(self, parent=None):
        super(history, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.disp)
    def disp(self):
        Pname = self.xiala2.currentText()
        ProId = ProivinceName_to_Id(cursor,Pname)
        start_date = self.date1.date().toString("yyyy-MM-dd")
        end_date = self.dateEdit_2.date().toString("yyyy-MM-dd")
        result = QueryByDateAndProvince(cursor,[start_date,end_date],ProId)
        self.table1.clearContents()
        self.table1.setRowCount(0)
        for re in result:
            row = self.table1.rowCount()
            self.table1.setRowCount(row + 1)
            self.table1.setItem(row,0,QTableWidgetItem(Pname))
            self.table1.setItem(row, 1, QTableWidgetItem(str(re[0])))
            self.table1.setItem(row,2,QTableWidgetItem(str(re[1])))
            self.table1.setItem(row, 3, QTableWidgetItem(str(re[2])))
            self.table1.setItem(row, 4, QTableWidgetItem(str(re[3])))
            self.table1.setItem(row, 5, QTableWidgetItem(str(re[4])))
            self.table1.setItem(row, 6, QTableWidgetItem(str(re[5])))

class patientQ(QMainWindow, Ui_PatientQ):
    def __init__(self, parent=None):
        super(patientQ, self).__init__(parent)
        self.setupUi(self)
        #self.xiala1.show()
        self.success = chenggong()
        self.fail = shibai()
        self.pushButton.clicked.connect(self.query)
    def query(self):
        params = []
        sql = "select * from patient natural join patient_status where ("
        if self.checkBox.isChecked():
            pname = self.lineEdit.text()
            params.append("%"+pname+"%")
            sql = sql+ "Pname like %s ) and ("
        provinceList = self.comboBox.Selectlist()
        if provinceList!=[]:
            n = len(provinceList)
            for i in range(n):
                ProId = ProivinceName_to_Id(cursor,provinceList[i])
                if i!=n-1:
                    sql = sql+"Province_id ="+str(ProId)+" or "
                else:
                    sql = sql+" Province_id ="+str(ProId)+") and ("
        statusList = self.comboBox_2.Selectlist()
        if statusList !=[]:
            n = len(statusList)
            for i in range(n):
                if i!=n-1:
                    sql = sql+"Pstatus =" +statusList[i]+ " or "
                else:
                    sql = sql + "Pstatus =" + statusList[i] + ") and ("

        before = self.dateEdit.date().toString("yyyy-MM-dd")
        after = self.dateEdit_2.date().toString("yyyy-MM-dd")
        params.append(before)
        params.append(after)
        sql = sql+ "Birthday >= %s" + " and Birthday <= %s" + " )"
        print(sql)
        try:
            cursor.execute(sql,params)
            result = cursor.fetchall()
            self.disp(result)
        except:
            self.fail.show()

    def disp(self,result):
        STATUS = {1:'治愈',2:'疑似',3:'确诊',4:"死亡"}
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for re in result:
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row+1)
            proName = ProivinceId_to_name(cursor,re[3])
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(re[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(re[2])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(re[1])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(proName))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(re[4])))
            print(re[5])
            self.tableWidget.setItem(row, 5, QTableWidgetItem(STATUS[re[5]]))

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
