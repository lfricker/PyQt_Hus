from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
from HusMainUi import Ui_Dialog as HusMainUi
import time

class Hus(HusMainUi):
   def __init__(self):
      super(Hus, self).__init__()
      self.init()

   def init(self):
      self.currentPlayer = "a"
      self.state = "idle"
      self.app = QtWidgets.QApplication(sys.argv)
      self.Dialog = QtWidgets.QDialog()
      self.setupUi(self.Dialog)
      self.handstones = 0

      self.setButtons()
      self.pb_start.clicked.connect(self.startcb)

      self.Dialog.show()
      sys.exit(self.app.exec_())

   def setButtons(self):

      # create button list
      self.a_buttons = []
      self.a_buttons.append(self.pb_a00)
      self.a_buttons.append(self.pb_a01)
      self.a_buttons.append(self.pb_a02)
      self.a_buttons.append(self.pb_a03)
      self.a_buttons.append(self.pb_a04)
      self.a_buttons.append(self.pb_a05)
      self.a_buttons.append(self.pb_a06)
      self.a_buttons.append(self.pb_a07)
      self.a_buttons.append(self.pb_a08)
      self.a_buttons.append(self.pb_a09)
      self.a_buttons.append(self.pb_a10)
      self.a_buttons.append(self.pb_a11)
      self.a_buttons.append(self.pb_a12)
      self.a_buttons.append(self.pb_a13)
      self.a_buttons.append(self.pb_a14)
      self.a_buttons.append(self.pb_a15)

      self.b_buttons = []
      self.b_buttons.append(self.pb_b00)
      self.b_buttons.append(self.pb_b01)
      self.b_buttons.append(self.pb_b02)
      self.b_buttons.append(self.pb_b03)
      self.b_buttons.append(self.pb_b04)
      self.b_buttons.append(self.pb_b05)
      self.b_buttons.append(self.pb_b06)
      self.b_buttons.append(self.pb_b07)
      self.b_buttons.append(self.pb_b08)
      self.b_buttons.append(self.pb_b09)
      self.b_buttons.append(self.pb_b10)
      self.b_buttons.append(self.pb_b11)
      self.b_buttons.append(self.pb_b12)
      self.b_buttons.append(self.pb_b13)
      self.b_buttons.append(self.pb_b14)
      self.b_buttons.append(self.pb_b15)

      # create cb list
      self.a_button_cbs = []
      self.a_button_cbs.append(lambda ch, arg = "a00": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a01": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a02": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a03": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a04": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a05": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a06": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a07": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a08": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a09": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a10": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a11": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a12": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a13": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a14": self.buttonHandler(arg))
      self.a_button_cbs.append(lambda ch, arg = "a15": self.buttonHandler(arg))

      self.b_button_cbs = []
      self.b_button_cbs.append(lambda ch, arg = "b00": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b01": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b02": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b03": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b04": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b05": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b06": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b07": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b08": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b09": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b10": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b11": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b12": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b13": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b14": self.buttonHandler(arg))
      self.b_button_cbs.append(lambda ch, arg = "b15": self.buttonHandler(arg))

      # connect buttons with cbs
      for i in range(16):
         self.a_buttons[i].clicked.connect(self.a_button_cbs[i])
         self.b_buttons[i].clicked.connect(self.b_button_cbs[i])

   def buttonHandler(self, button):
      button_nr = int(re.findall('\d+', button)[0])
      print("Button ", button_nr, " clicked, current state: ", self.state)
      player = button[0]
      if player == self.currentPlayer:
         if self.state == "ready":
            self.state == "working"
            self.move(player, button_nr)
            if self.currentPlayer == "a":
               self.currentPlayer = "b"
            else:
               self.currentPlayer = "a"
            self.state = "ready"

   def move(self, player, start_pos):
      moveDelayS = 0.1
      handstones = 0
      if player == "a":
         self.myButtons = self.a_buttons
         self.enemyButtons = self.b_buttons
      else:
         self.myButtons = self.b_buttons
         self.enemyButtons = self.a_buttons

      currentpos = start_pos
      self.handstones = int(self.myButtons[start_pos].text())
      print(str(self.edithandstones(0)))
      if self.edithandstones(0) < 2:
         # bad starting point... you failed
         return

      # clear the starting position
      self.myButtons[start_pos].setText("0")

      # start the loop
      while True:
         # simple moving until all stones are used
         while self.edithandstones(0) > 0:
            currentpos = (currentpos + 1) % 16
            self.myButtons[currentpos].setText(str(int(self.myButtons[currentpos].text()) + 1))
            self.setButtonColor(self.myButtons[currentpos], "move")

            self.edithandstones(-1)
            self.app.processEvents()
            time.sleep(moveDelayS)
            self.setButtonColor(self.myButtons[currentpos], "basic")
         
         if int(self.myButtons[currentpos].text()) < 2:
            # not enouth stones to continue
            print("Move over")
            self.setButtonColor(self.myButtons[currentpos], "stop")
            #get a and b stones and print to lables
            a_ammount = 0
            a_save = False
            b_ammount = 0
            b_save = False
            for i in range(16):
               a_val = int(self.a_buttons[i].text())
               if a_val > 1:
                  a_save = True
               a_ammount = a_ammount + a_val
               b_val = int(self.b_buttons[i].text())
               if b_val > 1:
                  b_save = True
               b_ammount = b_ammount + b_val
            # check if one got only fields with 0 or 1. if so other player wins
            if not b_save:
               print("A wins!")
               self.l_aWins.setText(str( int(self.l_aWins.text()) + 1))
               self.startcb()
            if not a_save:
               print("B wins!")
               self.l_bWins.setText(str( int(self.l_bWins.text()) + 1))
               self.startcb()

            self.label_5.setText(str(a_ammount))
            self.label_6.setText(str(b_ammount))
            time.sleep(moveDelayS)
            self.setButtonColor(self.myButtons[currentpos], "basic")
            return
         # try to rob
         self.edithandstones(self.robbery(player, currentpos))
         self.edithandstones(int(self.myButtons[currentpos].text()))
         self.setButtonColor(self.myButtons[currentpos], "pickup")
         print("adding ",int(self.myButtons[currentpos].text())," stones from current field. Total of ", handstones, " available now")
         self.myButtons[currentpos].setText("0")
         time.sleep(moveDelayS)
         self.setButtonColor(self.myButtons[currentpos], "basic")

   def robbery(self, player, position):
      stolen = 0
      if player == "a" and position > 7 or player == "b" and position < 8:
         opponentField = 15 - position
         if(int(self.enemyButtons[opponentField].text())) > 0:
            self.setButtonColor(self.myButtons[position], "robbing")
            self.setButtonColor(self.enemyButtons[position], "stolen")
            self.setButtonColor(self.enemyButtons[opponentField], "stolen")
            # steal the stones
            stolen = stolen + int(self.enemyButtons[opponentField].text())
            stolen = stolen + int(self.enemyButtons[position].text())
            self.enemyButtons[opponentField].setText("0")
            self.enemyButtons[position].setText("0")
            print("Robbing ", stolen, " Stones")
            time.sleep(0.5)
            self.setButtonColor(self.enemyButtons[position], "basic")
            self.setButtonColor(self.enemyButtons[opponentField], "basic")
         self.setButtonColor(self.myButtons[position], "basic")
      return stolen

   def setButtonColor(self, button, color):
      basic = """QPushButton {
      color: #333;
      border: 2px solid #555;
      border-radius: 30px;
      border-style: outset;
      background: qradialgradient(
      cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
      radius: 1.35, stop: 0 #fff, stop: 1 #888
      );
      padding: 5px;
      }
      QPushButton:hover {
      background: qradialgradient(
      cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
      radius: 1.35, stop: 0 #fff, stop: 1 #bbb
      );
      }
      """
      if color == "basic":
         #button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #969e9b;")
         button.setStyleSheet(basic)
      elif color == "move":
         button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #68d496;")
      elif color == "robbing":
         button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #db8b51;")
      elif color == "stolen":
         button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #db5675;")
      elif color == "stop":
         button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #ff1212;")
      elif color == "pickup":
         button.setStyleSheet("border-radius : 30; border : 2px solid black; background-color: #55cfd4;")
      self.app.processEvents()

   def startcb(self):
      for i in range(16):
         self.a_buttons[i].setText("2")
         self.b_buttons[i].setText("2")

      for i in range(12, 16):
         self.b_buttons[i].setText("1")
      for i in range(4,8):
         self.a_buttons[i].setText("1")
      self.state = "ready"

      print("Round started")

   def edithandstones(self, toAdd):
      self.handstones = self.handstones + toAdd
      self.l_handstones.setText(str(self.handstones))
      return self.handstones
app = Hus()
