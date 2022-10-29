# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:50:23 2022

@author: İsmail Kaya
"""

#Hadi turtle drawings ile harika çizimler yapalim.

import turtle #turtle paketini import edelim
# turtle da kurulum yapiyoruz
turtle.bgcolor("black") # Arkaplan rengi
turtle.pensize(2)# Kalem boyutu
turtle.color("red")

# Simdi bir kare cizelim
turtle.forward(50)# 50 adım ileri gitmesini soyledik
turtle.left(90) # 90 derece dön
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.done() # Turtle ekranda kalmasını sagladik.