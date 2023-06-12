#Juego de CARA Y SELLAZO
#Importamos las funciones del metodo ramdom
import random
#Definimos la funciones a utilizar en el juego
def lanzarMoneda():
    nombre = input("Digite su nombre\n")
    glo=int(input("Digite el un valor global para iniciar\n"))
    aleatorio = random.randint(1,2)
    return (nombre, glo, aleatorio)
def jugar():
    apostar=int(input("Digite el valor que va apostar inicialmente\n"))
    opcion=int(input("Seleccione una opcion\n 1. CARA\n 2. SELLO"))
    return (apostar,opcion)

def pierde(a,b,nom):
    ap=a*0
    b=b+ap
    perdida=print(f"{nom} Perdiste {a} la ronda ahora tienes {b}")
    return perdida
def gana(a,b,nom):
    ap=a*2
    b=b+ap
    ganaste=print(f"{nom} Ganaste {ap} la ronda ahora tienes",b)
    return ganaste
#Inicializamos el juego CARAYSELLAZO
#Menu de opciones
print("BIENVENIDO AL CARA Y SELLAZO")
op1=1
while(op1==1):
    #Funcion 1 traemos nombre y aleatorio
    nom,glo,ale=lanzarMoneda()
    #Funcion 2 traemos valor apostar y selecciones de CARA O SELLO
    apu,op=jugar()
    if (ale==op):
        g = gana(apu,glo,nom)
    elif(ale!=op):
        p = pierde(apu,glo,nom)
    op1=int(input("¿Seguir apostando?\nDigite\n 1. si\n 2. No\n"))




