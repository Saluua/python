tourdechien=[]
class Chien (object) :
    def __init__ (self,nom):
        self.nom = nom
    def ajouter_tour_chien (self,nomtour):
        self.tour=nomtour
        tourdechien.append(nomtour)
    def afficher_info (self):
        print ("le chien est ", self.nom, "et ses tours de chien sont :")
        for tour in tourdechien :
            print (tour)
chien1 = Chien ("Rex")
chien1.ajouter_tour_chien ('tourner sur son dos')
chien1.ajouter_tour_chien('rapporter un objet')
chien1.afficher_info()
