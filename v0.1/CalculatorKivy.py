# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:31:20 2019

@author: Starscream
"""

#Imports for Kivy and other dependancies 
from kivy.lang import Builder	
from kivy.uix.gridlayout import GridLayout
from kivy.properties import AliasProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
Config.set('graphics', 'width', '275')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', False)
test = "hello"
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from threading import Thread
import sys
from kivy.uix.textinput import TextInput
from datetime import date


#My Modules 
import Calculator
#import test

#Sys Modules
import re

#Builder for the application 
Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition

<MainMenu>:
    BoxLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "background.jpg" 
                
        #Results                 
        GridLayout:
            cols: 3
            rows: 5
            spacing: 10
            padding: 10
            width: 50
            pos_hint: {"top":0.77}
    
            
           
            #Top Buttons
            Button:
                text: "<-"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTNErase()
            Button:
                text: "CE"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTNCncl()   
            Button:
                text: "C"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTNClear()
            # Second Row 
            Button:
                text: "7"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN7()
            Button:
                text: "8"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN8()
            Button:
                text: "9"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN9()
            # Third Row 
            Button:
                text: "4"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN4()
            Button:
                text: "5"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN5()
            Button:
                text: "6"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN6()
            # Fourth Row 
            Button:
                text: "1"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN1()
            Button:
                text: "2"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN2()
            Button:
                text: "3"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN3()
            # Fifth Row 
            Button:
                text: "0"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTN0()
            Button:
                text: "."
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (1,1,1,0.75)
                on_release : root.BTNDeci()

            
    #Results or Output area           
    RelativeLayout:
        #pos_hint: {"right":1.,"top":1}
        #pos: 200, 200
        BoxLayout:
            pos_hint: {"right":0.5,"top":0.99}

            Label:
                
                text: "VEDA" 
                outline_width: 2
                outline_color: (1,1,1,0.75)  
                color: (0,0,0,1)
                font_size: sp(16)
                halign: 'center'
                font_name:"TakaoPMincho.ttf" 
                size: self.texture_size
                size_hint_y : None
                size_hint_x : None
        GridLayout:
            cols: 1
            rows: 3
            spacing: 10
            padding: 0
            width: 50
            pos_hint: {"right":1.05,"top":0.99} 
            
            
                
            TextInput:
                id : input
                text: ""
                readonly: True 
                on_text: root.inputupdate()
                font_name:"TakaoPMincho.ttf" 
                size_hint_x : None
                size_hint_y : None
                width: 230
                height : 25
                color: (1,1,1,1)
                foreground_color: (0, 0, 0, 1)
                font_size: sp(11)
                background_color: (1,1,1,0.75)
            TextInput:
                id : result
                text: ""
                readonly: True 
                font_name:"TakaoPMincho.ttf" 
                size_hint_x : None
                size_hint_y : None
                width: 230
                height : 25
                color: (1,1,1,0.75)
                foreground_color: (0, 0, 0, 1)
                font_size: sp(11)
                background_color: (1,1,1,0.75)
            
            
    #Numeric Operators    
    RelativeLayout:
        pos_hint: {"right":1.65,"top":1}
        #pos: 200, 200
        GridLayout:
            cols: 1
            rows: 5
            spacing: 10
            padding: 10
            width: 50
            pos_hint: {"top":0.77}
        
            Button:
                text: "/"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (0.28,0.58,0.66,1)
                on_release : root.BTNDiv()
            Button:
                text: "*"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (0.28,0.58,0.66,1)
                on_release : root.BTNMult()
            Button:
                text: "-"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (0.28,0.58,0.66,1)
                on_release : root.BTNSub()
            Button:
                text: "+"
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (0.28,0.58,0.66,1)
                on_release : root.BTNAdd()
            Button:
                text: "="
                size_hint_y : None
                size_hint_x : None
                height: 25
                width: 50
                color: (0,0,0,0.75)
                background_color: (0.28,0.58,0.66,1)
                on_release : root.BTNEquals()
        
                
                
    #Numeric Operators 
    
      
''')
    
    
    
    
#Main Screen function 
class MainMenu(Screen):
    
    #We can assign variables that we can use globally 
   
        
    def inputupdate(self):
        #To make it update if it doesn't
        pass
    #Control Buttons and funcitons 
    
    def BTNErase(self):
        #store the values in a list 
        a = self.ids.result.text
        a = a[:-1]
        self.ids.result.text = a
        
    def BTNCncl(self):
        self.ids.result.text = ""
    
    def BTNClear(self):
        self.ids.input.text = ""
        self.ids.result.text = ""
    def BTNEquals(self):
        #Passes the information to the calculator module 
        self.ids.input.text = ""
        a = Calculator.SingularMethod(self.ids.result.text)
        #A to list 
        b = list(str(a))
        print(b)
        a =a.strip()
        self.ids.input.text = str(a)
        print(a)
        

        
    def BTNDeci(self):
        a = self.ids.result.text

        #Count the number of present decimals 
        b = re.split('\d+' , a)
        deci = "."
        print(b)
        if deci in b:
            return
        else:
            self.ids.result.text = self.ids.result.text + str(".")

        '''
        #Check if the last character is an operator 
        a = a[s-1:s]
        
        Validate = ["."]   
        if a in Validate:
            a = a[:-1]
        '''
            
        
         
        
    #Operators and Functions 
    def BTNDiv(self):
        #Check if the last character is an operator 
        a = self.ids.result.text
        s = len(a) 
        print("Div", a[:-1])
        a = a[:-1]
        b = a
        a = a[s-2:s]
        print("Value of 2 " , a)
        Validate = ["+",'-','*','/',' ', "  "]   
        if a in Validate:
            print("hit")
            b= b[0:s-2]
            b = b + "/" + " "
            self.ids.result.text = b
        else:              
            self.ids.result.text = self.ids.result.text + " " + str("/") +" " 
        
    def BTNMult(self):
        #Check if the last character is an operator 
        a = self.ids.result.text
        s = len(a) 
        print("Div", a[:-1])
        a = a[:-1]
        b = a
        a = a[s-2:s]
        print("Value of 2 " , a)
        Validate = ["+",'-','*','/',' ', "  "]   
        if a in Validate:
            print("hit")
            b= b[0:s-2]
            b = b + "*" + " "
            self.ids.result.text = b
        else:              
            self.ids.result.text = self.ids.result.text + " " + str("*") + " " 
        
    def BTNSub(self):
        #Check if the last character is an operator 
        a = self.ids.result.text
        s = len(a) 
        print("Div", a[:-1])
        a = a[:-1]
        b = a
        a = a[s-2:s]
        print("Value of 2 " , a)
        Validate = ["+",'-','*','/',' ', "  "]   
        if a in Validate:
            print("hit")
            b= b[0:s-2]
            b = b + "-" + " "
            self.ids.result.text = b
        else:              
            self.ids.result.text = self.ids.result.text + " " + str("-") +" " 
        
    def BTNAdd(self):
        #Check if the last character is an operator 
        a = self.ids.result.text
        s = len(a) 
        print("Div", a[:-1])
        a = a[:-1]
        b = a
        a = a[s-2:s]
        print("Value of 2 " , a)
        Validate = ["+",'-','*','/',' ', "  "]   
        if a in Validate:
            print("hit")
            b= b[0:s-2]
            b = b + "+" + " "
            print(b)
            self.ids.result.text = b
        else:              
            self.ids.result.text = self.ids.result.text + " " + str("+") +" " 
        
    
    #Number Buttons and Functions 
    def BTN0(self):
        self.ids.result.text = self.ids.result.text + str(0)
    
    def BTN1(self):
        self.ids.result.text = self.ids.result.text + str(1)
        
    def BTN2(self):
        self.ids.result.text = self.ids.result.text + str(2)
        
    def BTN3(self):
        self.ids.result.text = self.ids.result.text + str(3)
    
    def BTN4(self):
        self.ids.result.text = self.ids.result.text + str(4)
        
    def BTN5(self):
        self.ids.result.text = self.ids.result.text + str(5)
        
    def BTN6(self):
        self.ids.result.text = self.ids.result.text + str(6)
        
    def BTN7(self):
        self.ids.result.text = self.ids.result.text + str(7)
        
    def BTN8(self):
        self.ids.result.text = self.ids.result.text + str(8)
    
    def BTN9(self):
        self.ids.result.text = self.ids.result.text + str(9)
    

def main():
    class GridLayoutApp(App):
        def build(self):
            self.title = "KA-VEDA"
            return sm
        def fappy(self):
            pass
        
    sm = ScreenManager()
    sm.add_widget(MainMenu(name='Main'))
    
    
    glApp = GridLayoutApp()
    glApp.run()


if __name__ == "__main__":
    main()

