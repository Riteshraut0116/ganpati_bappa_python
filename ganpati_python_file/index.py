from turtle import*

title('CoderHuBhai')
bgcolor("black")
speed(4)
pencolor('red')
fillcolor('orange')

def CoderHu(x,y):
    penup()
    goto(x,y)
    pendown()

# trunk
CoderHu(-130,150)
seth(-120)
begin_fill()
circle(100,90)
circle(280,10)
circle(-120,90)
circle(-60,150)
circle(-30,60)
seth(-120)
circle(30,60)
circle(55,150)
circle(120,77)
circle(-100,115)
end_fill()
CoderHu(0,50)
seth(20)
begin_fill()
circle(-50,80)
circle(-200,70)
circle(-50,60)
seth(-20)
circle(50,70)
circle(205,70)
circle(50,85)
end_fill()
CoderHu(70,10)
seth(15)
begin_fill()
circle(90,120)
seth(-52)
circle(-90,110)
end_fill()

# eyes
def eye():
    seth(-55)
    begin_fill()
    circle(20,120)
    seth(-90)
    circle(-17,165)
    end_fill()
CoderHu(-100,110)
eye()
CoderHu(40,110)
eye()

# tilak
def cir(r):
    begin_fill()
    circle(r)
    end_fill()
CoderHu(0,150)
cir(10)
CoderHu(-2,125)
cir(8)
CoderHu(-4,105)
cir(5)

# crown
CoderHu(-80,200)
seth(30)
begin_fill()
circle(-150,60)
seth(141)
circle(120,80)
end_fill()
CoderHu(-70,225)
seth(30)
begin_fill()
circle(-120,60)
seth(141)
circle(95,80)
end_fill()
CoderHu(-30,280)
seth(-120)
begin_fill()
circle(20,250)
circle(-50,40)
seth(-100)
circle(50,42)
circle(-15,240)
end_fill()
CoderHu(-5,268)
cir(9)

# left ear
CoderHu(-160,130)
seth(120)
begin_fill()
circle(70,60)
circle(15,100)
circle(90,30)
circle(-15,40)
circle(90,30)
circle(20,100)
seth(-130)
circle(-20,100)
circle(-90,30)
circle(15,35)
circle(-90,50)
circle(-18,80)
circle(-70,80)
end_fill()

# right ear
CoderHu(140,130)
seth(60)
begin_fill()
circle(-70,60)
circle(-15,100)
circle(-90,30)
circle(15,40)
circle(-90,30)
circle(-20,100)
seth(-50)
circle(20,100)
circle(90,30)
circle(-15,35)
circle(90,50)
circle(18,80)
circle(70,80)
end_fill()

# belly
CoderHu(-130,-20)
seth(-60)
begin_fill()
circle(-20,60)
circle(150,50)
circle(60,60)
seth(175)
circle(-70,70)
circle(-132,50)
circle(40,40)
end_fill()

# left leg
CoderHu(-90,-250)
seth(180)
begin_fill()
circle(-100,60)
circle(20,90)
circle(40,40)
circle(20,60)
circle(120,40)
seth(178)
circle(-120,40)
circle(-25,60)
circle(-50,50)
circle(-30,90)
circle(70,50)
end_fill()

# right leg
CoderHu(120,-260)
seth(15)
begin_fill()
circle(120,50)
circle(20,90)
circle(70,40)
circle(120,40)
circle(-60,60)
circle(70,60)
circle(20,90)
seth(-120)
circle(20,120)
circle(40,50)
circle(-70,40)
seth(180)
circle(65,40)
circle(-35,40)
circle(-17,120)
seth(120)
circle(-14,70)
circle(-65,60)
circle(40,70)
circle(-115,50)
circle(-60,20)
circle(-15,98)
circle(-110,50)
end_fill()

# left hand
CoderHu(-170,-60)
seth(180)
begin_fill()
circle(20,80)
circle(-30,150)
circle(20,80)
seth(0)
circle(-20,80)
circle(32,170)
circle(-20,80)
end_fill()
CoderHu(-205,-80)
seth(75)
begin_fill()
circle(40,60)
seth(-150)
circle(40,60)
seth(65)
circle(-40,40)
seth(-45)
circle(-40,35)
end_fill()

# right hand
CoderHu(240,-60)
seth(180)
begin_fill()
circle(20,80)
circle(-30,150)
circle(20,80)
seth(0)
circle(-20,80)
circle(32,170)
circle(-20,80)
end_fill()
CoderHu(205,-80)
seth(75)
begin_fill()
circle(40,60)
seth(-150)
circle(40,60)
seth(65)
circle(-40,40)
seth(-45)
circle(-40,35)
end_fill()
hideturtle()
done()