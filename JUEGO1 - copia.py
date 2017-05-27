from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sys
import time
import random
ventana = Tk()
ventana.geometry("700x500")
ventana.title("Road Fighter")
imagen1= PhotoImage(file="imagen1.JPG")
imagenBoton1= PhotoImage(file="imagenB.JPG")
imagenBoton2= PhotoImage(file="imagenC.JPG")
imagenBoton3= PhotoImage(file="imagenD.JPG")
imagenEncabezado= PhotoImage(file="road2.png")
imagen2= PhotoImage(file="Scarrito.png")
imagen3= PhotoImage(file="2carro.png")
imagen4= PhotoImage(file="carroizq.png")
imagen5= PhotoImage(file="CarroEST.png")
imagen7= PhotoImage(file="oil.gif")
imagen8= PhotoImage(file="carroEST.png")
imagen10= PhotoImage(file="mapa37.png")
imagen11= PhotoImage(file="explosion3.png")
imagen12= PhotoImage(file="explosion4.png")
imagen13= PhotoImage(file="explosion5.png")
imagen14= PhotoImage(file="explosion6.png")
imagen15= PhotoImage(file="explosion7.png")
imagen16= PhotoImage(file="explosion8.png")
imagen17= PhotoImage(file="explosion9.png")
imagen18= PhotoImage(file="gasolina22.png")
imagen19= PhotoImage(file="gameover.png")
imagen20= PhotoImage(file="mapa38.png")
imagen21= PhotoImage(file="level2.png")
imagen22= PhotoImage(file="mapa39.png")
imagen23= PhotoImage(file="level3.png")
imagen24= PhotoImage(file="mapa40.png")
imagen25= PhotoImage(file="level4.png")
imagen26= PhotoImage(file="mapa41.png")
imagen27= PhotoImage(file="level5.png")
imagen28= PhotoImage(file="final2.png")
imagen29= PhotoImage(file="carroVerde.png")
imagen30= PhotoImage(file="mancha.png")





