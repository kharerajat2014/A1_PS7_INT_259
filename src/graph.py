# Python program to add and remove Vertex in Adjacency Matrix 
class Vertice():
    __name = 0
    __type = 0
    __count = 0

    def __init__(self, name, type):
        self.__name = name
        self.__type = type
    
    def __hash__(self):
        return self.__hash__()

    def __eq__(self, other):
        return self.__name == other.__name and self.__type == other.__type

    def getName(self):
        return self.__name
    
    def getType(self):
        return self.__type
    
    def getCount(self):
        return self.__count

class Graph: 
    __n = 0
    __vertices = []

    # adjacency matrix 
    __g =[[0 for x in range(25)] for y in range(25)] 
        
    def getGraph(self):
        return self.__g
    
    # constructor 
    def __init__(self, x): 
        self.__n = x 

        # initializing each element of the adjacency matrix to zero 
        for i in range(0, self.__n): 
            for j in range(0, self.__n): 
                self.__g[i][j]= 0

    def displayAdjacencyMatrix(self): 
        print("\n\n Adjacency Matrix:", end ="") 
        
        # displaying the 2D array 
        for i in range(0, self.__n): 
            print() 
            for j in range(0, self.__n): 
                print("", self.__g[i][j], end ="") 
    def addEdge(self, x, y): 

        # checks if the vertex exists in the graph 
        if(x>= self.__n) or (y >= self.__n): 
            print("Vertex does not exists !") 
        
        # checks if the vertex is connecting to itself 
        if(x == y): 
            print("Same Vertex !") 
        else: 
                
            # connecting the vertices 
            self.__g[y][x]= 1
            self.__g[x][y]= 1    

    def addVertex(self, vertice): 
        #print("Value of n -")
        #print(self.__n)
        # increasing the number of vertices 
        self.__n = self.__n + 1 
        
        self.__vertices.append(vertice)
        # initializing the new elements to 0 
        for i in range(0, self.__n):
            #print(self.__n) 
            self.__g[i][self.__n-1]= 0
            self.__g[self.__n-1][i]= 0  

    def getVerticesSize(self):
        return len(self.__vertices)

    def getVertices(self):
        return self.__vertices

    def showAll(self):
        #uniqint = [v for v in self.__vertices if v.getType() == "intepreter"]
        #print(uniqint)
        uniqI = []
        uniqL = []


        for v1 in self.__vertices:
            if(v1.getType() == "interpreter"):
                uniqI.append(v1.getName())
            elif(v1.getType() == "language"):
                uniqL.append(v1.getName())

        print("Total no. of candidates: "+str(len(uniqI)))
        print("Total no. of languages: "+str(len(uniqL)))

        print("List of candidates:")
        print(uniqI)

        print("List of languages:")
        print(uniqL)



    def removeVertex(self, x): 
        
        # checking if the vertex is present 
        if(x>self.__n): 
            print("Vertex not present !") 
        else: 
        
            # removing the vertex 
            while(x<self.__n): 
        
                # shifting the rows to left side 
                for i in range(0, self.__n): 
                    self.__g[i][x]= self.__g[i][x + 1] 
            
                # shifting the columns upwards 
                for i in range(0, self.__n): 
                    self.__g[x][i]= self.__g[x + 1][i] 
                x = x + 1

            # decreasing the number of vertices 
            self.__n = self.__n - 1            


# # creating objects of class Graph 
# obj = Graph(4); 
    
# # calling methods 
# obj.addEdge(0, 1); 
# obj.addEdge(0, 2); 
# obj.addEdge(1, 2); 
# obj.addEdge(2, 3); 
#obj.addEdge(5, 3); 
# # the adjacency matrix created 
# obj.displayAdjacencyMatrix(); 

# # adding a vertex to the graph 
# obj.addVertex(); 
# # connecting that verex to other existing vertices 
# obj.addEdge(4, 1); 
# obj.addEdge(4, 3); 
# # the adjacency matrix with a new vertex 
# obj.displayAdjacencyMatrix(); 
    
# # removing an existing vertex in the graph 
# obj.removeVertex(1); 
# # the adjacency matrix after removing a vertex 
# obj.displayAdjacencyMatrix(); 
