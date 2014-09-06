__author__ = 'Fredy'
#Librerias
import string, math, random, copy

#Funcion para obtener los valores de la Matriz de Adyacencia
def distancesFromCoords():
    f = open('berlin52.tsp')
    data = [string.split(line.replace("\n",""), " ")[1:] for line in f.readlines()[6:58]]
    coords =  map(lambda x: [float(x[0]),float(x[1])], data)
    distances = []
    for i in range(len(coords)):
        row = []
        for j in range(len(coords)):
            row.append(math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2))
        distances.append(row)
    return distances
#---------------------------------------------------------------
###Matriz de Adyacencia de las distancias entre las ciudades.###
distancias = distancesFromCoords()

#-------------------------------------------
#Variables Importantes
ciudades=52                      #Numero de ciudades, como hes berlin52 serian 52.
alfa = 1.                        #Alfa
beta = 2.
roo = 0.5                         #rooo
mHormigas = ciudades                    #Numero de Hormigas
nHormigExploradora = 100

#Matriz De Feromonas.
feromonaMatriz= [([0.01]*ciudades) for i in range(ciudades)]

def inversoMultiplicativo(matriz):
    inversa = copy.deepcopy(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(inversa[i][j]!=0):
                inversa[i][j] = (1.0/inversa[i][j])
    return inversa

#Matriz Heuristica Local
matrizHeuristicaLocal= inversoMultiplicativo(distancias)

#Funcion para calular el costo de un tur.
def calcularCosto(tur):
    z=0.0
    for i in range(0,len(tur)):
        if (i<(len(tur)-1)):
            z = z + distancias[(tur[i])][(tur[i+1])]
        else:
            z = z + distancias[(tur[i])][(tur[0])]
    return z

#Funcion para generar un tur aleatorio
def unTurAleatorio(nciud):
    tur=[0]*nciud
    for i in range(nciud):
        tur[i]=i
    random.shuffle(tur)
    return tur

def tures_iniciales(nhormigas,nciud):
    salida=[]
    for i in range(nhormigas):
        tur=[]
        tur=unTurAleatorio(nciud)
        salida.append(tur)
    return salida

def ActualizarMatrizFeromona(tur):
    costo = calcularCosto(tur)
    var = 1.0/costo
    for i in range(len(tur)):
        if(i==(len(tur)-1)):
            feromonaMatriz[tur[i]][tur[0]]=feromonaMatriz[tur[i]][tur[0]]+var
        else:
            feromonaMatriz[tur[i]][tur[i+1]]=feromonaMatriz[tur[i]][tur[i+1]]+var

def evaporacionFeromona():
    for i in range (0,ciudades):
        for j in range(0,ciudades):
            feromonaMatriz [i][j]=(1-roo)*feromonaMatriz[i][j]

def ciudadInicial():
    ciud = random.randrange(ciudades)
    return ciud

def sumatoria(ciudadActual,ciudadesVisitadas):
    salida=0.00000000000001
    for j in range(ciudades):
        if not(j in ciudadesVisitadas):
            salida=salida+((feromonaMatriz[ciudadActual][j])**alfa)*((matrizHeuristicaLocal[ciudadActual][j])**beta)

    return salida

def elegirCiudad(probabilidad):
    numeroAleatorio=random.random()
    ciudad=probabilidad.keys()[0]
    for i in probabilidad.keys():
            if numeroAleatorio>probabilidad[i]:
                if probabilidad[i]>probabilidad[ciudad]:
                    ciudad=i
            else:
                if probabilidad[i]>probabilidad[ciudad]:
                    ciudad=i

    return ciudad

def recorrido():
    probabilidades={}
    ciudadesVisitadas=[]
    ciudadActual = 0
    for j in range(ciudades):
        if(ciudadActual==j):
            probabilidades[j]=0
        else:
            prob = float((feromonaMatriz[ciudadActual][j]**alfa)*((matrizHeuristicaLocal[ciudadActual][j])**beta)/sumatoria(ciudadActual,ciudadesVisitadas))
            probabilidades[j]=prob

        ciudadElegida = elegirCiudad(probabilidades)
        #print ciudadElegida
        #ESTO DEBERIA ESTAR FUERA DEL CICLO PERO SI LO SACO ME SALE ERROR DE DIVISION ENTRE ZERO :(
        probabilidades.clear()
        ciudadActual = ciudadElegida
        ciudadesVisitadas.append(ciudadActual)
    return ciudadesVisitadas


#INICIO
#Generamos las hormigas exploradoras
costoOptimo=0.0
inicalesTur = tures_iniciales(nHormigExploradora,ciudades)
for i in range(0,ciudades):
    ActualizarMatrizFeromona(inicalesTur[i])

evaporacionFeromona()

for t in range(10):
    for i in range(52):
        turRecorrido = copy.deepcopy(recorrido())
        costoNuevo=calcularCosto(turRecorrido)
        if costoOptimo<costoNuevo:
            costoOptimo=costoNuevo
            rutaOptima=copy.deepcopy(turRecorrido)

    ActualizarMatrizFeromona(turRecorrido)
    evaporacionFeromona()

print rutaOptima
print str(calcularCosto(rutaOptima))







