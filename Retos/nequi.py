# ***************     NEQUI           ***********************************************
# Cree una carpeta llamada Nequi y cree en él un programa que simule las siguientes funcionalidades de la aplicación Nequi Colombia:
# Acceso a la aplicación: Solicitar número de celular y clave de 4 dígitos:
# Si usuario y contraseña son correctos permitir el acceso 
# Si alguno no es correcto mostrar mensaje ¡Upps! Parece que tus datos de acceso no son correctos, Tienes tres intentos más
# Si los tres intentos se agotan debe terminar la ejecución
# Al ingresar deberá mostrar saldo Disponible el cual tendrá un valor inicial de 4500
# Funcionalidades: Nequi cuenta con varias opciones que usted deberá programar acorde a lo siguiente:
# Saca: Le permitirá escoger entre 2 opciones Cajero, Punto físico, si saldo es < 2000 no podrá hacer el retiro y deberá mostrar el mensaje No te alcanza de lo contrario confirmar cuanto desea retirar y generar código de 6 dígitos para el retiro.
# Envía: Le solicitará el número de teléfono al que desea enviar dinero, así como el valor a enviar, deberá validar que el valor a enviar no sea superior al saldo disponible, en cuyo caso deberá decir que no es posible enviar el dinero, si se envía el dinero deberá hacerse el respectivo descuento al saldo.
# Recarga: Le solicitará al usuario el valor a recargar, le pedirá que confirme que desea realizar la recarga si responde que sí se realizará la recarga de lo contrario
# Salir: Salir saldrá de la aplicación Nequi
# El programa deberá repetir las funciones tantas veces como el usuario desee, el saldo deberá mostrar el cambio después de cada transacción.
# Proponga dos funcionalidades más de Nequi que pueda desarrollar aplicando estructuras algorítmicas
disponible=4500
intentos=3
for i in range (1,4):
    password=1234
    cel=int(input("***Bienvenido a Nequi.Sena\n   Digite sus credenciales de acceso\n\nDigite su numero de celular\n"))
    pas=int(input("Digite su password\n"))
    if(cel==3213162622 and pas==1234):
        op=1
        while(op==1):
            selec=int(input(f"Bienvenido a su cuenta Usuario 3213162622 su saldo actual es de: {disponible} \nSelecciones una opcion\n 1. Sacar \n 2. Enviar \n 3. Recarga \n 4. Verificar 4x1000 \n 5. Crear un colchon\n 6. Salir\n"))
            if(selec==1):
                sacar=int(input(f"¿Cuanto desea retirar?\n Recuerde que cuenta con {disponible}\n"))
                if(sacar<disponible):
                    op2=int(input("Seleccione \n 1. Para retirar en cajero\n 2. Para retirar punto fisico\n"))
                    if(op2==1):
                        if(disponible>=2000):                           
                            disponible=disponible-sacar
                            print("Su codigo para retirar en cajero es CAJERO1234\n")
                        else:
                            print("**Fondos incuficientes para sacar\n")
                    if(op2==2):
                        if(disponible>=2000):                            
                            disponible=disponible-sacar
                            print("Su codigo para retirar en punto fisico es FISICO1234\n")
                        else:
                            print("**Fondos incuficientes para sacar\n")                    
                else:
                    print("**Fondos incuficientes para sacar\n **Operacion NO realizada")       
                print(f"Su saldo actual es de: {disponible}\n")
            elif(selec==2):
                enviar=int(input("Digite el monto a enviar: \n$ "))
                tel=int(input("Digite el numero de telefono al que va enviar: \ntel "))
                if(enviar<disponible):
                    disponible=disponible-enviar
                    print(f"Se enviaron ${enviar} al tel {tel} su saldo actual es de:\n ${disponible}\n")
                else:
                    print("**Fondos incuficientes para realizar el envio \n\n **Operacion NO realizada\n")
            elif(selec==3):
                recargar=int(input("Digite el valor que desea recargar\n $ "))
                op1=int(input(f"Su saldo actual es de {disponible}\n Desea realizar la recarga de ${recargar}\n Seleccione\n 1. Si Recargar\n 2. No, Salir\n"))
                disponible=disponible+recargar
                if(op1==1):
                    print(f"Su recarga de ${recargar} fue Exitosa\n Su saldo actual es de ${disponible} ")
                else:
                    print("Precione enter para continuar...")
            elif(selec==4):
                print(f"El 4x1000  que debe pagar de su saldo ${disponible} es de {(disponible*4)/1000} ")
            elif(selec==5):
                colchon=input("Digite el nombre del colchon\n")
                ahorro=int(input("Digite el valor que desea ahorrar\n"))
                if(ahorro<=disponible):
                    disponible=disponible-ahorro
                    print(f"Colchon {colchon} creado Exitosamente, \nCuentas con un ahorro de ${ahorro}\n Su saldo actual es de ${disponible}")
                else:
                    print("**Fondos incuficientes para realizar el envio \n\n **Operacion NO realizada\n")
            else:
                break
            op=int(input("Selcecione \n 1. Para volver en el menu Nequi\n 2. Para salir del programa\n"))
        break                  
    else:
        intentos=intentos-1
        print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {intentos} intentos \n*Precione enter para continuar")
print("*********Gracias vuelve pronto*********")


