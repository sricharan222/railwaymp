import turtle
from turtle import *
screen=turtle.Screen()
screen.bgcolor("white")
t=turtle.Pen()
t.color("black")


image='C:\\Users\\HI\\Documents\\Downloads\\1001698706430.jpg'



t.speed(10000)     
t.up()    

def square(f,d):
    for i in range(0,4):
        t.down()
        t.fd(f)
        t.left(d)
        t.up()
    
def position(x,y,a,b):
    t.setx(x)
    t.sety(y)
    square(a,b)

def platform(x,y):
    
    t.setx(x)
    t.sety(y)
    t.down()
    
    t.fd(300)
    t.left(90)
    t.fd(600)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(600)
    t.up()
def plat(x,y):
    
    t.setx(x)
    t.sety(y)
    t.down()
    
    t.left(180)
    t.fd(600)
    t.up()
    
    


position(-380,-280,100,90)
position(-380,-80,100,90)
position(-380,120,100,90)
position(270,-280,100,90)
position(270,-80,100,90)
position(270,120,100,90)
platform(-386,-300)
t.left(90)
platform(80,-300)
plat(-146,-300)
t.left(180)

plat(146,-300)
t.left(270)
position(-250,150,500,90)
position(-250,-150,50,90)
position(-250,50,50,90)
position(200,-150,50,90)
position(200,50,50,90)
t.left(90)



screen.mainloop()
