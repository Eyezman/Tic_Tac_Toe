from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class tic_tac_toe(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 400, 300, 250)
        
        self.text_input1 = QLineEdit(self)
        self.text_input1.move(10,5)
        self.text_input1.resize(50,50)
        self.text_input1.setAlignment(Qt.AlignCenter)
        self.text_input1.setFont(QFont("Courier New"))
        
        
        self.text_input2 = QLineEdit(self)
        self.text_input2.move(61,5)
        self.text_input2.resize(50,50)
        self.text_input2.setAlignment(Qt.AlignCenter)
        self.text_input2.setFont(QFont("Courier New"))
        
        self.text_input3 = QLineEdit(self)
        self.text_input3.move(112,5)
        self.text_input3.resize(50,50)
        self.text_input3.setAlignment(Qt.AlignCenter)
        self.text_input3.setFont(QFont("Courier New"))
        
        self.text_input4 = QLineEdit(self)
        self.text_input4.move(10,56)
        self.text_input4.resize(50,50)
        self.text_input4.setAlignment(Qt.AlignCenter)
        self.text_input4.setFont(QFont("Courier New"))
        
        self.text_input5 = QLineEdit(self)
        self.text_input5.move(61,56)
        self.text_input5.resize(50,50)
        self.text_input5.setAlignment(Qt.AlignCenter)
        self.text_input5.setFont(QFont("Courier New"))
        
        self.text_input6 = QLineEdit(self)
        self.text_input6.move(112,56)
        self.text_input6.resize(50,50)
        self.text_input6.setAlignment(Qt.AlignCenter)
        self.text_input6.setFont(QFont("Courier New"))
         
        self.text_input7 = QLineEdit(self)
        self.text_input7.move(10,107)
        self.text_input7.resize(50,50)
        self.text_input7.setAlignment(Qt.AlignCenter)
        self.text_input7.setFont(QFont("Courier New"))
        
        self.text_input8 = QLineEdit(self)
        self.text_input8.move(61,107)
        self.text_input8.resize(50,50)
        self.text_input8.setAlignment(Qt.AlignCenter)
        self.text_input8.setFont(QFont("Courier New"))
                
        self.text_input9 = QLineEdit(self)
        self.text_input9.move(112,107)
        self.text_input9.resize(50,50)
        self.text_input9.setAlignment(Qt.AlignCenter)
        self.text_input9.setFont(QFont("Courier New"))

        
        self.button = QPushButton(self,text = "check")
        self.button.move(38,165)
        self.button.resize(90,27)
        
        self.button2 = QPushButton(self,text = "clear")
        self.button2.move(38,193)
        self.button2.resize(90,27)
        
        
        self.button.clicked.connect(self.change_label_text)  
        
        self.button2.clicked.connect(self.clear_squares)
        
        self.title = QLabel(self)
        self.title.setText("Play")
        self.title.move(170,80)
            
                
    def change_label_text(self):    
   
        a1 = self.text_input1.text()
        a2 = self.text_input2.text()
        a3 = self.text_input3.text()
        a4 = self.text_input4.text()
        a5 = self.text_input5.text()
        a6 = self.text_input6.text()
        a7 = self.text_input7.text()
        a8 = self.text_input8.text()
        a9 = self.text_input9.text()
        
        if (a1=="X" or a1=="O" or a1==str()) and (a2=="X" or a2=="O" or a2==str()) and (a3=="X" or a3=="O" or a3==str()) and (a4=="X" or a4=="O" or a4==str()) and  (a5=="X" or a5=="O" or a5==str()) and  (a6=="X" or a6=="O" or a6==str()) and  (a7=="X" or a7=="O" or a7==str()) and  (a8=="X" or a8=="O" or a8==str()) and  (a9=="X" or a9=="O" or a9==str()):
            
            self.title.setText("Play")
                
        else:
            self.title.setText("Invalid Input") 
            
        if (a1=="X" and a2=="X" and a3=="X") or (a4=="X" and a5=="X" and a6=="X") or (a7=="X" and a8=="X" and a9=="X"):
         
            self.title.setText("X Won")
        
        if (a1=="O" and a2=="O" and a3=="O") or (a4=="O" and a5=="O" and a6=="O") or (a7=="O" and a8=="O" and a9=="O"):
             
            self.title.setText("O Won")
             
        if (a1=="X" and a4=="X" and a7=="X") or (a2=="X" and a5=="X" and a8=="X") or (a3=="X" and a6=="X" and a9=="X"):
    
            self.title.setText("X Won")
            
        if (a1=="O" and a4=="O" and a7=="O") or (a2=="O" and a5=="O" and a8=="O") or (a3=="O" and a6=="O" and a9=="O"):
    
            self.title.setText("O Won")

        if (a1=="X" and a5=="X" and a9=="X") or  (a3=="X" and a5=="X" and a7=="X"):
                        
            self.title.setText("X Won")
            
        if (a1=="O" and a5=="O" and a9=="O") or  (a3=="O" and a5=="O" and a7=="O"):
                         
            self.title.setText("O Won")   


            
    def clear_squares(self):

        self.text_input1.clear()
        self.text_input2.clear()
        self.text_input3.clear()
        self.text_input4.clear()
        self.text_input5.clear()
        self.text_input6.clear()
        self.text_input7.clear()
        self.text_input8.clear()
        self.text_input9.clear()    


           
app = QtWidgets.QApplication((sys.argv))

window =  tic_tac_toe()

window.show()

sys.exit(app.exec_())