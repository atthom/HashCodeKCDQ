import math
import numpy

import networkx as nx
import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
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


class Pizza:
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

    def isValidSlice(self, shape, coordinate):
        nb_tomato = 0
        for i in range(coordinate.x, coordinate.x + shape.longeur):
            if matrix[i][coordinate.y] == 'T':
                nb_tomato += 1

        nb_mush = shape.size() - nb_tomato

        if nb_mush > self.min_ingredient and nb_tomato > self.min_ingredient:
            return True
        else:
            return False


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

for i in range(1, max_size + 1):
    for j in range(1, max_size + 1):
        current_shape = Shape(i, j)
        if current_shape.isValidShape(min_size, max_size):
            all_shape.append(current_shape)

print("\nShapes acceptables :")
for shape in all_shape:
    print(shape)

print("sandbox pour trouver un sous graph complet")
G = nx.DiGraph()

G.add_edge('1', '2', weight=4)
G.add_edge('1', '4', weight=4)
G.add_edge('1', '7', weight=4)
G.add_edge('1', '9', weight=4)

G.add_edge('2', '6', weight=7)
G.add_edge('2', '3', weight=7)
G.add_edge('2', '1', weight=7)
G.add_edge('2', '10', weight=7)

G.add_edge('3', '5', weight=8)
G.add_edge('3', '8', weight=8)
G.add_edge('3', '6', weight=8)
G.add_edge('3', '2', weight=8)
G.add_edge('3', '10', weight=8)

G.add_edge('4', '1', weight=6)
G.add_edge('4', '7', weight=6)
G.add_edge('4', '5', weight=6)

G.add_edge('5', '8', weight=30)
G.add_edge('5', '3', weight=30)
G.add_edge('5', '4', weight=30)

G.add_edge('6', '8', weight=2)
G.add_edge('6', '3', weight=2)
G.add_edge('6', '2', weight=2)
G.add_edge('6', '10', weight=2)

G.add_edge('7', '4', weight=4)
G.add_edge('7', '1', weight=4)

G.add_edge('8', '6', weight=2)
G.add_edge('8', '3', weight=2)
G.add_edge('8', '5', weight=2)
G.add_edge('8', '10', weight=2)

G.add_edge('9', '1', weight=5)

G.add_edge('10', '2', weight=2)
G.add_edge('10', '6', weight=2)
G.add_edge('10', '3', weight=2)
G.add_edge('10', '8', weight=2)

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


#clique = nx.find_cliques(G)