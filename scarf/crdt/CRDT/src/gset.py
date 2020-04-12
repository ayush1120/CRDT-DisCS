class GSet:
    def __init__(self):
        self.payload = []

    def add(self, elem):
        self.payload.append(elem)
        self.payload.sort()

    def query(self, elem):
        return elem in self.payload

    def compare(self, gs2):
        for elem in self.payload:
            if elem not in gs2.payload:
                return False
        return True

    def merge(self, gs2):
        for elem in gs2.payload:
            if elem not in self.payload:
                self.payload.append(elem)
        self.payload.sort()

    def display(self):
        print(self.payload)

    def toDict(self):
        return self.__dict__
    
    def loadFromDict(dict_input):
        gset = GSet()
        gset.__dict__ = dict_input
        return gset