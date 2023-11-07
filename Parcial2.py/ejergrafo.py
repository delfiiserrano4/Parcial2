#!2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
#!algoritmos necesarios para resolver las siguientes tareas:
#!a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
#!cantidad de episodios en los que aparecieron juntos ambos personajes que se
#!relacionan;
#!b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#!c) determinar cuál es el número máximo de episodio que comparten dos personajes y quienes son; 
#!d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,  Boba Fett, Leia, Rey, 
#!Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;




from grafo import Grafo 
from grafo import Arista 
grafo =  Grafo(dirigido=False)
arista = Arista()


#!A
grafo.insertar_vertice('Luke Skywalker')
grafo.insertar_vertice('Darth Vader')
grafo.insertar_vertice('Yoda') 
grafo.insertar_vertice('Boba Fett')
grafo.insertar_vertice('C-3PO') 
grafo.insertar_vertice('Leila')
grafo.insertar_vertice('Rey')
grafo.insertar_vertice('Kylo Ren')
grafo.insertar_vertice('Chewbacca')
grafo.insertar_vertice('Han Solo')
grafo.insertar_vertice('R2-D2')
grafo.insertar_vertice('BB-8')


grafo.insertar_arista('Luke Skywalker', 'Darth Vader', 4)
grafo.insertar_arista('Luke Skywalker', 'Leia', 300)
grafo.insertar_arista('Darth Vader', 'R2-D2', 5)
grafo.insertar_arista('Darth Vader', 'BB-8', 453)
grafo.insertar_arista('Yoda', 'Han Solo', 12)
grafo.insertar_arista('Boba Fett', 'Leia', 42)
grafo.insertar_arista('Boba Fett', 'BB-8', 34)
grafo.insertar_arista('Leila', 'Han Solo', 442)
grafo.insertar_arista('Rey', 'Kylo Ren', 563)
grafo.insertar_arista('Kylo Ren', 'BB-8', 132)
grafo.insertar_arista('Kylo Ren', 'Leila', 442)
grafo.insertar_arista('Chewbacca', 'R2-D2', 45)
grafo.insertar_arista('Chewbacca', 'Yoda', 87)
grafo.insertar_arista('Han Solo', 'Darth Vader', 84)
grafo.insertar_arista('R2-D2', 'Boba Fett', 442)
grafo.insertar_arista('BB-8', 'Yoda', 354)



#!B
arbol = grafo.kruskal()
arbol = arbol[0]
peso_total = 0
if ('Yoda' in arbol)
  for nodo in arbol:
      nodo = nodo 
      peso_total += init(nodo[2])
      print(f'{nodo[0]}')
      print(f'Arbol de expansion minimo: {peso_total}')





#!C
grafo.personaje_compartio_episodios()


def personaje_compartio_episodios(self):
        personaje = {}
        aux = self.__inicio
        while aux is not None:
            if [aux.datos['peso']] not in personaje:
                if (aux.datos > aux.datos.sig):
                    print(aux.datos)
                aux = aux.sig
            return personaje
        
grafo.episodios()    
def episodios(self):
        episodios = {}
        aux = self.__inicio
        while aux is not episodios:
            if aux.datos['peso'] > 2:
                print(aux.datos)
            return episodios


print('El maximo de episodios compartidos son ', grafo.episodios())
print('Los personajes que mas episodios comnpratieron son ', grafo.personaje_compartio_episodio())