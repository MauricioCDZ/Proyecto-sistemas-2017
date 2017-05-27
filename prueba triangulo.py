from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
import random
ventana = Tk()
ventana.geometry("700x500")
ventana.title("Road Fighter")
imagen1= PhotoImage(file="imagen1.JPG")
imagenBoton1= PhotoImage(file="imagenB.JPG")
imagenBoton2= PhotoImage(file="imagenC.JPG")
imagenBoton3= PhotoImage(file="imagenD.JPG")
imagenBoton4= PhotoImage(file="name.png")
imagenEncabezado= PhotoImage(file="road2.png")
imagenBoton5= PhotoImage(file="dificultad.png")
imagen2= PhotoImage(file="Scarrito.png")
imagen3= PhotoImage(file="2carro.png")
imagen4= PhotoImage(file="carroizq.png")



fondo1=Label(ventana,image=imagen1).place(x=0,y=0)
ventana.config(bg="blue")
nombreJugador1=""
nombreJugador2=""
listaBotones=[]
gasolina= StringVar()
def oneplayer():
    ventana1=Toplevel(ventana)

    ventana1.geometry("700x500")
    ventana1.config(bg="black")
    oneplayer=Label(ventana1,image=imagenBoton1).place(x=290,y=240)
    fondo3= Label(ventana1,image=imagenEncabezado).place(x=60,y=0)
    FondoName=Label(ventana1,image=imagenBoton4).place(x=120,y=290)
    difi= Label(ventana1,image=imagenBoton5).place(x=120,y=400)
    nombre=StringVar() ##get user acuerdese
    nombre=Entry(ventana1,textvariable=nombre).place(x=280,y=310)
    
    def Pjuego():
        ventana2=Toplevel(ventana1)
        ventana2.geometry("700x500")
        ventana2.config(bg="black")
        
        canvas=Canvas(ventana2,width=400,height=700)
        
        canvas.pack()
        carroRojo= canvas.create_image(0,0, image=imagen2)
        carroCaja=canvas.bbox(carroRojo)
        

        
    
        carroAzul= canvas.create_image(0,0, image=imagen3)
        carroRojoIZQ= canvas.create_image(0,0, image=imagen4)
        
        canvas.move(carroRojo,200,410)
   
        def moverCarro(event):
      
            if event.keysym=="Left":
                canvas.move(carroRojo,-10,0)
                
                h=canvas.coords(carroRojo)
                       
            else:
                h=canvas.move(carroRojo,10,0)
        
   
      
                
        

        canvas.bind_all("<Left>",moverCarro)
        
        canvas.bind_all("<Right>",moverCarro)                    
        canvas.move(carroAzul,200,0)
        pos1= canvas.coords(carroRojo)
        ventana2.update

        
        yspeed=10
        xspeed=0
        ss=canvas.coords(carroRojo)
        xx=ss[0]
        
    
        
        while True:
            altura=canvas.winfo_height()
            canvas.move(carroAzul,xspeed,yspeed)
            pos = canvas.coords(carroAzul)
            #print(pos)
            pos2 = canvas.coords(carroRojo)
            SS=pos2[0]
            S3=SS+3
            print(SS)
            print(S3)
            
            if pos[1] >700:
                y=random.randrange(20,380,10)
                #print(y)
                
              
                    
                
                
                carroAzul= canvas.create_image(0,0, image=imagen3)
                
                canvas.move(carroAzul,y,0)
                yspeed=10
                xspeed=0
                canvas.move(carroAzul,xspeed,yspeed)
                print(pos)
                
            elif pos == pos2:
                
                """canvas.move(carroRojoIZQ,0,0)"""
                
             
                canvas.move(carroRojo,0,0)
                canvas.move(carroRojoIZQ,pos[0],pos2[1])
            
                o=canvas.coords(carroRojoIZQ)
           
               
    
        
        
            
                             
                       
                
                
               
                
                
            
            ventana2.update()
            time.sleep(0.1)
            contador1=1
    
       
        
                
     
       
        
            
     
        ventana1.iconify()
        
    

    
    
    

    
    Level1=Button(ventana1,text="Easy",width=30,command=Pjuego,activebackground="blue").place(x=280,y=340)
    Level2=Button(ventana1,text="Normal",width=30,activebackground="green").place(x=280,y=370)
    Level3=Button(ventana1,text="Hard",width=30,activebackground="pink").place(x=280,y=400)
    Level4=Button(ventana1,text="Extreme",width=30,activebackground="red").place(x=280,y=430)
    Level5=Button(ventana1,text="Impossible",width=30,activebackground="red").place(x=280,y=460)
    ventana.iconify()
botononeplayer= Button(ventana,image=imagenBoton1,command=oneplayer,height=26,width=180,bg="black").place(x=280,y=270)
botontwoplayer= Button(ventana,image=imagenBoton2,height=26,width=180,bg="black").place(x=280,y=317)
botonSalir= Button(ventana,image=imagenBoton3,command=quit, height=26,width=180,bg="black").place(x=280,y=391)

ventana.mainloop()
