import math
import numpy
import operator
import networkx as nx
import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    ### classe qui encapsule les fonctions utiles pour les shapes
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def isValidShape(self, min, max):
        if self.size() < min:
            return False
        if self.size() > max:
            return False
        return True

    def size(self):
        return self.longeur * self.largeur

    def __str__(self):
        return "{ longeur:" + str(self.longeur) + "," + " largeur: " + str(self.largeur) + "}"



class Slice:
    ### classe qui encapsule les fonctions utiles pour les shapes
    def __init__(self, coordinate, shape):
        self.coordinate = coordinate
        self.shape = shape


class Pizza:
    ### initialise la pizza
    def __init__(self, matrix, list):
        self.matrix = matrix
        self.min_ingredient = int(list[2])
        self.max_shape_size = int(list[3])
        self.long = int(list[1])
        self.width = int(list[0])
        L = len(matrix)
        l = len(matrix[0])
        self.matrix_tomato = [l * [0] for _ in range(L)]  # numpy.zeros((L, l))
        self.generate_array_tomato()

    ### genere un tableau pour connaitre le nombre de tomate à une position,
    ### sans avoir besoin de tout recalculer à chaque fois
    def generate_array_tomato(self):
        for k in range(0, self.width):
            nb_tomato = 0
            for l in range(0, self.long):
                if matrix[k][l] == 'T':
                    nb_tomato += 1

                self.matrix_tomato[k][l] = nb_tomato + self.matrix_tomato[k - 1][l]

        print("\nNb tomato :")
        print(self.matrix_tomato)

    def getNbTomatoByCoordinate(self, coord):
        return self.matrix_tomato[coord.x][coord.y]

    ### A refactor : permet de vérifier si la slice est valide en connaissant la shape et la position de départ
    def isValidSlice(self, shape, coordinate):
        ###
        shape.size()


f = open("input_files/small.in", "r")

matrix = []
for line in f.readlines():
    matrix.append(line[:-1])

meta_list = matrix[0].split(' ')
del matrix[0]
print("\nPizzaaa :")
print(matrix)

print("\nMeta data :")
print(meta_list)

pizza = Pizza(matrix, meta_list)

min_long = math.floor(math.sqrt(float(meta_list[3])))

all_shape = []

min_size = int(meta_list[2]) * 2
max_size = int(meta_list[3])

### Générations des différentes shapes utilisés

for i in range(1, max_size + 1):
    for j in range(1, max_size + 1):
        current_shape = Shape(i, j)
        if current_shape.isValidShape(min_size, max_size):
            all_shape.append(current_shape)

print("\nShapes acceptables :")
for shape in all_shape:
    print(shape)

print("sandbox pour trouver un sous graph complet")

### On ne peux pas utiliser un graph orienté si on veux utiliser la recherche de la library
### Du coup j'ai laisser qu'un arc sur les deux et j'ai additionné le poids des deux slices

G = nx.Graph()

G.add_edge('1', '2', weight=4+7)
G.add_edge('1', '4', weight=4+6)
G.add_edge('1', '7', weight=4+4)
G.add_edge('1', '9', weight=4+5)

G.add_edge('2', '6', weight=7+2)
G.add_edge('2', '3', weight=7+8)
#G.add_edge('2', '1', weight=7)
G.add_edge('2', '10', weight=7+2)
G.add_edge('2', '8', weight=7+2)

G.add_edge('3', '5', weight=8+30)
G.add_edge('3', '8', weight=8+2)
G.add_edge('3', '6', weight=8+2)
#G.add_edge('3', '2', weight=8)
G.add_edge('3', '10', weight=8+2)

#G.add_edge('4', '1', weight=6)
G.add_edge('4', '7', weight=6+4)
G.add_edge('4', '5', weight=6+30)

G.add_edge('5', '8', weight=30+2)
#G.add_edge('5', '3', weight=30)
#G.add_edge('5', '4', weight=30)

G.add_edge('6', '8', weight=2+2)
#G.add_edge('6', '3', weight=2)
#G.add_edge('6', '2', weight=2)
G.add_edge('6', '10', weight=2+2)

#G.add_edge('7', '4', weight=4)
#G.add_edge('7', '1', weight=4)

#G.add_edge('8', '6', weight=2)
#G.add_edge('8', '3', weight=2)
#G.add_edge('8', '5', weight=2)
G.add_edge('8', '10', weight=2+2)

#G.add_edge('9', '1', weight=5)

#G.add_edge('10', '2', weight=2)
#G.add_edge('10', '6', weight=2)
#G.add_edge('10', '3', weight=2)
#G.add_edge('10', '8', weight=2)


### Bricolage pour afficher le graph, #yolo #swag

pos = nx.spring_layout(G)  # positions for all nodes
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True),  width=6)
# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("weighted_graph.png")  # save as png
#plt.show()

graph = nx.make_max_clique_graph(G)
pos = nx.spring_layout(graph)  # positions for all nodes
    # # nodes
nx.draw_networkx_nodes(graph, pos, node_size=700)
# edges
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(data=True), width=6)
    # # labels
nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("weighted_graph222.png")

#clique = list(nx.enumerate_all_cliques(G))

print("calcul des cliques")
clique = list(nx.algorithms.find_cliques(G))
min_size = 0
max_size = 0

cc = nx.algorithms.node_clique_number(G, cliques=clique)
print("tableau associatif (noeud => longeur de la plus grande clique qui contient le noeud)")
print(cc)

nodemax = max(cc, key=cc.get)
size_max = cc[nodemax]

pruned_list = []
for graph in clique:
    ### affiche une liste de slice qui correspond a une configuration possible
    ### il suffit de calculer l'air couvert par chaqu'une des liste, prendre le maximum et c'est bon :)
    if len(graph)*5 > size_max*2:
        pruned_list.append(graph)

print("after pruning :")

for graph in pruned_list:
    print(graph)


### Methode Ismael : [[1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0]]
# [[1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 3, 4, 5], [2, 3, 3, 4, 7, 8, 10], [3, 4, 4, 6, 9, 10, 12], [4, 6, 7, 10, 14, 16, 18], [5, 8, 10, 14, 19, 22, 24]]
# Methode Thomas :  [[1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 3, 4, 5], [2, 3, 3, 4, 7, 8, 10], [3, 4, 4, 6, 9, 10, 12], [4, 6, 7, 10, 14, 16, 18], [5, 8, 10, 14, 19, 22, 24]]

