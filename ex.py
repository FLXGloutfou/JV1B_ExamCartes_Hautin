

class Cartes :
    def __init__ (self,Mana,Nom,Description):
        self.__mana = Mana
        self.__nom = Nom
        self.__description = Description


class Mage :
    def __init__ (self,Nom,Vie,MTotal,MActu,Main):
        self.__nom = Nom
        self.__vie = Vie
        self.__MT = MTotal
        self.__MA = MActu
        self.__main = Main
        self.__defausse = 0
        self.__ZDJ = 0


    def recupmana(self):
       self.__MA += 20

    def getnom (self):
        return self.__nom
    
    def getvie (self):
        return self.__vie
    
    def getmt (self):
        return self.__MT
    
    def getmana(self):
        return self.__MA
    
    def getmain (self):
        return self.__main






class Cristal(Cartes):
    def __init__ (self,Valeur,Mana,Nom,Description):
        Cartes.__init__(self,Mana,Nom,Description)
        self.__valeur = Valeur

    def jouercarte(self):
       self.__MA = self.__MA - self.__mana 
    


class Creature(Cartes):
    def __init__ (self,PV,Patk,Mana,Nom,Description):
        Cartes.__init__(self,Mana,Nom,Description)
        self.__pv = PV
        self.__patk = Patk
    
    def jouercarte(self):
       self.__MA = self.__MA - self.__mana 



class Blast(Cartes):
    def __init__ (self,Valeur,Mana,Nom,Description):
        Cartes.__init__(self,Mana,Nom,Description)
        self.__valeur = Valeur

    



cristtal = Cristal(10,5,"cristal","Le cristal reste dans votre zone de jeux et augemente votre maximum de mana")
creatture = Creature (20,10,20,"kulberg","En voila une belle créature prête a se battre")
blastt = Blast (10,20,"BLast","BOULE DE FEUUUUUUUUUUUU !")

gloutfou = Mage("Gloutfou",100,50,50,[cristtal,creatture,blastt])
merling = Mage("Marling",100,50,50,[cristtal,creatture,blastt])


#end = False
#
#while end == False :
#    print ("tour 1")

    
print ("oui")