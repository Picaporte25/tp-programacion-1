# #Ejercicio 1)
# # Añadir las siguientes frutas con sus respectivos precios:
# # ● Naranja = 1200
# # ● Manzana = 1500
# # ● Pera = 2300
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# #Añadido de las frutas con sus precios
# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# # ● Banana = 1330
# # ● Manzana = 1700
# # ● Melón = 2800
# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1700
# precios_frutas["Banana"] = 2800

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# # precios.
# print(precios_frutas.keys())

# # 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# # • Luego, pedí un nombre y mostrale el número asociado, si existe.
# diccionario= {}#Creacion del diccionario
# for x in range(5):#ciclo for para hacer las preguntas 5 veces y asi almacenar los 5 nombres
#     clave=input("Ingrese el nombre: ")
#     valor=input(f"Ingrese el valor de {clave}: ")
#     diccionario[clave]=valor#aqui lo que hacemos es en diccionario amacenar la variable CLAVE y asignarle mediante un igual el valor que el usuario pida
# nombre_buscar=input("Escriba un nombre y te diremos el numero que este vinculado al mismo: ")#Hacemos la pregunta para que vea si esta o no esta el nombre que busca
# if nombre_buscar in diccionario:
#     print(f"El numero vinculado a {nombre_buscar} es: {diccionario[nombre_buscar]}")
# else:
#     print("El nombre no esta registrado en la  lista")

# # 5) Solicita al usuario una frase e imprime:
# # • Las palabras únicas (usando un set).
# # • Un diccionario con la cantidad de veces que aparece cada palabra
# frase=input("Ingrese una frase: ")#Ingreso de frase
# frase_minusculas=frase.lower()#pasamos la frase a minusculas
# frase_de_palabras=frase_minusculas.split()#separamos cada palabra a travez del split que separa cuando hay un espacio
# set_frase=set(frase_de_palabras)#realizamos el conjunto
# diccionario_frases={}#diccionario
# for palabra in frase_de_palabras:#bucle
#     if palabra in diccionario_frases:
#         diccionario_frases[palabra] +=1
#     else:
#         diccionario_frases[palabra]= 1
# print(f"Las palabras que escribiste de forma unica: {set_frase}")
# print(f"Y este es el resultado de tus palabras  con su respectiva cuenta de cada una de ellas: {diccionario_frases}")



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# diccionario={} # creacion de diccionario
# for x in range(3):# bucle
#     alumnos = input("\nIngresa el nombre del alumno: ")

#     notas = input("Ingresa las 3  notas del alumno puestas una al lado de la otra (# SEPARADAS MEDIANTE ESPACIOS #):")
#     notas_separadas = notas.split()

#     notas_lista=[]#creacion de una lista vacia que va a servir para convertir los datos de notas_separadas a number o flotante
#     for nota in notas_separadas:
#         nota_Float=float(nota)#conversion a flotante
#         notas_lista.append(nota_Float)
    
#     #calcular el promedio
#     suma=sum(notas_lista)
#     divisor=len(notas_lista)
#     promedio= suma / divisor

#     notas_tupla=tuple(notas_lista)#conversion de la lista notas a una tupla
#     diccionario[alumnos]=notas_tupla#asignamos la key con su value ( key = alumnos, value= notas_tupla)
#     print(f"\nEl promedio de {alumnos} es de {promedio}")#mensaje
#     print(diccionario)#imprimir diccionario



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# parcial_1={"Gaizka","Irene","Dario","Inaki"}
# parcial_2={"Inaki","Gaizka","Elias","Avernal"}

# aprobaron_ambos_parciales= parcial_1 & parcial_2 
# aprobaron_solo_un_parcial=parcial_1 ^ parcial_2
# lista_total_que_aprobaron_al_menos_un_parcial=parcial_1 | parcial_2

# print(f"Los que aprobaron ambos parciales son: {aprobaron_ambos_parciales}")
# print(f"Los que aprobaron solo un  parcial son: {aprobaron_solo_un_parcial}")
# print(f"Los que aprobaron al menos un  parcial son: {lista_total_que_aprobaron_al_menos_un_parcial}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

# diccionario={"RX-6800XT":4,"Ryzen-5-9600X":4}

# while True:
#     print("---  MENU  ---")
#     print("\nCuando desee salir de la operacion pulse CERO(0)")
#     print(f"Aqui tiene la lista de productos disponibles: {diccionario}")
#     respuesta=input("Que producto desea comprar ? ")
    
#     if respuesta == "0":
#         print("Hasta luego!")
#         break
#     if respuesta in diccionario:
#         diccionario[respuesta]+=1
#     else:
#         diccionario[respuesta]=1

    
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
#  agenda= {
#   ("lunes", "10:00"):"Reunion",
#   ("martes","15:00"):"clase de ingles"
#  }
# permiti consultar que actividad hay en cierto dia y hora

# agenda = {
# ("Lunes","19:00"):"Tenis",
# ("Martes","10:00"):"Gimnasio",
# ("Miercoles","20:00"):"Clase de programacion",
# ("Jueves","21:00"):"Cena",
# ("Viernes","13:00"):"Mantenimiento PC",
# }

# while True:
#     print("- - - - Para salir de la operacion pulse CERO (0) - - - -")
    
#     dia= input("Que dia queres consultar si tenes actividades pendientes?: ").title() 
#     if dia == "0":
#         print("Hasta luego !")
#         break

#     hora=input("Que horario desea consultar?: ").title()
#     if hora == "0":
#         print("Hasta luego !")
#         break

#     clave = (dia, hora)
#     if clave in agenda:
#         print(f"La actividad pendiente en esa fecha y dia es: {agenda[clave] }")
#     else:
#         print("Para ese día o ese horario no hay actividades pendientes.")      


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# diccionario={"Buenos Aires":"Argentina","Santiago":"Chile","Bogota":"Colombia","Washington D. C.":"EE.UU."}

# print(diccionario)