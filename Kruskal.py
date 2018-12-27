#Alberto Calvo Madurga

#Algoritmos y Computación 18/19, UVA

#Clase para representar un grafo
class Grafo:

    def __init__(self,nodos):
        self.V= nodos
        self.aris = []

        self.padre =[] #Padre de cada nodo
        self.rango =[]   #Rango de cada nodo

    #Inicializacion de los valores para los conjuntos
    def iniciarConjuntos(self):
        for nodo in range(self.V):
            self.padre.append(nodo)
            self.rango.append(0)

    # Funcion para meter una arista al grafo
    def incluirArista(self,u,v,w):
        self.aris.append([u,v,w])

    # Funcion para buscar el padre de un nodo
    def buscar(self, i):
        if self.padre[i] == i:
            return i
        #Aplica la tecnica de compresion de caminos
        self.padre[i]=self.buscar(self.padre[i])
        return self.padre[i]

    #Funcion que une dos conjuntos x e y
    def fusionar(self, x, y):
        padrex = self.buscar(x)
        padrey = self.buscar(y)

        # Union por rango
        if self.rango[padrex] < self.rango[padrey]:
            self.padre[padrex] = padrey
        elif self.rango[padrex] > self.rango[padrey]:
            self.padre[padrey] = padrex

        # Si los rangos son iguales, elegir uno cualquiera como padre
        else :
            self.padre[padrey] = padrex
            self.rango[padrex] += 1

# Funcion que devuelve el grafo con el Algoritmo de Kruskal
def Kruskal(g):

        # Creamos los "Disjoint-sets"
        g.iniciarConjuntos()
        #Creamos el array donde quedaran las aristas elegidas
        res =[]

        i = 0 #Indice para recorrer los diferentes caminos(ordenados por peso)
        n = 0 #Es el numero de nodos conectados por el momento

        #Ordenamos las aristas de menor peso a mayor
        #Mantiene el orden dentro del mismo peso (robusto)
        g.aris =  sorted(g.aris,key=getKey)

        #Hasta que no estan los N-1 nodos conectados seguimos
        while n < g.V -1 :
            #Como ya estan ordenados, seleccionamos cada vez el
            #camino de menor peso
            u,v,w =  g.aris[i]
            i = i + 1

            x = g.buscar(u)
            y = g.buscar(v)

            # Comprobacion de ciclo
            if x != y:
                #Aumentamos el numero de vertices conectados
                n = n + 1
                #Metemos la arista buena a la solucion
                res.append([u,v,w])
                g.fusionar(x, y)

        #Comprobacion de resultados
        print "Resultado"
        peso = 0
        for u,v,w  in res:
            print ("%d -- %d == w: %d" % (u,v,w))
            peso = peso +w
        print ("El MST tiene un peso de %d" %peso)

        #print "Rangos"
        #for j in range(g.V):
        #    print("Rango de %d es %d" % (j,g.rango[j]))

        return res

#Funcion que te selecciona el elemento deseado de una lista
def getKey(item):
    return item[2]

#Valores para ejemplo
g = Grafo(5)
g.incluirArista(0, 1, 9)
g.incluirArista(0, 2, 7)
g.incluirArista(0, 3, 2)
g.incluirArista(1, 2, 2)
g.incluirArista(2, 3, 2)
g.incluirArista(1, 3, 2)
g.incluirArista(1, 4, 3)
g.incluirArista(3, 4, 3)

Kruskal(g)
