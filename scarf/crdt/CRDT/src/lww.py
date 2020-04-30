from datetime import datetime
import time
import logging
logger = logging.getLogger('CRDT Logger')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# add the handler to the root logger
logger.addHandler(console)

class LWWFunctions:
    @staticmethod
    def update(payload, elem):
        payload.append({'elem': elem, 'timestamp': datetime.now()})
        payload.sort(key=lambda i: i['timestamp'])
        return payload

    @staticmethod
    def compare(payload1, payload2):
        item = False

        for item_1 in payload1:
            for item_2 in payload2:
                if item_2['elem'] == item_1['elem']:
                    item = True
                    break
            if item:
                break
        return item

    @staticmethod
    def merge(payload1, payload2):
        for item in payload2:
            if item not in payload1:
                payload1.append(item)
        payload1.sort(key=lambda i: i['timestamp'])
        return payload1

    @staticmethod
    def display(name, payload):
        print("{}: ".format(name), end="")
        for item in payload:
            print("{}:{}".format(item["elem"], item["timestamp"].microsecond), end=", ")
        print()


class LWWElementSet():
    def __init__(self):
        self.A = []
        self.R = []
        self.lwwf = LWWFunctions()

    def add(self, elem):
        self.A = self.lwwf.update(self.A, elem)

    def remove(self, elem):
        self.R = self.lwwf.update(self.R, elem)

    def query(self, elem):
        elem_in_a = [item for item in self.A if item['elem'] == elem]
        if len(elem_in_a) != 0:
            elem_in_r = [item for item in self.R if item['elem'] == elem]
            if len(elem_in_r) == 0 or elem_in_r[-1]["timestamp"] < elem_in_a[-1]["timestamp"]:
                return True
        return False

    def compare(self, lww):
        return self.lwwf.compare(self.A, lww.A) and self.lwwf.compare(self.R, lww.R)

    def merge(self, lww):
        self.A = self.lwwf.merge(self.A, lww.A)
        self.R = self.lwwf.merge(self.R, lww.R)

    def display(self):
        self.lwwf.display('A', self.A)
        self.lwwf.display('R', self.R)
    
    def toDict(self):
        return self.__dict__
    
    def loadFromDict(dict_input):
        lwwElementSet = LWWElementSet()
        lwwElementSet.__dict__ = dict_input
        return lwwElementSet

class LWW():
    def __init__(self):
        self.value = None
        self.timestamp = time.time()

    def add(self, elem):
        current_time = time.time()
        if(current_time > self.timestamp):
            self.value = elem
            self.time = current_time

    def query(self):
        return self.value

    def merge(self, lww):
        if(self.timestamp < lww.timestamp):
            self.value = lww.value
            self.timestamp = lww.timestamp

    def display(self):
        print(self.value, self.timestamp)
    
    def toDict(self):
        return self.__dict__
    
    def loadFromDict(dict_input):
        lwwElement = LWW()
        lwwElement.__dict__ = dict_input
        return lwwElement

if __name__ == "__main__":
    logging.basicConfig(filename='logs.log', 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
    logger.setLevel(level=logging.DEBUG)

    a = LWW()
    a.add(5)
    a.add(4)
    b = LWW()
    b.add(6)
    a.merge(b)
    # print(a.query())
    logger.debug(f'a  value :  {a.query()}')   
    c = LWW()
    c.add("Hemant")
    d = LWW()
    d.add("GVV")
    c.merge(d)
    # print(c.query())
    logger.debug(f'c value : {c.query()}')
    