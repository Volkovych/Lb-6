import pandas as pd
import collections
class Translator():
    def method(self, x:str ,y:float,c:float):
        self.x=x
        self.y=y
        self.c=c
        print(self.x, self.y, self.c)
    def method2(self, x:str ,y:float,c:float):
        self.x=x
        self.y=y
        self.c=c
        print(self.x, self.y)
t=Translator()
print("Варианты перевода:")
t.method("lucky", "счастливый", "lucky")
print("Перевод слова")
t.method2("beautiful", "красивый","видный")
