from gset import GSet

class TwoPSet:

    def __init__(self):
        self.A = GSet()
        self.R = GSet()

    def add(self, elem):
        self.A.add(elem)

    def remove(self, elem):
        self.R.add(elem)

    def query(self, elem):
        return self.A.query(elem) and not self.R.query(elem)

    def compare(self, tps2):
        return self.A.compare(tps2.A) and self.R.compare(tps2.R)

    def merge(self, tps2):
        self.A.merge(tps2.A)
        self.R.merge(tps2.R)
        # self.display()

    def display(self):
        print("A: ", end="")
        self.A.display()
        print("R: ", end="")
        self.R.display()

    def writeToFile(self,fileAdd,fileRemove):
        self.A.writeToFile(fileAdd)
        self.R.writeToFile(fileRemove)