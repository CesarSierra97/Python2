# Realizar los retos 1 y 3 implementado funciones 

#Reto 1
#Definimos las funciones
def agregar():
    op="1"
    while(op=="1"):
        agregar=(input("Indique el nombre del instructor que desea agregar a la lista\n"))
        instructores.append(agregar)
        op=input("¿Desea agregar otro instructor?\n 1. para continuar \n 2. Cualquier tecla para terminar de agregar\n")
        print("Su lista de instructores quedo de la siguiente manera:\n")
        #for para listas
        for index, i in enumerate(sorted(instructores)):
            Rta=print(index+1,i)
    return Rta

def Listar():
    print("Su lista de instructores quedo de la siguiente manera:\n")
    #for para listas
    for index, i in enumerate(sorted(instructores)):
        print(index+1,i)


instructores = ["jenifer","Jonathan","c","A","B"]
op="1"
cont=-1
print("Bienvenidos al SENA \nSeleccione una opscion ")
while(op=="1"):
    opcion="0"
    while(opcion!="1" and opcion !="2" and opcion != "3" and opcion !="4" and opcion !="5" and opcion !="6" ):
        opcion = (input("\n 1. Agregar un instructor a la lista\n 2. Listar los instructores que están en la lista \n 3. Modificar un elemento de la lista \n 4. borrar un instructor, dependiendo su posicion \n 5. Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas \n 6. Ordenar la lista de instructores de la A-Z \n "))
        if(opcion=="1"):
            agregarInstructor=agregar()
            break
        elif(opcion=="2"):
            print("Su lista de instructores quedo de la siguiente manera:\n")
            #for para listas
            for index, i in enumerate(sorted(instructores)):
                print(index+1,i)
            break            
        elif(opcion=="3"):
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
            break
        elif(opcion=="4"):
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
            break
        elif(opcion=="5"):
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
            break           
        elif(opcion=="6"):
            print("Su lista de instructores esta de la siguiente manera:\n")
            instructores.sort()
            print(instructores)
            break
        else:
            print("******************\nLos valores son incorrectos\nDigite unicamente un numero del 1 al 6")