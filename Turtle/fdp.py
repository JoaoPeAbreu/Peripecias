import turtle

#formando a tartaruga
tartuga = turtle.Turtle()
tela = turtle.Screen()
tartuga.shape("turtle")
tartuga.color("slate blue")

#movimentando a tartarua
tartuga.speed(2)
tartuga.pensize(2)
tartuga.fillcolor("light sea green")
tartuga.begin_fill()
tartuga.bk(300)
tartuga.right(90)
tela.bgcolor("tan")
tartuga.fd(200)
tartuga.left(90)
tartuga.fd(300)
#tartuga.left(90)
#tartuga.fd(200)
tartuga.home()
tartuga.end_fill()
tartuga.setpos(100, -90)
tartuga.penup()
tartuga.setx(10)
tartuga.stamp()
tartuga.sety(10)
tartuga.pendown()
tartuga.fillcolor("aquamarine")
tartuga.begin_fill()
tartuga.circle(69)
tartuga.end_fill()

tartuga.right(90)
tartuga.penup()

fonte1 = ("Arial", 20, "normal")
tartuga.write("Matheus", False, "center", fonte1)
tartuga.fd(50)

tartuga.clear()