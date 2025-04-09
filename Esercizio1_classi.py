class Punto():
    x=0
    y=0
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def muovi(self,nx,ny):      #metodo muovi
            self.x = nx
            self.y = ny
            print("la distanza dal origine x ora e ", self.x)
            print("la distanza dal origine y ora e ", self.y)


#stampare distanza origine
oggett1_Punto=Punto(0,0)
oggett1_Punto.muovi(10,12)
        



    


