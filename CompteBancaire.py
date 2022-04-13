class CompteBancaire (object):
    def __init__ (self,nom,solde=0) :
        self.nom_titulaire = nom
        self.solde = solde
    def deposer (self,montant) :
        self.solde = self.solde + montant
    def retrait (self,montant) :
        self.solde = self.solde - montant
    def afficher_info (self):
        print ("nom du titulaire : ", self.nom_titulaire)
        print ("solde : ",self.solde)
compte1= CompteBancaire("Ali",10000)
compte1.deposer(2500)
compte1.retrait(3000)
compte1.retrait(7000)
compte1.deposer(1500)
compte1.afficher_info()
