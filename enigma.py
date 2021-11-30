from tabulate import tabulate
# la libreria tabulate permite visualizar las 
# listas como tablas, lo cual resulta util en ciertos problemas

# ----------------------------------------------------------------------------------------------------------------------------
# :::::::::::::::::::::::::::::::        FUNCIONES       :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ----------------------------------------------------------------------------------------------------------------------------


# [1] ------------------------------------------------------------------------------------------------------------------------
# :::::::::::::::::::::::::::::::      funcion rotaAntihorario    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ----------------------------------------------------------------------------------------------------------------------------
def rotaAntiHorario(serieTiempo,step):
    # se clona por asignación para no modificar la variable original
    aux = list(serieTiempo)
    
    for i in range(0,step):
        # agrega el primer elemento al final
        aux.append(aux[0])
        # remueve el primer elemento
        aux.pop(0)
    return aux 

# [2] ------------------------------------------------------------------------------------------------------------------------
# :::::::::::::::::::::::::::::::      funcion: rotaHorario    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ----------------------------------------------------------------------------------------------------------------------------

def rotaHorario(serieTiempo,step):
    # se clona por asignación para no modificar la variable original   
    aux = list(serieTiempo)
    for i in range(0,step):
        # se invierte la serie
        aux.reverse()
        # agrega el primer elemento al final
        aux.append(aux[0])
        # remueve el primer elemento
        aux.pop(0)
        aux.reverse()
    return aux  

# [3] ------------------------------------------------------------------------------------------------------------------------
# :::::::::::::::::::::::::::::::      funcion: buscaLetra     :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ----------------------------------------------------------------------------------------------------------------------------

def buscaLetra(letra,oracion):
    # Esta funcion indica la posicion en la que se encunetra una letra dentro de una oracion
    aux = "".join(oracion)
    posicion = aux.find(letra)
    return posicion

# [4] ------------------------------------------------------------------------------------------------------------------------
#  :::::::::::::::::::::::::::::::      funcion: trayectoria     :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------------------------------------------------------------------
# esta funcion va conectando los puntos para ir obteniendo el valor auxiliar y final de la letra encriptada




# [5] ------------------------------------------------------------------------------------------------------------------------
# :::::::::::::::::::::::::::::::        funcion controlReloj     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------------------------------------------------------------------
# esta funcion debe contabilizar el numero de movimientos realizados y cada 28



# ======================================================================================================================
#                                                              MAIN 
# ======================================================================================================================


# TRAINNING DEMO
A = [1,2,3,4,5]

# -----------------------------------------------------------------------------------------------------------------------
#                                                       ENGRANAJES
# -----------------------------------------------------------------------------------------------------------------------
# Defincion de constantes:

# ENGRANAJE (ROTOR) 1 (en su posición incial por defecto)
# -----------------------------------------------------------------------------------------------------------------------
alfabeto_11   = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabeto_12   = ['b','d','f','h','j','l','c','p','r','t','x','v','z','n','y','e','i','w','g','a','k','m','u','s','q','o']


# ENGRANAJE (ROTOR) 2 (en su posición incial por defecto)
# -----------------------------------------------------------------------------------------------------------------------
alfabeto_21   = list(alfabeto_11)
alfabeto_22   = ['a','j','d','k','s','i','r','u','x','b','l','h','w','t','m','c','q','g','z','n','p','y','f','v','o','e']

# ENGRANAJE (ROTOR) 3 (en su posición incial por defecto)
# -----------------------------------------------------------------------------------------------------------------------
alfabeto_31   = list(alfabeto_11)
alfabeto_32   = ['e','k','m','f','l','g','d','q','v','z','n','t','o','w','y','h','x','u','s','p','a','i','b','r','c','j']

# -----------------------------------------------------------------------------------------------------------------------
# MAQUINA CRIPTOGRAFICA: ENIGMA
# -----------------------------------------------------------------------------------------------------------------------

a = list(zip(alfabeto_11,alfabeto_12))
b = list(zip(alfabeto_21,alfabeto_22))
c = list(zip(alfabeto_31,alfabeto_32))

listaPareada  = list(zip(a,b,c))

# -----------------------------------------------------------------------------------------------------------------------
# MAQUINA CRIPTOGRAFICA ENIGMA ROTADA 
# Configurando la posicion inicial de los 3 engranajes
# -----------------------------------------------------------------------------------------------------------------------

