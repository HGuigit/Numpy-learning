import numpy as np
from math import pi

a = np.array([1,2,3], dtype = 'int16')
b = np.array([[9.0,7.0,8.0] , [7.0,5.0,3.0]])

#pegar dimensão
#print(a.ndim)
#print(b.ndim)

#formato
#print(a.shape)
#print(b.shape)

#Tipo
#print(a.dtype)
#print(b.dtype)

#Tamanho cada elemento
#print(a.itemsize)#bytes
#print(b.itemsize)

#Tamanho total
#print(a.size*a.itemsize)
#print(a.nbytes)

##### Trocando elementos especificos colunas linhas etc #####
c = np.array([[1,2,3,4,5,6,7],[3,4,5,6,7,8,9]])
#print(c[1][5])#same
#print(c[1,5])#same
#print(c[1,-2])#same

#Pegar linha específica
#print(c[0][:])
#print(c[0,:])

#Coluna específica
#print(c[:,2])

#Pegar intervalo
#print(c[0, 1:6:2]) #3º numero depois dos 2 pontos é o passing, ler de dois em dois

#Tridimensional

d = np.array([[[1,2], [3,4]] , [[5,6], [7,8]]])
#print(d)
#print(d[0,1,1])#Numero 4
#print(d[0,1,:])
#print(d[:,1,:])

#inicializar matriz de 0
#e = np.zeros(5)
#print(e)
#e = np.zeros((2,3))#Duplo parenteses pois estou passando um vetor do tipo tupla dentro da função
#print(e)
#e = np.zeros((2,3,3))
#print(e)
# = np.zeros((2,3,3,3))
#print(e)

#Matriz de 1 e qualquer outro numero
#e = np.ones((2,3,3) , dtype = 'int32')
#print(e)
#e = np.full((2,2), 99 , dtype = 'float32')
#print(e)

#Numeros decimais randomicos entre 0  e 1
#f = np.random.rand(4,4,2)
#print(f)

#Numero inteiros randomicos
#f = np.random.randint(-10,40 , size=(3,3))
#print(f)

#Matriz identidade
#g = np.identity(4)
#print(g)

#Repetição array
#arr = np.array([1,2,3])
#r1 = np.repeat(arr,3, axis = 1)
#print(r1)  
#arr = np.array([[1,2,3]])
#r1 = np.repeat(arr,3,axis = 0)
#print(r1)   

#Exerício matriz
#tam = 5
#arr = np.ones((5,tam), dtype='int16')
#arr[1:(tam-1), 1:(tam-1)] = 0
#arr[int((tam-1)/2) , int((tam-1)/2) ] = 9
#print(arr)

#Outra solução
#arr = np.ones((5,5), dtype = 'int16')
#z = np.zeros((3,3), dtype = 'int16')
#z[1,1] = 9
#arr[1:4,1:4] = z
#print(arr)

#Cuidado ao copiar!!!
#ERRADO
#a = np.array([1,2,3])
#b = a 
#b[0] = 100
#print(b)
#print(a)

#CERTO
#a= np.array([1,2,3])
#b = a.copy()
#b[0] = 100
#print(b)
#print(a)

#Funções matemáticas do Numpy
#a = np.array([1,2,3,4])
#print(a+2)
#print(a-2)
#print(a*2)
#print(a/2)
#b = np.array([1,0,1,0])
#print(a+b)
#print(a**2)
#print(np.sin(a))
#print(np.sin(b))
#print(np.cos(a))


#####ALGEBRA LINEAR#####

#a = np.ones((2,3))
#print(a)    
#b = np.full((3,2), 2)
#print(b)
#print(np.matmul(a,b))#same
#print(np.dot(a,b))#same
#c = np.identity(3)
#print(np.linalg.det(c))#Determinante


##### STATISTICS #####

#stats = np.array([[1,2,3],[4,5,6]])
#print(np.min(stats, axis = 1))
#print(np.min(stats, axis = 0))
#print(np.min(stats))
#print(np.max(stats))
#print(np.max(stats, axis = 1))
#print(np.max(stats, axis = 0))
#print(np.sum(stats))
#print(np.sum(stats, axis = 0))
#print(np.sum(stats, axis = 1))

#Reorganizando arrays
#before = np.array([[1,2,3,4],[5,6,7,8]])
#print(before)
#after = before.reshape((4,2))
#after = before.reshape((8,1))
#after = before.reshape((2,2,2))
#print(after)

#Vertical stacking vectors
#v1 = np.array([1,2,3,4])
#v2 = np.array([5,6,7,8])
#v3 = np.vstack([v1,v2])
#v3 = np.vstack([v1,v1,v2,v2])
#print(v3)

 
#Horizontal stack

#h1 = np.ones((2,4))
#h2 = np.zeros((2,2))
#h3 = np.hstack((h1,h2))
#print(h3)

#Pegando data 

File = np.genfromtxt('Matplotlib & numpy/data.txt', delimiter = ',')
File = File.astype('int32')
#print(File)


##### Index Avançada
#print(File > 50)
#print(File[File>50])


###Voce pode usar uma lista de index no numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])
print(np.any(File>50, axis= 0))








#https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html ### CRIAÇÃO DE ARRAYS COM NUMPY
#https://docs.scipy.org/doc/numpy/reference/routines.math.html           ### FUNÇÕES MATEMÁTICAS COM NUMPY
#https://docs.scipy.org/doc/numpy/reference/routines.linalg.html         ### ALGEBRA LINEAR COM NUMPY