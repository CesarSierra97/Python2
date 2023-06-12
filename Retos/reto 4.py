# Realizar los retos 1 y 3 implementado funciones 

#Definimos las funciones para el reto 1
def agregar():
    op="1"
    while(op=="1"):
        agregar=(input("Indique el nombre del instructor que desea agregar a la lista\n"))
        instructores.append(agregar)
        op=input("¿Desea agregar otro instructor?\n 1. para continuar \n 2. Cualquier tecla para terminar de agregar\n")
def Listar():
    print("Su lista de instructores quedo de la siguiente manera:\n")
    #for para listas
    for index, i in enumerate(sorted(instructores)):
        print(index+1,i)
def modificar():
    print("Su lista de instructores quedo de la siguiente manera:\n")
    op2="1"
    while(op2=="1"):
        for i, dato in enumerate(instructores):
            print(" Pocision: ",i+1," Instructor: ",dato)            
        def buscarIdx(lista,indice):
                if indice < len(lista):
                    return lista[indice]
                else:
                    return None
        idx=int(input("Indique la posicion del instructor que desea editar\n"))
        usuario_encontrado = buscarIdx(instructores,idx-1)    
        if usuario_encontrado:
            print("Usuario encontrado:", usuario_encontrado)
            nuevo=(input("Indique el dato a remplazar\n"))
            del instructores[idx-1]
            instructores.insert(idx-1,nuevo)
            print("Su lista de instructores quedo de la siguiente manera:\n",instructores)
            break
        else:
            print("**********\nUsuario no encontrado.\nVerifique la posicion seleccionada!!")
def borra():
    op2="1"
    while(op2=="1"):
        print("Su lista de instructores quedo de la siguiente manera:\n")
        #for para listas
        for i, dato in enumerate(instructores):
            print(" Pocision: ",i+1," Instructor: ",dato) 
        def buscarIdx(lista,indice):
                    if indice < len(lista):
                        return lista[indice]
                    else:
                        return None
        idx=int(input("Indique la posicion del instructor que desea Elimiar\n"))
        usuario_encontrado = buscarIdx(instructores,idx-1)    
        if usuario_encontrado:
            del instructores[idx-1]
            print("Su lista de instructores quedo de la siguiente manera:\n",instructores)
            break                    
        else:
            print("**********\nUsuario no encontrado.\nVerifique la posicion seleccionada!!")
def buscar():
    def buscar(lista,nombre):
        for usuario in lista:
            if usuario == nombre.lower():
                return usuario
        return None
    nombre=input("Digite el nombre del instructor que desa buscar\n")
    usuario_encontrado = buscar(instructores,nombre)    
    if usuario_encontrado:
        print("Usuario encontrado:", usuario_encontrado)
        print("El instructor ",nombre," Se encuentra en la posicion",(instructores.index(nombre))+1)
    else:
        print("Usuario no encontrado.")
def listar():
    print("Su lista de instructores esta de la siguiente manera:\n")
    instructores.sort()
    print(instructores)
#Funciones reto 2
def agregarR2():
    def buscar(lista,nombre):
        for usuario in lista:
            if usuario == nombre:
                return usuario
        return None
    nombre=input("Digite el nombre del instructor\n")
    usuario_encontrado = buscar(instructores,nombre)    
    if usuario_encontrado:
        print("Usuario encontrado:", usuario_encontrado)
        print("Ya existe el instructor\n",nombre)
        op=input("¿Desea modificar los datos?\n Precione unicamente 1 para Si")
        if op =="1":
            materiaNew = input("Actualize la materia del instructor: ")
            telNew = input("Actualize el telefono del instructor: ")
            instru=instructores.get(nombre)
            instru["Materia"]=materiaNew
            instru["Tel"]=telNew
            print("Usuario Actualizado correctamente")        
    else:
        print("Usuario no encontrado.\nContinue el registro los datos del instructor",nombre)
        materia = input("Ingrese la materia del instructor: ")
        tel = input("Ingrese el telefono del instructor: ")
        instructores[nombre]={"Materia":materia,"Tel":tel}
def buscarR2():
    def buscar_valores(diccionario, texto):
        valores_coincidentes = []
        for valor in diccionario: #.values() muestra datos .items() muestra keys
            if texto.lower() in str(valor).lower():
                valores_coincidentes.append(valor)
        return valores_coincidentes        
    texto_busqueda = input("Ingrese el nombre del instructor: \n")
    resultados = buscar_valores(instructores, texto_busqueda)
    if resultados:
        print("Usuarios encontrados con el nombre:",texto_busqueda)
        cont=0
        for valor in resultados:
            cont=cont+1
            print(cont,". ",valor)               
    else:
        print("No se encontraron coincidencias.")
