import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from Gui.Login import Ui_MainWindow as Login_window
import pandas as pd
import os


class Login_window(QMainWindow, Login_window):
    def __init__(self):
        super(Login_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("登录窗口")
        self.pushButton.clicked.connect(self.on_login_button_clicked)
        self.pushButton_2.clicked.connect(self.on_exit_button_clicked)

    def on_login_button_clicked(self):
        print("登录按钮被点击了")
        # 在这里添加登录逻辑
        if self.get_input_text():
            print("登录成功")
        else:
            print("登录失败")

    def on_exit_button_clicked(self):
        print("退出按钮被点击了")
        # 在这里添加退出逻辑，例如关闭窗口或退出程序
        sys.exit()

    def get_input_text(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print("用户名:", username, "密码:", password)
        return check_password(username, password)

def check_password(n, p):
    for i in range(len(array)):
        if array[i][0] == n and array[i][1] == p:
            return True
    return False


def getUserInfo():
    print("当前工作目录：%s" % os.getcwd())
    data = pd.read_csv(r'user.csv', sep=',', header=0)
    global array
    array = data.values[0::, 0::]  # 读取全部行，全部列


if __name__ == '__main__':
    array = []
    getUserInfo()
    app = QApplication(sys.argv)
    window = Login_window()
    window.show()
    sys.exit(app.exec_())
