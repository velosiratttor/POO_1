import turtle

t = turtle.turtles()
s = turtle.Screen()
s.bgcolor("#262626")
t.pencolor ("#262626")
t.speed (100)
col=("ED7864","#6E544F","#592F2F","#6E382E")

for n in range(5):
    for x in range (8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.spencolor(col[n%4])
s.exitonclick()
