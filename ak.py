class Ak47:
    #def __init__(self):
     def __init__(self, n_strings=6):   
         #self.n_strings = 6
         self.n_strings = n_strings
         self.play()
         self.__cost = 5000 
    def play(self):
        print("TA TA TA") 

class Ak74(Ak47):
      pass

class Kalashnikov(Ak47):
    def __init__(self):
       super().__init__(n_strings = 8):
       #self.n_strings = 8
       self.colour = ("#000000", "#FFFFFF")
       #self.__cost = 5000
    #pass
   def shootLouder(self):
       print("ta ta ta".upper())
   def __secret(self):
       print("Ak47 Price", self._Ak47__cost,)  

#my_machinegun = Ak47()
#print(my_machinegun.n_strings)
#my_machinegun.play()

#my_machinegun = Kalashnikov()
#print(my_machinegun.n_strings)
#my_machinegun.shootLouder()
#print("child class:", my_machinegun.n_strings)
#print("parent class:", Ak47().n_strings)

my_machinegun = Kalashnikov()
my_machinegun =._Kalashnikov__secret()
print(Ak74(4).n_strings)