def borrar2():
    op="1"
    while(op=="1"):
        def buscar(lista,nombre):
            for usuario in lista:
                if usuario == nombre:
                    return usuario
            return None
        nombre=(input("Indique el nombre del instructor que desea Elimiar\n"))
        usuario_encontrado = buscar(instructores,nombre)    
        if usuario_encontrado:
            op=input("¿El usuario existe desa eliminarlo?\nDigite unicamente 1 para Si")
            if op =="1":
                print(f"********\nEl instructor: {nombre}\na sido Eliminado\n*********")
                del instructores[nombre]
                print("Su lista de instructores quedo de la siguiente manera:")
                cont=0
                for x, y in instructores.items():    
                    cont=cont+1                               
                    print("Posicion: ",cont,x,":", y)
                break                    
        else:
            print("**********\nUsuario no encontrado!!")
def listar2():
    cont=0
    print("Lista de Instructores registrados")
    for x in instructores:
        cont=cont+1
        print(cont,". ",x)

#INDEX *******  
print("Bienvenida al probador de retos con funciones instructora")                                
opRetos="0"
while(opRetos!="1" and opRetos!="2"):
    retos=input("¿Que reto desea probar?\nSeleccione,\n 1. reto 1\n 2. reto 3\n\t")
    if(retos=="1"):
        instructores = ["jenifer","Jonathan","c","A","B"]
        op="1"
        cont=-1
        print("Bienvenidos al SENA \nSeleccione una opscion ")
        while(op=="1"):
            opcion="0"
            while(opcion!="1" and opcion !="2" and opcion != "3" and opcion !="4" and opcion !="5" and opcion !="6" ):
                opcion = (input("\n 1. Agregar un instructor a la lista\n 2. Listar los instructores que están en la lista \n 3. Modificar un elemento de la lista \n 4. borrar un instructor, dependiendo su posicion \n 5. Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas \n 6. Ordenar la lista de instructores de la A-Z \n "))
                if(opcion=="1"):
                    agregar()
                    break
                elif(opcion=="2"):
                    Listar()
                    break            
                elif(opcion=="3"):
                    modificar()
                    break
                elif(opcion=="4"):
                    borra()
                    break
                elif(opcion=="5"):
                    buscar()
                    break           
                elif(opcion=="6"):
                    listar()
                    break
                else:
                    print("******************\nLos valores son incorrectos\nDigite unicamente un numero del 1 al 6")
            op=(input("Selcecione \n 1. Para volver en el menu BAUL \n 2. Cualquier otra tecla para salir"))
        print("Al FINAL su lista quedo de la siguiente manera:\n")
        for i in instructores:
            cont=cont+1
            print(i,"posicion",cont)
    elif(retos=="2"):
        #Reto 3
        instructores={
            'CESAR':{
                'Materia':"Adso",
                'Tel':"321316zx"
            },
            'CE2':{
                'Materia':"ABCz",
                'Tel':"0"
            },
            'CE3':{
                'Materia':"Xxz",
                'Tel':"321316"
            },
            'CE4':{
                'Materia':"ZZZ",
                'Tel':"321316"
            }
        }
        op="1"
        while (op =="1"):
            opcion="0"
            while(opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4"):
                print("Bienvenidos a la lista de instructores de la ficha2557861")
                opcion=input("Seleccione una opcion\n 1. Agregar/modificar:\n 2. Buscar\n 3. Borrar\n 4. Listar \n")
                if(opcion =="1"):
                    agregarR2()                    
                    break  
                elif(opcion=="2"):
                    buscarR2()
                    break
                elif(opcion=="3"):
                    borrar2()
                    break
                elif(opcion=="4"):
                    listar2()
                    break
                else:
                    print("*******     **********\tSeleccion incorrecta\t*******     ********")
                    print("**********************\t  Digite 1,2,3 o 4\t***********************")    
            op=input("Desea continuar? digite unicamente 1 para Si") 
        print("Gracias por visitarnos!")
    else:
        print("*******     **********\tSeleccion incorrecta\t*******     ********")
        print("**********************\t   Digite 1 o 2   \t***********************")
print("Gracias por visitarnos!")
