import json
import os


class FileHistory():
    def __init__(self):
        self.__path = os.path.join('data', 'file.json')
        if os.path.exists(self.__path):
            __f = open(self.__path, 'r')
            self.__file = json.load(__f)
            __f.close()
        else:
            __f = open(self.__path, 'w')
            json.dump([], __f, indent=6)
            __f.close()
            __f = open(self.__path, 'r')
            self.__file = json.load(__f)
            __f.close()

    def addfile(self, name, id, md5, typ='video'):
        element = {'id': id, 
                    'name': name,
                    'hash': md5,
                    'type':typ}
        self.__file.append(element)
        f = open(self.__path, 'w')
        json.dump(self.__file, f, indent=6)
        f.close()

    def getfile(self):
        return self.__file

    def clearHistory(self):
        self.__file = []
        f = open(self.__path, 'w')
        json.dump(self.__file, f)
        f.close()
