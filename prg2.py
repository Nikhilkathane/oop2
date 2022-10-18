import prg1
print(prg1)
obj2=prg1.Person1("nilu","suru",1552)
print(obj2.yob)
   class Person:
        _name = "niks"
        __surname = "kayhu"
        yob = 1899
obj=Person()
print(obj)

   class emp(Person):
   pass
obj1 = emp()
print(obj1._name)
print(obj1._Person__surname)