# configuracion incicial
letra_1 = 'a'
letra_2 = 'b'
letra_3 = 'c'

aux_rotacion_1  = buscaLetra(letra_1,alfabeto_11)
aux_rotacion_2  = buscaLetra(letra_2,alfabeto_21)
aux_rotacion_3  = buscaLetra(letra_3,alfabeto_31)

step_rotacion_c = aux_rotacion_1
step_rotacion_b = aux_rotacion_2
step_rotacion_a = aux_rotacion_3

a_rotado = rotaAntiHorario(a,step_rotacion_a)
b_rotado = rotaAntiHorario(b,step_rotacion_b)
c_rotado = rotaAntiHorario(c,step_rotacion_c)
# los engranajes estan numerados en orden inverso (derecha a izquierda -> antihorario)
listaPareadaRotada  = list(zip(a_rotado,b_rotado,c_rotado))


# -----------------------------------------------------------------------------------------------------------------------
# SALIDA POR PANTALLA
# -----------------------------------------------------------------------------------------------------------------------

# TRAYECTORIA CRIPTOGRAFICA (FLUJO CRIPTOGRAFICO)
# [ LETRA INPUT ] --> [ ENGRANAJE 3 ] --> [ ENGRANAJE 2 ] --> [ ENGRANAJE 1 ] --> REGLECTOR --> ...
# [ ENGRANAJE 2 ] --> [ ENGRANAJE 1 ] --> [ ENGRANAJE 2 ] --> [ ENGRANAJE 3 ] --> [ LETRA OUTPUT 
# ]

# -----------------------------------------------------------------------------------------------------------------------
# +--------------+    +-------------+    +---------------+  +-------------+    +------------+
# | LETRA INPUT  +--> | ENGRANAJE 3 +--> | ENGRANAJE 2   |  | ENGRANAJE 1 +--> | REFLECTOR  |
# +--------------+    +-------------+    +---------------+  +-------------+    +------------+
# -----------------------------------------------------------------------------------------------------------------------

# LETRA INPUT --> ENGRANAJE 1
print('---------------------------------------------------------')
print('LETRA INPUT --> ENGRANAJE 1')
input_3 = 'e'
id_empalme_3 = buscaLetra(input_3,alfabeto_32)
output_3     = alfabeto_31[id_empalme_3];
print('     Letra buscada ENGRANAJE 3')
print('     '+str(input_3))
print('     Lugar donde fue encontrada')
print('     '+str(id_empalme_3))
print('     Letra de encriptacion')
print('     '+str(output_3))


# ENGRANAJE 1 --> ENGRANAJE 2 
print('---------------------------------------------------------')
print(a_rotado[:])
print('ENGRANAJE 1 --> ENGRANAJE 2')
input_2 = output_3
id_empalme_2 = buscaLetra(input_2,alfabeto_22) # CONEXION POR CABLEADO INTERNO 
print('     Letra buscada en el ENGRANAJE 2')
print('     '+str(input_2))
print('     Lugar donde fue encontrada')
print('     '+str(id_empalme_2))

# ENGRANAJE 2 --> ENGRANAJE 3
# ENGRANAJE 3 --> REGLECTOR
# 
# REFLECTOR   --> ENGRANAJE 3
# ENGRANAJE 3 --> ENGRANAJE 2
# ENGRANAJE 2 --> ENGRANAJE 1
# ENGRANAJE 1 --> LETRA OUTPUT




#condicion = True
condicion = False
if (condicion):
    print('')
    print('Rotacion en sentido antihorario:')
    print(A)
    print(rotaAntiHorario(A,2))
    print('')
    print('Rotacion en sentido horario:')
    print(A)
    print(rotaHorario(A,2))
    print('')
print('===========================================================')
print('Máquina criptográfica')
print('===========================================================')
#print(tabulate(listaPareada))
print('')
print('===========================================================')
print('Máquina criptográfica ROTADA')
# los engranajes estan numerados en orden inverso (derecha a izquierda -> antihorario)
print('ENGRANAJE 1 ROTADO: '+str(aux_rotacion_3)+' veces')
print('ENGRANAJE 2 ROTADO: '+str(aux_rotacion_2)+' veces')
print('ENGRANAJE 3 ROTADO: '+str(aux_rotacion_1)+' veces')
print('===========================================================')
print(tabulate(listaPareadaRotada))


'''
for id, letra in enumerate(disco):
    if entrada == letra and indice != id:
      indice_salida = id
'''