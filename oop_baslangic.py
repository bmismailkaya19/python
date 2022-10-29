# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:27:36 2022

@author: İsmail Kaya

"""
import matplotlib.pyplot as plt
class Koordinatlar:
    
    def __init__(self,baslangıc_x,baslangıc_y):
        
        self.x = baslangıc_x
        self.y = baslangıc_y
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y
    def toplama(self):
        return self.x+self.y
    def cıkarma(self):
        return self.x-self.y
    def carpma(self):
        return self.x*self.y
    def orjine_uzaklik(self):
        return ((self.x)**2+(self.y)**2)**0.5
    def plot(self):
        plt.plot(self.x,self.y, marker='o',markersize=10)
        plt.show()
        
        
a = Koordinatlar(3, 4)
print(a.returnX())
print(a.returnY())
print(a.toplama())
print(a.cıkarma())
print(a.carpma())
print(a.orjine_uzaklik())
a.plot()
    
    
