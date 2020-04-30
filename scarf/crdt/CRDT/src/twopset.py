import sys
sys.path.append('../../../')

from crdt.CRDT.src.gset import GSet


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


    def addedValues(self):
        addedValues = []
        for elem in self.A.payload:
            if self.A.payload.count(elem) > self.R.payload.count(elem):
                if elem not in addedValues:
                    addedValues.append(elem)
        return addedValues

    def removedValues(self):
        removedValues = []
        for elem in self.R.payload:
            if self.R.payload.count(elem) > self.A.payload.count(elem):
                if elem not in removedValues:
                    removedValues.append(elem)
        return removedValues


    def toDict(self):
        self.A = self.A.toDict()
        self.R = self.R.toDict()
        # print(self.__dict__)
        return self.__dict__
    
    def loadFromDict(self, dict_input):
        A = GSet()
        R = GSet()
        self.A =  A.loadFromDict(dict_input['A'])
        self.R =  R.loadFromDict(dict_input['R'])
        return self



if __name__ == "__main__":
    a = TwoPSet()
    a.add(2)
    a.add(3)
    a.add(4)
    a.remove(3)
    a.add(4)
    a.add(3)
    a.remove(3)
    a.add(3)
    a.remove(3)
    a.remove(3)
    # a.remove(4)
    # a.add(4)
    print('Added Values : ', a.addedValues())
    print('Removed Valiues : ', a.removedValues())


    b = a.toDict()
    # c = TwoPSet.loadFromDict(b) # This will not work
    c = TwoPSet().loadFromDict(b) # This will work
    
    # print(' Dict TwoPSet     :  ', b)
    # print(' Loaded from Dict :  ', c)