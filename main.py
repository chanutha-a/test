import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from home import Main

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()

        # Check if username or password fields are blank
        if not username or not password:
            self.error.setText("Please enter both username and password")
        else:
            conn = sqlite3.connect(r"C:\Users\Chanu\Desktop\CS Project\FinanceApp\FinanceAPP - Copy.db")
            print("Successfully Connected")
            cur = conn.cursor()
            q = 'SELECT Password FROM Users WHERE Username = ?'
            cur.execute(q, (username,))
            result = cur.fetchone()
            if result is None:
                self.error.setText("Username not found")
            else:
                passresult = result[0]
                if passresult == password:
                    self.error.setText("")
                    print("Successfully logged in with username: ", username, "and password:", password)
                    self._new_window = Main()
                    self._new_window.show()
                else:
                    self.error.setText("Password is incorrect")

            # Close the cursor and connection
            cur.close()
            conn.close()

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backBtn.clicked.connect(self.gotologin)

    def createaccfunction(self):
        username = self.username.text()
        password = self.password.text()
        confirm_pass = self.confirmpass.text()

        # Check if username or password fields are blank
        if not username or not password or not confirm_pass:
            self.error.setText("Please fill out all fields")
        # Check if passwords match
        elif password != confirm_pass:
            self.error.setText("Passwords do not match")
        else:
            try:
                conn = sqlite3.connect(r"C:\Users\Chanu\Desktop\CS Project\FinanceApp\FinanceAPP - Copy.db")
                print("Successfully Connected")
                cur = conn.cursor()
                q = 'INSERT INTO Users(Username, Password) VALUES (?, ?)'
                cur.execute(q, (username, password))
                conn.commit()
                print("Successfully created acc with username: ", username, "and password: ", password)
                self.error.setText("Account created successfully")
            except sqlite3.Error as e:
                print("SQLite error:", e)
            finally:
                # Close the cursor and connection
                cur.close()
                conn.close()

    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)




app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1900)
widget.setFixedHeight(1070)
widget.show()
sys.exit(app.exec_())
