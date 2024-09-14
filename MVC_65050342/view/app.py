import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout
    
) 
from PyQt5.QtGui import QFont
#เชื่อมmvc
from controller.inputCheck import checkInput
from controller.calculate_typeMilk import calculate_milk


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.totalMilk = {}
        self.bsodCowIDs = set()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(200,200, 600, 400)  # X, Y, Width, Height

        self.layout = QFormLayout()
        self.layout.setSpacing(20)

        font = QFont()
        font.setFamily("Comic Sans MS")  # กำหนดชนิดของฟอนต์
        font.setPointSize(10)
        font.setBold(True)

        self.cowId = QLabel("Enter the cow id:")
        self.cowId.setFont(font)
        self.cowIdInput = QLineEdit()
        self.cowIdInput.setMinimumHeight(35)
        self.layout.addRow(self.cowId, self.cowIdInput)
        
        self.cowColor = QLabel("Enter the cow color:")
        self.cowColor.setFont(font)
        self.cowColorInput = QLineEdit()
        self.cowColorInput.setMinimumHeight(35)
        self.layout.addRow(self.cowColor, self.cowColorInput)
        
        self.cowAge = QLabel("Enter the cow Age:")
        self.cowAge.setFont(font)
        self.cowAgeInput = QLineEdit()
        self.cowAgeInput.setMinimumHeight(35)
        self.layout.addRow(self.cowAge, self.cowAgeInput)
       
        #ปุ่มกด
        button = QPushButton('check', self)
        button.setFont(font)
        button.setStyleSheet('''
            QPushButton {
            background-color: #e18acf;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 10px 20px;
            border: 1px solid #ccc;
            border-radius: 15px;
            text-align: center;
            }
           QPushButton:hover {
                background-color: #e2a2d5;
            } 
        ''')
        button.clicked.connect(self.on_click) #เมื่อกดปุ่ม ให้เรียกฟังชั่น
        self.layout.addWidget(button)
        
        self.totalMilkLabel = QLabel("total milk:")
        self.totalMilkLabel.setFont(font)
        
        self.layout.addWidget(self.totalMilkLabel)
        

        self.setLayout(self.layout)

        self.show()
        
        #นับจำนวนขวดนม
        self.totalMilkCount = 0

    def on_click(self): #เรียกฟังชั่น
        cowId = self.cowIdInput.text()
        cowColor = self.cowColorInput.text()
        cowAge = self.cowAgeInput.text()
        isValid = checkInput(cowId, cowColor, cowAge) 
        print("Is Valid:", isValid)

        if isValid:
            #เรียกฟังชั่น
            type = calculate_milk(cowId, cowColor, cowAge) 
            QMessageBox.information(self, "Cow Information", f"Cow ID: {cowId}\nCow Color: {cowColor}\nCow Age: {cowAge}")
            #แสดงจากที่คำนวณcalulate milk
            if type == 'BSOD (Breast Supply Operation Down – วัวผลิตน้ํานมไม่ได้)':
                reply = QMessageBox.question(self, "Error", "This cow cannot produce milk. Do you want to reset?", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.totalMilk = {}
                    self.bsodCowIDs = set()
                else:
                    self.bsodCowIDs.add(cowId)
            else:
                QMessageBox.about(self, "Success", f"Producing {type} type")
                if cowId not in self.totalMilk:
                    self.totalMilk[cowId] = 0
                self.totalMilk[cowId] += 1 
                self.totalMilkCount += 1 #นับจำนวนขวดนม
                self.totalMilkLabel.setText(f"Total Milk: {self.totalMilkCount}")
                
                QMessageBox.information(self, "Total Milk", f"Total Drinking Yogurt: {self.totalMilk.get('drinking yogurth', 0)}\n"
                                                        f"Total White Milk: {self.totalMilk.get('white', 0)}\n"
                                                        f"Total Chocolate Milk: {self.totalMilk.get('chocolate', 0)}\n"
                                                        f"Total Milk: {self.totalMilkCount}")
        else:
            #บอกข้อผิดพลาดให้เห็นว่าผิดอะไร
            QMessageBox.warning(self, "Error", "Please check the input again:\n"
                                             "cowId must be 8 digits and start with 1-9\n"
                                             "cowId not start with 0\n"
                                             "cowColor must be brown or white\n"
                                             "cowAge must be a number")
            
