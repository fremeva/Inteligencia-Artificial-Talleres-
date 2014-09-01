__author__ = ''
#Librerias
import string, math, random, copy

#Funcion para obtener los valores de la Matriz de Adyacencia
def distancesFromCoords():
    '''
    @author: william
    Esta funcion toma el archivo berlin52 y produce una matriz con las distancias entre las ciudades.
    '''
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
ciudades=4                      #Numero de ciudades, como hes berlin52 serian 52.
alfa = 0.5                        #Alfa
beta = 1
p = 0.5                         #rooo
mHormigas = ciudades                    #Numero de Hormigas

#Matriz De Feromonas.
feromonaMatriz= [([0.1]*ciudades) for i in range(ciudades)]
def inversoMultiplicativo(matriz):
    inversa = copy.deepcopy(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(inversa[i][j]!=0):
                inversa[i][j] = (1.0/inversa[i][j])
    return inversa

matrizHeuristicaLocal= inversoMultiplicativo(distancias)

#Funcion para calular el costo de un tur.
def calcularCosto(tur):
    z=0
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
    '''
    Funcion para generar las Hormigas exploratorias(Tures iniciales)
    :param nhormigas: numeros de hromigas
    :param nciud: numeros de ciudades que recorre cada hormiga
    :return: una matriz de tures iniciales.
    '''
    salida=[]
    for i in range(nhormigas):
        tur=[]
        for j in range(nhormigas):
            tur=unTurAleatorio(nciud)
        salida.append(tur)

    return salida

def ActualizarMatrizFeromona(tur):
    costo = calcularCosto(tur)
    for i in range(len(tur)):
        if(i==(len(tur)-1)):
            feromonaMatriz[tur[i]][tur[0]]=feromonaMatriz[tur[i]][tur[0]]+(1.0/costo)
        else:
            feromonaMatriz[tur[i]][tur[i+1]]=feromonaMatriz[tur[i]][tur[i+1]]+(1.0/costo)

def evaporacionFeromona():
    for i in range (ciudades):
        for j in range(ciudades):
            feromonaMatriz [i][j]=(1-p)*feromonaMatriz[i][j]

def ciudadInicial():
    ciud = random.randrange(ciudades)
    return ciud

def sumatoria(ciudadActual,ciudadesVisitadas):
    salida=0.0
    for j in range(ciudades):

        if not(j in ciudadesVisitadas):
            salida=salida+((feromonaMatriz[ciudadActual][j])**alfa)*((matrizHeuristicaLocal[ciudadActual][j])**beta)
            print "SALIDA: " + str(salida)
            print "MatrizHeuristica " + str(matrizHeuristicaLocal[ciudadActual][j])

    return salida

def elegirCiudad(probabilidades):
    numeroAleatoreo = random.random()
    for i in range(len(probabilidades)):
        if(numeroAleatoreo<=probabilidades[i]):
            return i

def recorrido():
    probabilidades=[]
    ciudadesVisitadas=[]
    ciudadActual = ciudadInicial()
    ciudadesVisitadas.append(ciudadActual)
    for i in range(ciudades):
        if(ciudadActual==i):
            probabilidades.append(0.0)
        else:
            prob = float((feromonaMatriz[ciudadActual][i]**alfa)*(matrizHeuristicaLocal[ciudadActual][i])/sumatoria(ciudadActual,ciudadesVisitadas))
            probabilidades.append(prob)
        print probabilidades
        ciudadElegida = elegirCiudad(probabilidades)
        ciudadActual = ciudadElegida
        ciudadesVisitadas.append(ciudadElegida)
    return ciudadesVisitadas


#INICIO
#Generamos las hormigas exploradoras
hormigasExploradoras = tures_iniciales(mHormigas,ciudades)

#for i in range(ciudades):
    #ActualizarMatrizFeromona(hormigasExploradoras[i])

#iteraciones = 2

print feromonaMatriz
'''matrizHeuristicaLocal=[[0, 1/3, 1/2, 1/4],
                       [1/3,0,1/8,1/9],
                       [1/2,1/8,0,1/10],
                       [1/4,1/9,1/10,0]]'''


matrizHeuristicaLocal=[[0,0.333,0.5,0.25],
                       [0.333,0,0.125,0.1111],
                       [0.5,0.125,0,0.1],
                       [0.25,0.1111,0.1,0]]


print matrizHeuristicaLocal
cvisitadas=[]
cvisitadas.append(1)
print sumatoria(1,cvisitadas)





