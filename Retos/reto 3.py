#Autor: Cesar Sierra

# Escribir un diccionario llamado instructores2557861. En él se podrán
# guardar nombres, materia y telefono que dicta cada instructor que le
# orienta este trimestre. El programa mostrará el siguiente menú:
# 1. Agregar/modificar: Nos pide el nombre del instructor. Si el nombre
# se encuentra en la agenda, debe mostrar la materia y el teléfono y,
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no
# se encuentra, debe permitir ingresar los datos correspondientes.
# 2. Buscar: Nos pide ingresar un texto de búsqueda y nos muestra todos
# los contactos cuyos nombres comiencen por dicha cadena.
# 3. Borrar: Nos pide ingresar el nombre del instructor y si existe nos
# preguntará si queremos borrarlo de la agenda.
# ¿Cómo podría borrar un key dentro de un instructor en particular?
# 4. Listar: Nos muestra todos los instructores de la agenda.
instructores={
    'CESAR':{
        'Materia':"Adso",
        'Tel':"321316z"
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
                    break
            else:
                print("Usuario no encontrado.\nContinue el registro los datos del instructor",nombre)
                materia = input("Ingrese la materia del instructor: ")
                tel = input("Ingrese el telefono del instructor: ")
                instructores[nombre]={"Materia":materia,"Tel":tel}
                break
            break  

        elif(opcion=="2"):
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
            break
        elif(opcion=="3"):
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
            break
        elif(opcion=="4"):
            cont=0
            print("Lista de Instructores registrados")
            for x in instructores:
                cont=cont+1
                print(cont,". ",x)
            break
        else:
            print("*******     **********\tSeleccion incorrecta\t*******     ********")
            print("**********************\t  Digite 1,2,3 o 4\t***********************")    
    op=input("Desea continuar? digite unicamente 1 para Si") 
print("Gracias por visitarnos!")
        

    

