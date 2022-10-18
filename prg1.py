from prg2 import prg2()

obj= Person1("nilu","suru",1552)
class Person1:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob
nikhil=Person1("shubham","chat",1997)
print(nikhil._name)
print(nikhil._Person1__surname)
print(nikhil.yob)
