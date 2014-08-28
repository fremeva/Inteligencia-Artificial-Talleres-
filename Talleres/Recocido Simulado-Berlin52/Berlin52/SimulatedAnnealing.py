__author__ = 'FDL'
#****Librerias****
import math
import random
import copy

nciudad = 52            #Numero de ciudad para el Tur (EN ESTE CASO ES 52)
x =[]                   #Lista de los Puntos x de las coordenadas de cada ciudad
y =[]                   #Lista de los Puntos y de las coordenadas de cada ciudad
mcoordenada = []        #Matriz de las coordenadas [nciudad][2]
amatriz= []             #Matriz de Adyacencia
k=0                     #Variable aux de indice de la lista x[]
l=0                     #Variable aux de indice de la lista y[]

#Contruimos la Matriz de coordenadas  y la inicializamos en 0 cada elemento
for i in range(nciudad):
    mcoordenada.append([0]*2)
#Contruimos la Matriz de Adyacencia y la inicializamos en 0 cada elemento
for i in range(nciudad):
    amatriz.append([0]*nciudad)

#Lee archivo con las coordenadas
archivo = open("datos.txt","r")
while True:
    linea = archivo.readline()
    dato= linea.partition(" ")
    aux = dato[2].partition(" ")
    if (aux[0] != ''):
        x.append(float(aux[0]))
    aux = aux[2].partition(" ")
    if (aux[0] != ''):
        y.append(float(aux[0]))
    if not linea: break

#llenar la matriz de coordenadas por parejas de con cada una de las listas x[], y[]
for i in range(nciudad):
    for j in range(2):
        if j==0:
            mcoordenada[i][j] = x[k]
            k=k+1
        else:
            mcoordenada[i][j] = y[l]
            l=l+1

#Llenando la matriz de adyacencia de los costos de cada una de las ciudades.
for i in range(nciudad):
    for j in range(nciudad):
        amatriz[i][j] = math.sqrt(math.pow((mcoordenada[j][0]-mcoordenada[i][0]),2) + math.pow((mcoordenada[j][1]-mcoordenada[i][1]),2))

#Funcion para generar un tur Inicial
def xInicial():
    tur=[0]*nciudad
    for i in range(nciudad):
        tur[i]=i+1

    random.shuffle(tur)
    return tur

def calcularZ(tur):
    z=0
    for i in range(0,nciudad):
        if (i<nciudad-1):
            z = z + amatriz[(tur[i]-1)][(tur[i+1]-1)]
        else:
            z = z + amatriz[(tur[i]-1)][(tur[0]-1)]
    return z

def perturbacion(tur):
    ciud = random.choice(tur)
    pos1 = tur.index(ciud)
    while True:
        pos2 = tur.index(random.choice(tur))
        if (pos1 != pos2):
            tur[pos1],tur[pos2] = tur[pos2], tur[pos1]
            break
    return tur



#INICIO
T=10000                         #Temperatura Inicial
inicial_tur=[]                      #Tur Inicial.
alfa=0.99                           #Enfriamiento
niteracion=10000                    #numero de iteraciones
inicial_tur=xInicial()              #Obtenemos el recorrido inicial
z_inicial=calcularZ(inicial_tur)    #calculamos el costo Inicial

for c in range(niteracion):
    nuevo_tur= copy.deepcopy(inicial_tur)
    nuevo_tur = perturbacion(nuevo_tur) #Perturbamos la solucion Inicial
    z_nueva=calcularZ(nuevo_tur)        #Calculamos el Nuevo costo con el recorrido perturbado
    if(z_nueva<z_inicial):
        inicial_tur=copy.deepcopy(nuevo_tur)
        z_inicial=z_nueva
    else:
        z_delta = z_nueva - z_inicial   #Delta de Z
        prob=math.pow(math.e,(-1*z_delta/T))  #Distribucion de probabilidad
        n=random.random()
        if (n<prob):
            inicial_tur=copy.deepcopy(nuevo_tur)
            z_inicial=z_nueva
    T = alfa*T

#SALIDAS
print "una Solucion Optima es: ", z_inicial
print "Tur correspondiente es:", inicial_tur
