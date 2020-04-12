class ORSetFunctions:
    @staticmethod
    def add(payload, elem, unique_tag):
        found = False
        for item in payload:
            if elem == item["elem"]:
                item["tags"].append(unique_tag)
                found = True
                break
        if not found:
            payload.append({"elem": elem, "tags": [unique_tag]})
        payload.sort(key=lambda i: i['elem'])
        return payload

    @staticmethod
    def remove(payloadA, payloadR, elem):
        elem_tags = []
        if len(payloadA):
            for item in payloadA:
                if elem == item["elem"]:
                    elem_tags += item["tags"]
                    break
        else:
            return

        found = False
        for item in payloadR:
            if elem == item["elem"]:
                item["tags"] = item["tags"] + list(set(elem_tags) - set(item["tags"]))
                found = True
                break
        if not found:
            payloadR.append({"elem": elem, "tags": elem_tags})

        payloadR.sort(key=lambda i: i['elem'])
        return payloadR

    @staticmethod
    def compare(payload1, payload2):
        if len(payload1):
            for item1 in payload1:
                for item2 in payload2:
                    if item1 != item2:
                        return False
        else:
            # print("No elements added")
            return False
        return True

    @staticmethod
    def merge(payload1, payload2):
        for item2 in payload2:
            found = False
            for item1 in payload1:
                if item1['elem'] == item2['elem']:
                    item1["tags"] = item1["tags"] + list(set(item2["tags"]) - set(item1["tags"]))
                    found = True
                    break
            if not found:
                payload1.append({"elem": item2["elem"], "tags": item2["tags"]})
        payload1.sort(key=lambda i: i['elem'])
        return payload1

    @staticmethod
    def display(name, payload):
        print("{}: ".format(name))
        if len(payload):
            for item in payload:
                print("{}:{}".format(item["elem"], item["tags"]))
                pass
        else:
            # print("No elements to show")
            return -1

    @staticmethod
    def query(elem, payload):
        if len(payload):
            for item in payload:
                if elem == item["elem"]:
                    return item["tags"]
            return []
        else:
            # print("No elements to query")
            return []


class ORSet():
    def __init__(self):
        self.A = []
        self.R = []
        self.orsetf = ORSetFunctions()

    def add(self, elem, unique_tag):
        self.A = self.orsetf.add(self.A, elem, unique_tag)

    def remove(self, elem):
        self.R = self.orsetf.remove(self.        self.id = id
    def display(self):
        self.orsetf.display('A', self.A)
        self.orsetf.display('R', self.R)


    def toDict(self):
        return self.__dict__
    
    def loadFromDict(dict_input):
        orset = ORSet()
        orset.__dict__ = dict_input
        return orset