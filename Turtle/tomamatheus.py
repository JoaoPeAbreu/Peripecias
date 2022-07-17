import turtle

#parindo a tartaruga e dando um berço #papaiamapapaicuida
tar = turtle.Turtle()#criei a tartuga
tel = turtle.Screen()#criei o fundo onde ela vive

#sendo bem machistinha e dizendo como a tartaruga tem que se comportar
tar.shape("turtle")#impus o padrão da sociedade nela
tar.color("light sea green")#impus sua cor de pele nela
tar.speed(2)#impus até que velocidade ela pode andar para não fugir de mim
tar.pensize(2)#impus a finura da linha que ela pode desenhar

#delimitando aonde ela pode caminhar e onde não pode #daescolaparacasadacasaparaaigrejaedaigrejaparaescola
#letra M
tar.penup()
tar.bk(300)
tar.pendown()
tar.right(90)
tar.fd(100)
tar.bk(200)
tar.setpos(-240, -30)
tar.setpos(-170, 90)
tar.fd(190)
tar.right(90)

#espaço
tar.penup()
tar.bk(35)
tar.pendown()

#A
tar.setpos(-80, 90)
tar.setpos(-40, -100)
tar.fd(96)

#espaço
tar.penup()
tar.bk(216)
tar.pendown()

#T
tar.right(90)
tar.fd(200)
tar.right(90)
tar.fd(85)
tar.bk(170)

#espaço
tar.penup()
tar.fd(85)
tar.left(90)
tar.bk(200)
tar.right(90)
tar.fd(120)
tar.pendown()

#H
tar.left(90)
tar.fd(200)
tar.bk(100)
tar.right(90)
tar.fd(85)
tar.right(90)
tar.fd(100)
tar.bk(200)

#espaço
tar.penup()
tar.fd(200)
tar.left(90)
tar.fd(235)
tar.pendown()

#desisti, vou escrever
tar.penup()
fonte1 = ("Comic Sans", 90, "normal")
tar.write("E U S", False, "center", fonte1)
tar.stamp()
tar.fd(100)


#mais escrita
tar.bk(600)
tar.right(90)
tar.fd(100)
fonte2 = ("Comic Sans", 70, "normal")
tar.write("Tá ai putinha do cabelo roxo", False, "center", fonte2)
tar.fd(300)