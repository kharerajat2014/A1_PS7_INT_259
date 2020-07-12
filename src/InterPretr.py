from sys import maxsize 
import sys
from graph import Graph
from graph import Vertice
INT_MAX = maxsize 

class InterPretr:
    adjMatrix = Graph(1)
    # prompts File
    __promptsFile = 0
    __promptsText = 0
    __inputFile   = 0
    __inputFileText = 0
    __outputFile = 0
    
    
    # constructor 
    def __init__(self):
        self.__promptsFile = open("../input/promptsPS7.txt", 'r') 
        self.__promptsText = self.__promptsFile.read()
        
        # Initialize outputPS7.txt to get the output of all results
        #original_stdout = sys.stdout  # Save a reference to the original standard output
        self.__outputFile =  open('../output/outputPS7.txt', 'w')
        # Change the standard output to the file we created.
        sys.stdout = self.__outputFile
       

    def run(self):
        self.readApplications("../input/inputPS7.txt")
        self.showAll()
        if 'showMinList' in self.__promptsText:
            self.displayHireList()

   
    def readApplications(self,inputFile):
        self.__inputFile = open(inputFile, 'r')
        self.__inputFileText = self.__inputFile.readlines()
        current_interpreter_index = 0
        current_language_index = 0
        for line in self.__inputFileText:
            content = line.rstrip().split("/")
            for y in range(len(content)):
                if(y == 0):
                    self.adjMatrix.addVertex(Vertice(content[y].strip(), "interpreter"))
                    current_interpreter_index = self.adjMatrix.getVerticesSize() - 1
                else:
                    obj = Vertice(content[y].strip(), "language")
                    if obj not in self.adjMatrix.getVertices():
                        self.adjMatrix.addVertex(Vertice(content[y].strip(), "language"))
                        current_language_index = self.adjMatrix.getVerticesSize() - 1
                        self.adjMatrix.addEdge(current_interpreter_index, current_language_index)
                    else:
                        #get the index of language and add edge
                        dup_index = self.adjMatrix.getVertices().index(obj)
                        self.adjMatrix.addEdge(current_interpreter_index, dup_index)

        for v1 in self.adjMatrix.getVertices():
            print(v1.getName()+"-"+v1.getType())
            print(v1.getCount())


        # calling methods 
        #self.adjMatrix.addEdge(0, 1); 
        #self.adjMatrix.addEdge(0, 2); 
        #self.adjMatrix.addEdge(1, 2); 
        #self.adjMatrix.addEdge(2, 3); 
        # the adjacency matrix created 
        self.adjMatrix.displayAdjacencyMatrix(); 
       

    def showAll(self):
        print("--------Function showAll--------")
        print(self.adjMatrix.showAll())

        
    def displayHireList(self):
        print("--------Function displayHireList--------")
        g = self.adjMatrix.getGraph()
        print(self.adjMatrix.getVerticesSize())
        self.__getMinimumCandidates(g, self.adjMatrix.getVerticesSize())
        # print the candidates and their languages.
        


    def displayCandidates(self, lang): 
        print("--------Function displayCandidates--------")
        


    def findDirectTranslator(self, langA, langB):
        print("--------Function findDirectTranslator--------")


    def findTransRelation(self, langA, langB):
        print("--------Function findTransRelation--------")


    def parsePrompts(self,inputPromptsFile):
        print("--------Function findTransRelation--------")


################## Private methods  ##########################
    
    # extract a minimum spanning tree from the adjacency matrix  
    # and get the edges of the minimum spanning tree. Picking the 
    # candidates from the edges will give is the minimum set of hires to 
    # cover all languages. 
    # 1. Here M is the adjacency Matrix 
    # 2. V is the number of vertices
    def __getMinimumCandidates(self, M,V): 
        inMST = [False] * V 
        minCandidates = []
        vertices = self.adjMatrix.getVertices()
    
        # Include first vertex in MST 
        inMST[0] = True
    
        # Keep adding edges while number of included  
        # edges does not become V-1. 
        edge_count = 0
        mincost = 0
        while edge_count < V - 1: 
    
            # Find minimum weight valid edge. 
            minn = INT_MAX 
            a = -1
            b = -1
            for i in range(V): 
                for j in range(V): 
                    if M[i][j] < minn: 
                        if self.__isValidEdge(i, j, inMST): 
                            minn = M[i][j] 
                            a = i 
                            b = j 
    
            if a != -1 and b != -1: 
                print("Edge %d: (%d, %d) minn: %d" % 
                    (edge_count, a, b, minn)) 
                #On either of the vertex in the edge a,b if its an interpreter keep it in minCandidates list
                #if(vertices[a].getType() == "interpreter"):
                #    if(!(vertices[a] in minCandidates)):
                #        minCandidates.append(vertices[a])
                if vertices[a].getType() == "interpreter":
                    if vertices[a] not in minCandidates:
                        name = vertices[a].getName()
                        print(name)
                        minCandidates.append(vertices[a])
                
                if vertices[b].getType() == "interpreter":
                    if vertices[b] not in minCandidates:
                        name = vertices[b].getName()
                        print (name)
                        minCandidates.append(vertices[b])
                        

                edge_count += 1
                mincost += minn 
                inMST[b] = inMST[a] = True
                # Check from the vertex on a,b and if any of them is a person store it in minCandidates
  
        
        return minCandidates
        #print("Minimum cost = %d" % mincost)    
    
    
    # Returns true if edge u-v is a valid edge to be  
    # include in MST. An edge is valid if one end is  
    # already included in MST and other is not in MST. 
    def __isValidEdge(self,u, v, inMST): 
        if u == v: 
            return False
        if inMST[u] == False and inMST[v] == False: 
            return False
        elif inMST[u] == True and inMST[v] == True: 
            return False
        return True


def main():
    interPretr = InterPretr()
    interPretr.run()
    

if __name__=="__main__":
    main()


    
        