fondo1=Label(ventana,image=imagen1).place(x=0,y=0)
ventana.config(bg="blue")
nombreJugador1=""
nombreJugador2=""
listaBotones=[]
#gasolina= StringVar()
def oneplayer():
    ventana1=Toplevel(ventana)

    ventana1.geometry("700x500")
    ventana1.config(bg="black")
    oneplayer=Label(ventana1,image=imagenBoton1).place(x=290,y=240)
    fondo3= Label(ventana1,image=imagenEncabezado).place(x=60,y=0)
    FondoName=Label(ventana1,text="Name",bg="black",font=("Virtual DJ",18),fg="red").place(x=150,y=300)
    difi= Label(ventana1,text="Choose \n Difficulty",bg="black",font=("Virtual DJ",18),fg="red").place(x=70,y=400)
    ment=StringVar()

    nombre=StringVar() ##get user acuerdese
    nombre1=Entry(ventana1,textvariable=ment,bg="black",font=("Virtual DJ",18),fg="white").place(x=260,y=300)
    
    def Pjuego():
        
        global gasolina
        global score
        gasolina=100
        score = 0
        num=IntVar()
        num3= IntVar()
        
        num.set(gasolina)
        num3.set(score)
        ventana2=Toplevel(ventana1)
        ventana2.geometry("500x500")
        ventana2.config(bg="black")
        
        gasolinalabel= Label(ventana2,textvariable=num,bg="black",font=("Virtual DJ",25),fg="white").place(x=200,y=340)
        scorelabel= Label(ventana2,textvariable=num3,bg="black",font=("Virtual DJ",25),fg="white").place(x=200,y=500)
        fondo90= Label(ventana2,text="Puntuación",bg="black",font=("Virtual DJ",18),fg="white").place(x=200,y=450)
        
        
        
        
        

        
        fondo5= Label(ventana2,text="Gasolina",bg="black",font=("Virtual DJ",18),fg="white").place(x=200,y=300)
        fondo6= Label(ventana2,text="Jugador",bg="black",font=("Virtual DJ",18),fg="white").place(x=200,y=50)
        mtext=ment.get()
        nombreJugador= Label(ventana2,text=mtext,bg="black",font=("Virtual DJ",20),fg="white").place(x=200,y=150)
    

        #600x
         #tener
        #en cuenta esto para la gasolina
        
        
        

        
        
        canvas=Canvas(ventana2,width=400,height=700) 
        
        canvas.pack()
        Fondo= canvas.create_image(200,250,image=imagen10)  
        Fondo2= canvas.create_image(200,250,image=imagen20)
        Fondo3= canvas.create_image(200,250,image=imagen22)
        levelTwo= canvas.create_image(180,300,image=imagen21)
        canvas.itemconfigure(levelTwo,state="hidden")
        canvas.itemconfigure(Fondo3,state="hidden")
        canvas.itemconfigure(Fondo2,state="hidden")
        carroRojo= canvas.create_image(0,0, image=imagen2)
        carroAzul= canvas.create_image(0,0, image=imagen3)
        carroVerde= canvas.create_image(0,0, image=imagen29)
        mancha= canvas.create_image(0,0, image=imagen30)
        
        carroRojoIZQ= canvas.create_image(0,0, image=imagen4)
        gasolina33= canvas.create_image(0,0, image=imagen18)
        carroA= canvas.create_image(0,0, image=imagen5)
        carroB= canvas.create_image(0,0,image=imagen8)
        explosion1 = canvas.create_image(-10,0, image=imagen11)
        explosion2 = canvas.create_image(-10,0, image=imagen12)
        explosion3 = canvas.create_image(-10,0, image=imagen13)
        explosion4 = canvas.create_image(-10,0, image=imagen14)
        explosion5 = canvas.create_image(-10,0, image=imagen15)
        explosion6 = canvas.create_image(-10,0, image=imagen16)
        explosion7 = canvas.create_image(-10,0, image=imagen17)
        over= canvas.create_image(-1000,0,image=imagen19)
        
        
        
        
        canvas.move(carroRojo,200,410)
        RAM=True
        RAM2=False
        RAMAMA=True
        RAM3=False
        RAMAZU=True
        RAM4=False
        RAMG=True
        RAMG1=False
        PUT=False
        fold=True
        mapas=0     
        RAMVERDE = True
        RAM7 = False
   
        def moverCarro(event):
            

         
                
      
            if event.keysym=="Left":
                    canvas.move(carroRojo,-10,0)
                
                    h=canvas.coords(carroRojo)
                       
            else:
                h=canvas.move(carroRojo,10,0)
           
        
   
      
                
        

        canvas.bind_all("<Left>",moverCarro)
        
        canvas.bind_all("<Right>",moverCarro)                    
        canvas.move(carroAzul,200,0)
        canvas.move(carroA,140,0)
        canvas.move(carroB,350,0)
        canvas.move(carroVerde,180,-300)
        canvas.move(Fondo,0,-1800)
        canvas.move(gasolina33,150,0)
        canvas.move(mancha,160,-700)
        
        pos1= canvas.coords(carroRojo)
        ventana2.update

        
        yspeed=10
        xspeed=0
        s=canvas.coords(carroRojoIZQ)
        
    
        
        while fold== True:
            altura=canvas.winfo_height()
            
            canvas.move(carroAzul,xspeed,yspeed)
            canvas.move(Fondo,0,10) #<---------- cambiar
            canvas.move(carroA,xspeed,yspeed)
            canvas.move(carroVerde,xspeed,yspeed)
            canvas.move(gasolina33,xspeed,yspeed)
            canvas.move(mancha,xspeed,yspeed)
            pos = canvas.coords(carroAzul)
            pos3= canvas.coords(carroA)
            pos2 = canvas.coords(carroRojo)
            posG=canvas.coords(gasolina33)
            posV = canvas.coords(carroVerde)
            posM= canvas.coords(mancha)
            
            
            posy= pos2[1]
            posx= pos2[0]
            posG1= posG[0]
            posyG=posG[1]
            Q8=posG1+10
            Q10=[Q8,posyG]
            Q12=posG1-10
            
            Q11=[Q12,posyG]
            
            
            posy1=pos[1]
            posx1=pos[0]
            Q13=posx1-10
            Q15=posx1+10
            Q20=[Q13,posy1]
            Q21=[Q15,posy1]
            Q3=posx-10
            Q5=posx+10
            Q4=[Q3,posy]
            Q7=[Q5,posy]
            #print(pos3,"pos3")
            posy2=pos3[1]
            posx2=pos3[0]
            posFondo= canvas.coords(Fondo)
            #print(posFondo)
            #print(pos,"carro azul")
            print(pos2,"carro rojo")
            #print(posV)
            
            if pos[1] >700:
                y=random.randrange(100,240,10) ##cambio
                
                #print(y)
                
                carroAzul= canvas.create_image(0,0, image=imagen3)
                
                canvas.move(carroAzul,y,0)
                #yspeed=10
                #xspeed=0
                canvas.move(carroAzul,xspeed,yspeed)
                score += 10
                num3.set(score)
                
                if pos[1]==300:
                    canvas.move(caroAzul,Xspeed,0)
            elif posM[1] > 700:
                y=random.randrange(100,240,10) ##cambio
                
                #print(y)
                
                mancha= canvas.create_image(0,0, image=imagen30)
                
                canvas.move(mancha,y,0)
                #yspeed=10
                #xspeed=0
                canvas.move(mancha,xspeed,yspeed)
                score += 10
                num3.set(score)
                
            elif posV[1] > 800:
                y=random.randrange(100,240,10)
                carroVerde= canvas.create_image(0,0, image=imagen29)
                canvas.move(carroVerde,y,0)
                #yspeed=10
                #xspeed=0
                canvas.move(carroAzul,xspeed,yspeed)
                score += 5
                num3.set(score)
                
                
                
            elif pos == pos2 or pos == Q4 or Q7 == pos:
              
               
                x=random.randrange(0,40)
                if x % 2 == 0:
                    
                    canvas.move(carroRojo,-30,0)
                    canvas.move(carroAzul,30,0)
                else:
                    canvas.move(carroRojo,30,0)
                    canvas.move(carroAzul,-30,0)
            elif pos2 == pos3 or pos3 == Q4 or pos3 == Q7:
                
                
                x=random.randrange(0,40)
                if x % 2 == 0:
                    
                    
                    canvas.move(carroRojo,-30,0)
                    canvas.move(carroA,30,0)
                else:
                    canvas.move(carroRojo,30,0)
                    canvas.move(carroA,-30,0)
            elif pos2 == posM or posM == Q4 or posM == Q7:
                x=random.randrange(0,40)
                if x % 2 == 0:
                    
                    canvas.move(carroRojo,-30,0)
                    
                else:
                    canvas.move(carroRojo,30,0)
                    
                
                
            elif pos == pos3 or Q20 == pos3 or Q21 == pos3:
                x=random.randrange(0,40)
                if x % 2 == 0:
                    canvas.move(carroAzul,-30,0)
                    canvas.move(carroA,30,0)
                else:
                    canvas.move(carroAzul,30,0)
                    canvas.move(carroA,-30,0)
                
                
            elif posV == pos2 or Q4 == posV or Q7 == posV:
                x=random.randrange(0,40)
                if x % 2 == 0:
                    canvas.move(carroVerde,-30,0)
                    canvas.move(carroRojo,30,0)
                else:
                    canvas.move(carroRojo,30,0)
                    canvas.move(carroVerde,-30,0)
                
                
            elif pos[1]==300:
                jx=random.randrange(-50,50,10)
                canvas.move(carroAzul,jx,0)
            
            elif pos3[1]==700:
            
                j=random.randrange(100,240,10)
                carroA= canvas.create_image(0,0, image=imagen5)
                canvas.move(carroA,j,0)
                #yspeed=10
                #xspeed=0
                canvas.move(carroA,xspeed,yspeed)
                score += 15
                num3.set(score)
                
       
            elif posFondo[1] > 2200:
                
                
                Fondo= canvas.create_image(200,250,image=imagen10)
                Fondo2= canvas.create_image(200,250,image=imagen20)
                levelTwo= canvas.create_image(180,300,image=imagen21)
                levelTre= canvas.create_image(180,300,image=imagen23)
                levelCua= canvas.create_image(180,300,image=imagen25)
                levelCin= canvas.create_image(200,250,image=imagen27)
                Fondo3= canvas.create_image(200,250,image=imagen22)
                Fondo4= canvas.create_image(200,250,image=imagen24)
                Fondo5= canvas.create_image(200,250,image=imagen26)
                canvas.itemconfigure(Fondo3,state="hidden")
                canvas.itemconfigure(Fondo4,state="hidden")
                canvas.itemconfigure(Fondo5,state="hidden")
                
                
                canvas.itemconfigure(levelTre,state="hidden")
                canvas.itemconfigure(levelCua,state="hidden")
                canvas.itemconfigure(levelCin,state="hidden")
                
                
                
                mapas += 1
                if mapas == 1:
                    
                    Fondo=Fondo2
                    gasolina=100
                    
                    
                    canvas.itemconfigure(Fondo2,state="normal")
                    
                    carroRojo= canvas.create_image(0,0, image=imagen2)
                    canvas.move(carroRojo,0,10)
                    carroAzul= canvas.create_image(0,0, image=imagen3)
                    carroA= canvas.create_image(0,0, image=imagen5)
                
                    canvas.itemconfigure(levelTwo,state="normal")
                    time.sleep(1.0)
                    ventana2.update()
                    canvas.itemconfigure(levelTwo,state="hidden")
                    Fondo=Fondo2
                    time.sleep(3.0)
                    canvas.itemconfigure(Fondo2,state="normal")
                    yspeed=20
                if mapas == 2:
                    
                    canvas.itemconfigure(levelTwo,state="hidden")
                    canvas.itemconfigure(Fondo2,state="hidden")
                    Fondo=Fondo3
                    levelTre= canvas.create_image(180,300,image=imagen23)
                    
                    gasolina=100                    
                    canvas.itemconfigure(Fondo3,state="normal")
                    carroRojo= canvas.create_image(0,0, image=imagen2)
                    canvas.move(carroRojo,posx,440)
                    g=canvas.coords(carroRojo)
                    print(g)
                    carroAzul= canvas.create_image(0,0, image=imagen3)
                    carroA= canvas.create_image(0,0, image=imagen5)
                
                    canvas.itemconfigure(levelTre,state="normal")
                    
                   
                    
                    time.sleep(1.0)
                    ventana2.update()
                    canvas.itemconfigure(levelTre,state="normal")
                    Fondo=Fondo3
                    
                    time.sleep(3.0)
                    canvas.itemconfigure(Fondo3,state="normal")
                    canvas.itemconfigure(levelTre,state="hidden")
                    
                   
                if mapas == 3:
                    canvas.itemconfigure(levelTwo,state="hidden")
                    canvas.itemconfigure(levelTre,state="hidden")
                    canvas.itemconfigure(Fondo3,state="hidden")
                    Fondo=Fondo3
                    levelCua= canvas.create_image(200,300,image=imagen25)
                    
                    gasolina=100
                    canvas.itemconfigure(Fondo4,state="normal")
                    carroRojo= canvas.create_image(0,0, image=imagen2)
                    carroAzul= canvas.create_image(0,0, image=imagen3)
                    carroA= canvas.create_image(0,0, image=imagen5)
                
                    canvas.itemconfigure(levelCua,state="normal")
                    
                   
                    
                    time.sleep(1.0)
                    ventana2.update()
                    canvas.itemconfigure(levelCua,state="normal")
                    Fondo=Fondo4
                    
                    time.sleep(3.0)
                    canvas.itemconfigure(Fondo4,state="normal")
                    canvas.itemconfigure(levelCua,state="hidden")
                if mapas == 4:
                    canvas.itemconfigure(levelTwo,state="hidden")
                    canvas.itemconfigure(levelTre,state="hidden")
                    canvas.itemconfigure(levelCua,state="hidden")
                    Fondo=Fondo4
                    levelCin= canvas.create_image(180,300,image=imagen27)
                    gasolina=100
                    canvas.itemconfigure(Fondo5,state="normal")
                    carroRojo= canvas.create_image(0,0, image=imagen2)
                    carroAzul= canvas.create_image(0,0, image=imagen3)
                    carroA= canvas.create_image(0,0, image=imagen5)
                
                    canvas.itemconfigure(levelCin,state="normal")
                    
                   
                    
                    time.sleep(1.0)
                    ventana2.update()
                    canvas.itemconfigure(levelCin,state="normal")
                    Fondo=Fondo5
                    
                    time.sleep(3.0)
                    canvas.itemconfigure(Fondo5,state="normal")
                    canvas.itemconfigure(levelCin,state="hidden")
                if mapas == 5:
                    canvas.itemconfigure(levelTwo,state="hidden")
                    Fondo5= canvas.create_image(200,250,image=imagen26)
                    win= canvas.create_image(0,0, image=imagen28)
                    canvas.move(win,175,300)
                    break
                    
                    
                    
                    

                    
                    
                    
                    
                    
                    
                    

                canvas.move(carroRojo,posx,posy)
                canvas.move(carroAzul,posx1,posy1)
                canvas.move(carroA,posx2,posy2)
                canvas.move(Fondo,0,-1800)

                #yspeed=10
                #xspeed=0
                
                canvas.move(Fondo,xspeed,yspeed)
            elif posV[1] == 350:
                if pos2[0] >= 180:
                    canvas.move(carroVerde,40,0)
                elif pos2[0] <= 160:
                    canvas.move(carroVerde,-40,0)
                    
                else:
                    pass
            elif pos2[0] == 250 :
                RAM=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen13)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                gasolina -= 10
                #print(gasolina)
                #gasolinalabel.config(textvariable=int(gasolina))
                num.set(gasolina)
                
                
                
                canvas.itemconfigure(carroRojo,state="hidden")
                canvas.move(carroRojo,-100,0)
               
               
                canvas.move(explosion1,posx,posy)
                time.sleep(0.2)
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                h=canvas.coords(explosion1)
                h1=h[0]
                h2=h[1]
                if h[0]== 240:
                    #print("perro hpta")
                    canvas.move(explosion2,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    
                    
                    canvas.itemconfigure(explosion2,state="hidden")
                #ventana2.update()
                hk=canvas.coords(explosion2)
                h3=hk[0]
                h4=hk[1]
                #print(h3,"dsd")
                if hk[0]==240.0:
                    ##print("Perro final")
                    
                    canvas.move(explosion3,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                #ventana2.update()
                hk1=canvas.coords(explosion3)
                h5=hk1[0]
                ##print(h5,"gdffhg")
                h6=hk1[1]
                if hk1[0] == 240.0:
                    ##print("perro5")
                    canvas.move(explosion4,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hk2=canvas.coords(explosion4)
                h7=hk2[0]
                h8=hk2[1]
                ##print(h7,"hola")
                if hk2[0] == 240.0:
                    ##print("perro4")
                    canvas.move(explosion5,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hk3=canvas.coords(explosion5)
                h9=hk3[0]
                h10=hk3[1]
                ##print(h9,"xx")
                if hk3[0]== 240:
                    ##print("perro3")
                    canvas.move(explosion6,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion6,state="hidden")

                hk4=canvas.coords(explosion6)
                h11=hk4[0]
                h12=hk4[1]
                #print(h11,"perro")
                if hk4[0] == 240:
                    #print("perro2")
                    canvas.move(explosion7,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion7,state="hidden")
            
               
                RAM= True
                RAM2=True

            elif pos2[0] == 90:
                RAM=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen12)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                gasolina -= 10
                #print(gasolina)
                #gasolinalabel.config(textvariable=int(gasolina))
                num.set(gasolina)
                
                canvas.itemconfigure(carroRojo,state="hidden")
                canvas.move(carroRojo,-100,0)

                canvas.move(explosion1,100,410)
                time.sleep(0.2)               
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                hh=canvas.coords(explosion1)
                hh2=hh[0]
                hh3=hh[1]
                if hh[0] == 90:
                   
                    canvas.move(explosion2,100,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion2,state="hidden")
                hg=canvas.coords(explosion2)
                
                hh4=hg[0]
                hh5=hg[1]
                if hg[0] == 90:
                    
                    canvas.move(explosion3,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                hg1=canvas.coords(explosion3)
                hh6=hg1[0]
                hh7=hg1[1]
                if hg1[0] == 90:
                    
                    canvas.move(explosion4,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hg2=canvas.coords(explosion4)
                #print(hg2,"XXXX")
                if hg2[0] == 90:
                    
                    canvas.move(explosion5,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hg3= canvas.coords(explosion5)    
                if hg3[0] == 90:
                   
                    canvas.move(explosion6,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion6,state="hidden")
                hg4=canvas.coords(explosion6)
                if hg4[0] == 90:
                    canvas.move(explosion7,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion7,state="hidden")
                RAM=True
                RAM2=True
                
            elif pos3[0] == 250:
                RAMAMA=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen13)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                
                canvas.itemconfigure(carroA,state="hidden")
                canvas.move(carroA,-100,0)
               
               
                canvas.move(explosion1,250,410)
                time.sleep(0.2)
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                h=canvas.coords(explosion1)
                h1=h[0]
                h2=h[1]
                if h[0]== 240:
                    #print("perro hpta")
                    canvas.move(explosion2,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    
                    
                    canvas.itemconfigure(explosion2,state="hidden")
                #ventana2.update()
                hk=canvas.coords(explosion2)
                h3=hk[0]
                h4=hk[1]
                #print(h3,"dsd")
                if hk[0]==240.0:
                    ##print("Perro final")
                    
                    canvas.move(explosion3,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                #ventana2.update()
                hk1=canvas.coords(explosion3)
                h5=hk1[0]
                ##print(h5,"gdffhg")
                h6=hk1[1]
                if hk1[0] == 240.0:
                    ##print("perro5")
                    canvas.move(explosion4,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hk2=canvas.coords(explosion4)
                h7=hk2[0]
                h8=hk2[1]
                ##print(h7,"hola")
                if hk2[0] == 240.0:
                    ##print("perro4")
                    canvas.move(explosion5,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hk3=canvas.coords(explosion5)
                h9=hk3[0]
                h10=hk3[1]
                ##print(h9,"xx")
                if hk3[0]== 240:
                    ##print("perro3")
                    canvas.move(explosion6,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion6,state="hidden")

                hk4=canvas.coords(explosion6)
                h11=hk4[0]
                h12=hk4[1]
                #print(h11,"perro")
                if hk4[0] == 240:
                    #print("perro2")
                    canvas.move(explosion7,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion7,state="hidden")
                RAMAMA=True
                RAM3=True
                
                
                
                
                    
                
                #print(h,"explosion")
                 
                    
                    
                    #time.sleep(0.1)
            
                    
                   
                
                
                
            elif  RAM == True and RAM2 == True:
                canvas.move(carroRojo,0,0)
                BB=canvas.coords(carroRojo)
                if BB[0] < 90:
                    canvas.move(carroRojo,200,0)
                
                canvas.move(explosion1,1000,1000)
                canvas.move(explosion2,1000,1000)
                canvas.move(explosion3,1000,1000)
                canvas.move(explosion4,1000,1000)
                canvas.move(explosion5,1000,1000)
                canvas.move(explosion6,1000,1000)
                canvas.move(explosion7,1000,1000)
                h=canvas.coords(explosion1)
                print(h,"coordenadas")
                canvas.itemconfigure(carroRojo,state="normal")
                
                canvas.itemconfigure(explosion1,state="normal")
                canvas.itemconfigure(explosion2,state="normal")
                canvas.itemconfigure(explosion3,state="normal")
                canvas.itemconfigure(explosion4,state="normal")
                canvas.itemconfigure(explosion5,state="normal")
                canvas.itemconfigure(explosion6,state="normal")
                canvas.itemconfigure(explosion7,state="normal")
                RAM2=False
            elif pos3[0] == 90:
                RAMAMA=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen12)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                
                canvas.itemconfigure(carroA,state="hidden")
                canvas.move(carroA,-100,0)

                canvas.move(explosion1,100,410)
                time.sleep(0.2)               
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                hh=canvas.coords(explosion1)
                hh2=hh[0]
                hh3=hh[1]
                if hh[0] == 90:
                    
                    canvas.move(explosion2,100,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion2,state="hidden")
                hg=canvas.coords(explosion2)
                
                hh4=hg[0]
                hh5=hg[1]
                if hg[0] == 90:
                   
                    canvas.move(explosion3,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                hg1=canvas.coords(explosion3)
                hh6=hg1[0]
                hh7=hg1[1]
                if hg1[0] == 90:
                    #print("explo4")
                    canvas.move(explosion4,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hg2=canvas.coords(explosion4)
                #print(hg2,"XXXX")
                if hg2[0] == 90:
                    
                    canvas.move(explosion5,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hg3= canvas.coords(explosion5)    
                if hg3[0] == 90:
                    
                    canvas.move(explosion6,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion6,state="hidden")
                hg4=canvas.coords(explosion6)
                if hg4[0] == 90:
                    canvas.move(explosion7,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion7,state="hidden")
                RAMAMA=True
                RAM3=True
            elif  RAMAMA== True and RAM3 == True:
                canvas.move(carroA,0,0)
                BB=canvas.coords(carroA)
                if BB[0] < 90:
                    canvas.move(carroA,200,0)
                
                canvas.move(explosion1,1000,1000)
                canvas.move(explosion2,1000,1000)
                canvas.move(explosion3,1000,1000)
                canvas.move(explosion4,1000,1000)
                canvas.move(explosion5,1000,1000)
                canvas.move(explosion6,1000,1000)
                canvas.move(explosion7,1000,1000)
                h=canvas.coords(explosion1)
                #print(h,"coordenadas")
                canvas.itemconfigure(carroA,state="normal")
                
                canvas.itemconfigure(explosion1,state="normal")
                canvas.itemconfigure(explosion2,state="normal")
                canvas.itemconfigure(explosion3,state="normal")
                canvas.itemconfigure(explosion4,state="normal")
                canvas.itemconfigure(explosion5,state="normal")
                canvas.itemconfigure(explosion6,state="normal")
                canvas.itemconfigure(explosion7,state="normal")
                RAM3=False
            elif pos[0] == 250 :
                
                RAMAZU=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen13)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                
                canvas.itemconfigure(carroAzul,state="hidden")
                canvas.move(carroAzul,-100,0)
               
               
                canvas.move(explosion1,posx,posy)
                time.sleep(0.2)
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                h=canvas.coords(explosion1)
                h1=h[0]
                h2=h[1]
                if h[0]== 240:
                    #print("perro hpta")
                    canvas.move(explosion2,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    
                    
                    canvas.itemconfigure(explosion2,state="hidden")
                #ventana2.update()
                hk=canvas.coords(explosion2)
                h3=hk[0]
                h4=hk[1]
                #print(h3,"dsd")
                if hk[0]==240.0:
                    ##print("Perro final")
                    
                    canvas.move(explosion3,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                #ventana2.update()
                hk1=canvas.coords(explosion3)
                h5=hk1[0]
                ##print(h5,"gdffhg")
                h6=hk1[1]
                if hk1[0] == 240.0:
                    ##print("perro5")
                    canvas.move(explosion4,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hk2=canvas.coords(explosion4)
                h7=hk2[0]
                h8=hk2[1]
                ##print(h7,"hola")
                if hk2[0] == 240.0:
                    ##print("perro4")
                    canvas.move(explosion5,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hk3=canvas.coords(explosion5)
                h9=hk3[0]
                h10=hk3[1]
                ##print(h9,"xx")
                if hk3[0]== 240:
                    ##print("perro3")
                    canvas.move(explosion6,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion6,state="hidden")

                hk4=canvas.coords(explosion6)
                h11=hk4[0]
                h12=hk4[1]
                #print(h11,"perro")
                if hk4[0] == 240:
                    #print("perro2")
                    canvas.move(explosion7,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion7,state="hidden")
            
               
                RAMAZU= True
                RAM4=True
            elif pos[0] == 90:
                RAMAZU=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen12)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                
                canvas.itemconfigure(carroAzul,state="hidden")
                canvas.move(carroAzul,-100,0)

                canvas.move(explosion1,100,410)
                time.sleep(0.2)               
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                hh=canvas.coords(explosion1)
                hh2=hh[0]
                hh3=hh[1]
                if hh[0] == 90:
                    
                    canvas.move(explosion2,100,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion2,state="hidden")
                hg=canvas.coords(explosion2)
                
                hh4=hg[0]
                hh5=hg[1]
                if hg[0] == 90:
                   
                    canvas.move(explosion3,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                hg1=canvas.coords(explosion3)
                hh6=hg1[0]
                hh7=hg1[1]
                if hg1[0] == 90:
                    
                    canvas.move(explosion4,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hg2=canvas.coords(explosion4)
                if hg2[0] == 90:
                    
                    canvas.move(explosion5,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hg3= canvas.coords(explosion5)    
                if hg3[0] == 90:
                    
                    canvas.move(explosion6,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion6,state="hidden")
                hg4=canvas.coords(explosion6)
                if hg4[0] == 90:
                    canvas.move(explosion7,100,410)
                    time.sleep(0.2)
                    ventana.update()
                    canvas.itemconfigure(explosion7,state="hidden")
                    RAMAZU=True
                    RAM4=True
            
        
            elif  RAMAZU== True and RAM4 == True:
                 
                 
                 
                 
                 
                 canvas.move(carroAzul,0,0)
                 BB=canvas.coords(carroA)
                 if BB[0] < 90:
                     canvas.move(carroAzul,200,0)
                
                 canvas.move(explosion1,1000,1000)
                 canvas.move(explosion2,1000,1000)
                 canvas.move(explosion3,1000,1000)
                 canvas.move(explosion4,1000,1000)
                 canvas.move(explosion5,1000,1000)
                 canvas.move(explosion6,1000,1000)
                 canvas.move(explosion7,1000,1000)
                 h=canvas.coords(explosion1)
                 
                 canvas.itemconfigure(carroAzul,state="normal")
                
                 canvas.itemconfigure(explosion1,state="normal")
                 canvas.itemconfigure(explosion2,state="normal")
                 canvas.itemconfigure(explosion3,state="normal")
                 canvas.itemconfigure(explosion4,state="normal")
                 canvas.itemconfigure(explosion5,state="normal")
                 canvas.itemconfigure(explosion6,state="normal")
                 canvas.itemconfigure(explosion7,state="normal")
                 RAM4=False
            elif pos == pos3:
                #canvas.itemconfigure(carroRojo,state="hidden")
                x=random.randrange(0,40)
                if x % 2 == 0:
                    
                    canvas.move(carroA,-30,0)
                    canvas.move(carroAzul,30,0)
                else:
                    canvas.move(carroA,30,0)
                    canvas.move(carroAzul,-30,0)
            elif pos2 == posG or Q10 == pos2 or Q11 == pos2:
                
                canvas.itemconfigure(gasolina33,state="hidden")
                canvas.move(gasolina33,-1000,0)

                #ventana2.update()
                
                gasolina += 10
                print(gasolina)
                #gasolinalabel.config(textvariable=int(gasolina))
                num.set(gasolina)
                RAMG1=True
            elif posG[1] == 1300:
                j1=random.randrange(100,240,10)
                gasolina33= canvas.create_image(0,0, image=imagen18)
                canvas.move(gasolina33,j,0)
                #yspeed=10
                #xspeed=0
                canvas.move(gasolina33,xspeed,yspeed)
            elif RAMG==True and RAMG1==True:
                canvas.move(gasolina33,0,0)
                canvas.itemconfigure(gasolina33,state="normal")
                RAMG1=False
            elif posFondo[1] % 100 ==0:
                gasolina -= 2
                print(gasolina)
                #gasolinalabel.config(textvariable=int(gasolina))
                num.set(gasolina)
            elif posV[0] == 250:
                RAMVERDE=False
                explosion1 = canvas.create_image(-10,0, image=imagen11)
                explosion2 = canvas.create_image(-10,0, image=imagen12)
                explosion3 = canvas.create_image(-10,0, image=imagen13)
                explosion4 = canvas.create_image(-10,0, image=imagen14)
                explosion5 = canvas.create_image(-10,0, image=imagen15)
                explosion6 = canvas.create_image(-10,0, image=imagen16)
                explosion7 = canvas.create_image(-10,0, image=imagen17)
                
                canvas.itemconfigure(carroVerde,state="hidden")
                canvas.move(carroVerde,-100,0)
               
               
                canvas.move(explosion1,250,410)
                time.sleep(0.2)
                ventana2.update()
                canvas.itemconfigure(explosion1,state="hidden")
                h=canvas.coords(explosion1)
                h1=h[0]
                h2=h[1]
                if h[0]== 240:
                    #print("perro hpta")
                    canvas.move(explosion2,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    
                    
                    canvas.itemconfigure(explosion2,state="hidden")
                #ventana2.update()
                hk=canvas.coords(explosion2)
                h3=hk[0]
                h4=hk[1]
                #print(h3,"dsd")
                if hk[0]==240.0:
                    ##print("Perro final")
                    
                    canvas.move(explosion3,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion3,state="hidden")
                #ventana2.update()
                hk1=canvas.coords(explosion3)
                h5=hk1[0]
                ##print(h5,"gdffhg")
                h6=hk1[1]
                if hk1[0] == 240.0:
                    ##print("perro5")
                    canvas.move(explosion4,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion4,state="hidden")
                hk2=canvas.coords(explosion4)
                h7=hk2[0]
                h8=hk2[1]
                ##print(h7,"hola")
                if hk2[0] == 240.0:
                    ##print("perro4")
                    canvas.move(explosion5,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion5,state="hidden")
                hk3=canvas.coords(explosion5)
                h9=hk3[0]
                h10=hk3[1]
                ##print(h9,"xx")
                if hk3[0]== 240:
                    ##print("perro3")
                    canvas.move(explosion6,250,410)
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion6,state="hidden")

                hk4=canvas.coords(explosion6)
                h11=hk4[0]
                h12=hk4[1]
                #print(h11,"perro")
                if hk4[0] == 240:
                    #print("perro2")
                    canvas.move(explosion7,250,410)
                    
                    time.sleep(0.2)
                    ventana2.update()
                    canvas.itemconfigure(explosion7,state="hidden")
                RAMVERDE=True
                RAM7=True
            elif  RAMVERDE== True and RAM7 == True:
                 
                 
                 
                 
                 
                 canvas.move(carroVerde,0,0)
                 BB=canvas.coords(carroVerde)
                 if BB[0] < 90:
                     canvas.move(carroVerde,200,0)
                
                 canvas.move(explosion1,1000,1000)
                 canvas.move(explosion2,1000,1000)
                 canvas.move(explosion3,1000,1000)
                 canvas.move(explosion4,1000,1000)
                 canvas.move(explosion5,1000,1000)
                 canvas.move(explosion6,1000,1000)
                 canvas.move(explosion7,1000,1000)
                 h=canvas.coords(explosion1)
                 
                 canvas.itemconfigure(carroVerde,state="normal")
                
                 canvas.itemconfigure(explosion1,state="normal")
                 canvas.itemconfigure(explosion2,state="normal")
                 canvas.itemconfigure(explosion3,state="normal")
                 canvas.itemconfigure(explosion4,state="normal")
                 canvas.itemconfigure(explosion5,state="normal")
                 canvas.itemconfigure(explosion6,state="normal")
                 canvas.itemconfigure(explosion7,state="normal")
                 RAM7=False

            elif gasolina <= 0:
                over= canvas.create_image(0,0, image=imagen19)
                
                canvas.move(over,180,300)
                
                break
            
            
                
                
                
                
                
        
                
                
                
                
                
                
        
               
                
            



                
            
            ventana2.update()
            time.sleep(0.1)
            contador1=1
    
       
        
                
     
       
        
            
     
        ventana1.iconify()
        
    

    
    
    

    #fondo5= Label(ventana2,text="Gasolina",bg="black",font=("Virtual DJ",18),fg="white").place(x=200,y=300)
    Level1=Button(ventana1,text="Easy",width=10,height=1,command=Pjuego,activebackground="blue",bg="black",font=("Virtual DJ",12),fg="white").place(x=280,y=340)
    Level2=Button(ventana1,text="Normal",width=10,height=1,activebackground="green",bg="black",font=("Virtual DJ",12),fg="white").place(x=280,y=370)
    Level3=Button(ventana1,text="Hard",width=10,height=1,activebackground="pink",bg="black",font=("Virtual DJ",12),fg="white").place(x=280,y=400)
    Level4=Button(ventana1,text="Extreme",width=10,height=1,activebackground="red",bg="black",font=("Virtual DJ",12),fg="white").place(x=280,y=430)
    Level5=Button(ventana1,text="Impossible",width=10,height=1,activebackground="red",bg="black",font=("Virtual DJ",12),fg="white").place(x=280,y=460)
    ventana.iconify()
botononeplayer= Button(ventana,image=imagenBoton1,command=oneplayer,height=26,width=180,bg="black").place(x=280,y=270)
botontwoplayer= Button(ventana,image=imagenBoton2,height=26,width=180,bg="black").place(x=280,y=317)
botonSalir= Button(ventana,image=imagenBoton3,command=quit, height=26,width=180,bg="black").place(x=280,y=391)

ventana.mainloop()
