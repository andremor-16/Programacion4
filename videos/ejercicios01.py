i=1
autoamarillo=0
autonaranaja=0
autorojo=0
autoverde=0
autoazul=0


while (i<=5):
    i=i+1
    placa=int(input("ingrese el ultimo digito de su placa:"))
while (placa>0 and placa <9):
    placa=int(input("ingrese el ultimo digito de su placa:"))
    if  placa==1 and placa==2:
        autoamarillo=autoamarillo+1
        print("el automovil es de color amarillo")
        print("su pico y placa son los lunes")
    elif placa==3 and placa==4:
        autonaranaja=autonaranaja+1
        print("el automovil es de color naranja")
        print("su pico y placa osn los martes")
    elif placa==5 and placa==6:
        autorojo=autorojo+1
        print("el automovil es de color rojo")
        print("su pico y placa son los miercoles")
    elif placa==7 and placa==8:
        autoverde=autoverde+1
        print("el automovil es de color verde")
        print("su pico y placa son los jueves")
    elif placa==9 and placa==0:
        autoazul=autoazul+1
        print("el automovil es de color azul")
        print("su pico y placa son los viernes")
    else:
            pass    
print("la cantidad de automoviles amarillos:",autoamarillo)        
print("la cantidad de automoviles naranaja:",autonaranaja) 
print("la cantidad de automoviles rojo:",autorojo) 
print("la cantidad de automoviles verde:",autoverde) 
print("la cantidad de automoviles azul:",autoazul)    
