#!/usr/bin/env python
import math 

 
nciudad = 5
x =[]
y =[]
		 
#Lee archivo con las coordenadas
d = open("datos.txt","r")
while True:
		linea = d.readline()
		dato= linea.partition(" ")
		aux = dato[2].partition(" ")
		if (aux[0] != ''):
			x.append(float(aux[0]))
		
		aux = aux[2].partition(" ")
		if (aux[0] != ''):
			y.append(float(aux[0]))
		if not linea: break 

#Crear matriz [52][2]
mcoordenada = []

for i in range(nciudad):
	mcoordenada.append([0]*2)
k=0
l=0
for i in range(nciudad):
	for j in range(2):
		if j==0:
			mcoordenada[i][j] = x[k]
			k=k+1
		else:
			mcoordenada[i][j] = y[l]
			l=l+1



amatriz= []
for i in range(nciudad):
	amatriz.append([0]*nciudad)


for i in range(nciudad):
	for j in range(nciudad):
		amatriz[i][j] = math.sqrt(math.pow((mcoordenada[j][0]-mcoordenada[i][0]),2) + math.pow((mcoordenada[j][1]-mcoordenada[i][1]),2))
		
print amatriz




	

	


  
	





			
			

		


	
	





    

  
	
	

	
	
	
	
	
	

	

	
	


	





