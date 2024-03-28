class student:
    def __init__(self,name) -> None:
        self.__name = name
    def getname(self):
        return self.__name
obj = student("archana")
print(f"name : {obj.getname()}")
        