class InterPretr:
    # prompts File
    __promptsFile = 0
    
    # constructor 
    def __init__(self):
        print("Starting InterPretr")
        self.__promptsFile = open("../input/promptsPS7.txt", 'r') 



    def run(self):
        self.readApplications("../input/inputPS7.txt")
        self.showAll()
        self.displayHireList()

   
    def readApplications(self,inputFile):
        print("readApplications")

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


    
        

