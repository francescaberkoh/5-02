'''
Created on Apr 22, 2019

@author: Francesca
'''
from tkinter import *

import random

root = Tk()

list= []
for n in range(0,random.randint(1,10)):
    list.append(random.randint(1,20))

Label1 = Label(root, text= list)
Label1.pack()


def findlargest(numberlist):
    largest= numberlist[0]
    for value in numberlist:
        if value > largest:
            largest = value
    return largest 
    
def output(ans):
    ans= Label(root, text=ans) 
    ans.pack()
    
    
sendb = Button (root, text = "Largest #", command = lambda: output(findlargest(list)))
sendb.pack()
   
root.mainloop()
