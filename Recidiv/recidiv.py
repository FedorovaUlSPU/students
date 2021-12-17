from PyQt5 import QtWidgets
from unp import Ui_MainWindow  # импорт сгенерированного файла
import sys
 
t0 = ['107.1','108','113','114','115']
t1 = ['106.2','107.2','120','126.1','150.1']
t2 = ['110.1','111.1','117.2','128.2','132.1']
t3 = ['105','111.3','126.2','131.3','134.3']
t = t0 + t1 + t2 + t3
ts = sorted(t)
tsup = [' '] + ts

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(ts)
        self.ui.comboBox_2.addItems(tsup)
        self.ui.comboBox_3.addItems(ts)

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        st1 = self.ui.comboBox.currentText()
        st2 = self.ui.comboBox_2.currentText()
        st3 = self.ui.comboBox_3.currentText()
        age = int(self.ui.textEdit.toPlainText())
        r = 0
        s1 = self.ui.checkBox.isChecked()
        s2 = self.ui.checkBox_2.isChecked()
#2. Рецидив преступлений признается опасным:
#а) при совершении лицом тяжкого преступления,
#   за которое оно осуждается к реальному лишению свободы,
#   если ранее это лицо два или более раза было осуждено за умышленное преступление
#   средней тяжести к лишению свободы;
        if st3 in t2:
            if st1 in t1 and st2 in t1 and s1 and s2:
                r = 1
#б) при совершении лицом тяжкого преступления, если ранее оно было осуждено за тяжкое
#       или особо тяжкое преступление к реальному лишению свободы.
        if st3 in t2:
            if st1 in t2 or st1 in t3:
                r = 1
#3. Рецидив преступлений признается особо опасным:
#а) при совершении лицом тяжкого преступления, за которое оно осуждается к реальному лишению свободы,
#    если ранее это лицо два раза было осуждено за тяжкое преступление к реальному лишению свободы;
        if st3 in t2:
            if st1 in t2 and st2 in t2 and s1 and s2:
                r = 2
#б) при совершении лицом особо тяжкого преступления, если ранее оно два раза было осуждено за тяжкое
#   преступление или ранее осуждалось за особо тяжкое преступление.
        if st3 in t3:
            if (st1 in t2 and st2 in t2) or st1 in t3:
                r = 2
#4. При признании рецидива преступлений не учитываются:
#а) судимости за умышленные преступления небольшой тяжести;
#б) судимости за преступления, совершенные лицом в возрасте до восемнадцати лет;
        if age < 19:
              r = 0
        
        if r == 0:
              self.ui.label_7.setText('Преступление не является рецидивом')
              self.ui.label_7.adjustSize()
        elif r == 1:
              self.ui.label_7.setText('Опасный рецидив')
              self.ui.label_7.adjustSize()
        elif r == 2:
              self.ui.label_7.setText('Особо опасный рецидив')
              self.ui.label_7.adjustSize()
        
          
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
