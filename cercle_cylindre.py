class Cercle :
    def __init__ (self,rayon):
        self.rayon=rayon
        self.nom ='cercle'
    def surface (self):
        surface = 2*3.14*(self.rayon**2)
        return (surface)
    def __str__ (self):
            return ("\n le {} ayant le rayon {} et la surface égale à {}"
                .format(self.nom,self.rayon,self.surface()))

class Cylindre (Cercle):
    def __init__ (self,rayon,hauteur):
        Cercle.__init__(self,rayon)
        self.hauteur =hauteur
        self.nom = 'cylindre'
    def volume (self):
        volume = self.surface()*self.hauteur
        return (volume)
class Cone (Cylindre) :
    def __init__ (self,rayon,hauteur):
        Cylindre.__init__(self,rayon,hauteur)
        self.nom = 'cone'
    def volume_cone (self):
        volume_cone = self.volume()/3
        return (volume_cone)
         
cercle = Cercle (14)
print(cercle)

cylindre = Cylindre (2,5)
v1=cylindre.volume()
print(v1)
print(cylindre)

cone = Cone(2,5)
v= cone.volume_cone()
print (v)
print(cone)
