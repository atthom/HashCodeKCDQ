import networkx

from docutils.parsers.rst.directives.html import meta


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def size(self):
        return self.longeur*self.largeur


class Pizza:
    def __init__(self, matrix, min, max):
        self.matrix = matrix
        self.min_ingredient = min
        self.max_shape_size = max

    def isValidShape(self, shape, coordinate):
        nb_tomato = 0
        for i in range(coordinate.x, coordinate.x + shape.longeur):
            if matrix[i][coordinate.y] == 'T':
                nb_tomato += 1

        nb_mush = shape.size() - nb_tomato

        if nb_mush> self.min_ingredient and nb_tomato>self.min_ingredient:
            return True
        else:
            return False


f = open("input_files/small.in", "r")

#str = f.read()
matrix = []
for line in f.readlines():
    #print(line)
    matrix.append(line[:-1])
    #for char in line:
        #print(char)
        #matrix.append()


meta_list = matrix[0].split(' ')
del matrix[0]
print(matrix)
print(meta_list)

L = len(matrix)
l = len(matrix[0])
matrix_zero = [L * [_] for _ in range(l)]

print(matrix_zero)

pizza = Pizza(matrix, meta_list[2], meta[3])


#min_long = meta_list[2]
#max_long =

