
class Voiture (object):
    def __init__ (self,marque,couleur):
        self.couleur=couleur
        self.marque=marque
        self.conducteur="personne"
        self.vitesse= 0
    def choisir_conducteur (self,nom):
        self.conducteur = nom
    def afficher_info (self) :
        print ("marque: ",self.marque,"- couleur: ",self.couleur,"- conducteur: ", self.conducteur,"- vitesse: ",self.vitesse)
mavoiture = Voiture('Ford','rouge')
tavoiture = Voiture ('Hyundai','blanche')
savoiture = Voiture('Suzuki','bleue')
mavoiture.choisir_conducteur('Hassan')
tavoiture.choisir_conducteur('Hanane')
savoiture.choisir_conducteur('Souad')
tavoiture.afficher_info()
