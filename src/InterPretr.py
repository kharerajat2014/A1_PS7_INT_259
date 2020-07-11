from graph import Graph

class InterPretr:
    # prompts File
    __promptsFile = 0
    __promptsText = 0
    vertices = []
    adjMatrix = Graph(6)
    
    
    # constructor 
    def __init__(self):
        print("Starting InterPretr")
        self.__promptsFile = open("../input/promptsPS7.txt", 'r') 
        self.__promptsText = self.__promptsFile.read()
       

    def run(self):
        self.readApplications("../input/inputPS7.txt")
        self.showAll()
        if 'showMinList' in self.__promptsText:
            self.displayHireList()

   
    def readApplications(self,inputFile):
        print("readApplications")
        # calling methods 
        self.adjMatrix.addEdge(0, 1); 
        self.adjMatrix.addEdge(0, 2); 
        self.adjMatrix.addEdge(1, 2); 
        self.adjMatrix.addEdge(2, 3); 
        # the adjacency matrix created 
        self.adjMatrix.displayAdjacencyMatrix(); 

    def showAll(self):
        print("--------Function showAll--------")
        
    def displayHireList(self):
        print("--------Function displayHireList--------")


    def displayCandidates(self, lang): 
        print("--------Function displayCandidates--------")
        


    def findDirectTranslator(self, langA, langB):
        print("--------Function findDirectTranslator--------")


    def findTransRelation(self, langA, langB):
        print("--------Function findTransRelation--------")


    def parsePrompts(self,inputPromptsFile):
        print("--------Function findTransRelation--------")





def main():
    interPretr = InterPretr()
    interPretr.run()
    

if __name__=="__main__":
    main()


    
        

