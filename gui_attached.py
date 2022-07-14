from audioop import add
import os.path
import random
from re import M
from sre_parse import FLAGS
import string
from unicodedata import numeric 
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import Image

class GUI(QDialog):
    def __init__(self):
        super(GUI,self).__init__()
        uic.loadUi("D:/My Projects/Python/ui/Interface.ui",self)
        # write interface destination
        self.show()
        
        self.GKButton.clicked.connect(self.generatekey)
        self.EButton.clicked.connect(self.encryption)
        self.DButton.clicked.connect(self.decryption)
    
    def decryption(self):
      address = self.L1Textbox.text()
      k = self.L2Textbox.text()
      r = self.L3Textbox.text()
      key = 0 
      rounds = 0
      pos = True
      try:
        key = int(k , base = 10)
        rounds = int(r , base = 10) 
      except ValueError:
          pos = False
          
      if(pos == True):
         for i in range(len(address)):
             if address[i] == "\\":
                address = address[:i] + "/" + address[i+1:]
    #    converting valid address
    
      pos = os.path.isfile(address)
    #  checking valid path
    
    # space left to check valid jpg image
    
      if(pos == False or key<1 or key>255 or rounds<1 or rounds>15):
          message = QMessageBox()
          message.setText("Wrong Path , File Name or Input")
          message.setWindowTitle("WARNING")
          message.exec_()
          return
      

      GUI.decrypt(address,key,rounds)
    
    def decrypt(address,key,rounds):
        file = open(address,"rb")
        image = file.read()
        file.close()
        
        # closing file pointer and taking value of image
        
        
        image = bytearray(image)
        
        for i  in range(len(address)-2,0,-1):
            if(address[i] == '.'):
                address = address[:i] + '-Decrypted' + address[i:]
                break
            
        print(address)
        
        file  = open(address,"wb")
        
    
        for l in range(0,rounds,1):
            for i,j in enumerate(image):
                image[i] = j ^ key
            key = (key+1) % 256
        
        file.write(image)
        file.close()
      
        message = QMessageBox()
        message.setText("Decryption Done")
        message.setWindowTitle("Success")
        message.exec_()
      
    
    def encryption(self):
      pos = True   
      address = self.L1Textbox.text()
      k = self.L2Textbox.text()
      r = self.L3Textbox.text()
      key = 0 
      rounds = 0
      try:
        key = int(k , base = 10)
        rounds = int(r , base = 10) 
      except ValueError:
          pos = False
      
 
      if(pos == True):
         for i in range(len(address)):
             if address[i] == "\\":
                address = address[:i] + "/" + address[i+1:]
    # str[:i] before i  str[startingidx : end_idx - 1]
      pos = os.path.isfile(address)
    #  checking valid path
      
      if(pos == True ):
         try:
            im = Image.open(address)
         except IOError:
             pos = False
    
    #  checking valid image or not
            

      
      
      if(pos == False or key<1 or key>255 or rounds<1 or rounds>15):
          message = QMessageBox()
          message.setText("Wrong Path , File Name or Input")
          message.setWindowTitle("WARNING")
          message.exec_()
          return
      

      GUI.encrypt(address,key,rounds)
      
      
      
    def encrypt(address,key,rounds):
      file  = open(address,"rb")
      image = file.read()
      file.close()
    
    #closing file pointer and taking values in image variable
      
      image = bytearray(image)
      for i in range(len(address)-1 , 0 , -1):
        
        if(address[i] == '.'):
            address = address[:i] + '-Encrypted' + address[i:]
            break
        # Getting Encrypted address
      print(address)

      file  = open(address,"wb")
    
      for l in range(0,rounds,1):
        for i,j in enumerate(image):
          image[i] = j ^ key
        key = (key+1) % 256
    #   encryption
          
      file.write(image)
      file.close()
      
      message = QMessageBox()
      message.setText("Encryption Successful!!!")
      message.setWindowTitle("Success")
      message.exec_()
      
      
             
    def generatekey(self):
      self.GKTextbox.setText(str(random.randint(1,255)))
    

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()
    
    
    
if __name__ == '__main__' :
    main()