from collections import defaultdict

# graph = defaultdict(list)
# def addEdge(graph, u, v):

# class interpreter:
#     vertices = []
#     edges = [[],[]]

#     def readApplications(self, inputfile):

#         interpreters = list()
#         with open(inputfile, "r") as reader:
#             for line in reader:
#                 interpreters.append(line)

#         return interpreters

#     def showAll(self):
#         return


# interpreters = interpreter()


# print(type(interpreters.readApplications("C:\\Users\\ssinghal1\\Desktop\\dsad\\inputPS7.txt")[6]))
# print(interpreters.readApplications("C:\\Users\\ssinghal1\\Desktop\\dsad\\inputPS7.txt"))

        # file1 = open(inputfile, 'r')
        # Lines = file1.readlines()
        
        # for line in Lines:
        #     vertices.append(line)
            
        # for x in range(len(vertices)):
        #     print(vertices[x])
    
#gobj = interpreter()
#gobj.readApplications("inputPS7.txt")

#**********************************************************************************

# vertices = []
# file1 = open("C:\\Users\\ssinghal1\\Desktop\\dsad\\inputPS7.txt", 'r')
# Lines = file1.readlines()
# for line in Lines:
#     vertices.append(line.split("/"))
    
# for x in range(len(vertices)):
#     print(vertices[x])

#**********************************************************************************


# Adjacency Matrix representation in Python


# class Graph(object):
#     vertices = []
#     edges = [[],[]]
#     # Initialize the matrix
#     def __init__(self, size):
#         self.adjMatrix = []
#         for i in range(size):
#             self.adjMatrix.append([0 for i in range(size)])
#         self.size = size

#     # Add edges
#     def add_edge(self, v1, v2):
#         if v1 == v2:
#             print("Same vertex %d and %d" % (v1, v2))
#         self.adjMatrix[v1][v2] = 1
#         self.adjMatrix[v2][v1] = 1

#     # Remove edges
#     def remove_edge(self, v1, v2):
#         if self.adjMatrix[v1][v2] == 0:
#             print("No edge between %d and %d" % (v1, v2))
#             return
#         self.adjMatrix[v1][v2] = 0
#         self.adjMatrix[v2][v1] = 0

#     def __len__(self):
#         return self.size

#     # Print the matrix
#     def print_matrix(self):
#         for row in self.adjMatrix:
#             for val in row:
#                 print('{:4}'.format(val)),
#             print


# def main():
#     g = Graph(5)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)

#     g.print_matrix()


# if __name__ == '__main__':
#     main()


#*********************************************************************************************

class Vertice():
    def __init__(self, name, type, index):
        self.name = name
        self.type = type
        self.index = index
        self.knownlang = list();
    
    def __hash__(self):
        return self.__hash__()

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

myVertices = []
myEdges = [[0 for x in range(5)] for x in range(5)]
uniq_interpreter = 0
uniq_lang = 0
interpreter_index = 0
lang_index = 0

file1 = open("../input/inputPS7.txt", 'r')
Lines = file1.readlines()
for line in Lines:
    content = line.rstrip().split("/")
    for y in range(len(content)):
        if(y == 0):
            uniq_interpreter += 1
            myVertices.append(Vertice(content[y].strip(), "interpreter", interpreter_index))
            interpreter_index = interpreter_index + 1
        else:
            obj = Vertice(content[y].strip(), "language", lang_index)
            if obj not in myVertices:
                uniq_lang += 1
                myVertices.append(Vertice(content[y].strip(), "language", lang_index))
                lang_index = lang_index + 1

#printing all unique interpreter and languages
print("*********Printing All*************")
for x in range(len(myVertices)):
    print(myVertices[x].name+ "-" +myVertices[x].type)

#printing unique intepreter
print("*********Unique interpreter*************")
for x in range(len(myVertices)):
    if(myVertices[x].type == "interpreter"):
        #uniq_interpreter += 1;
        print(myVertices[x].name)

#printing unique languages
print("*********Unique languges*************")
for x in range(len(myVertices)):
    if(myVertices[x].type == "language"):
        print(myVertices[x].name)


#populating adjancy matrices
#now we know the dimension of adjancy martrix its uniq_interpreter * uniq_lang
#initializing myEdges

#myEdges = 

#we have to create mapping for unique language and index of adjacency matrix
#now we have index 



#         English HIndi Punjabi Kannada
# Manasa    1       1      1      0
# Venkat
# Paul
# def showAll(self):
# def displayHireList(self)
# def displayCandidates(self, lang):
# # def findDirectTranslator(self, langA, langB):
# def findTransRelation(self, langA, langB):


