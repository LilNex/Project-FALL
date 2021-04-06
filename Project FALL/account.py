from database import *
from math import *

class account:
    def __init__(self, accountType, nom, prenom, user, pwd, reponse):
        self.nom = nom
        self.prenom = prenom
        self.user = user
        self.pwd = encryptPwd(pwd)
        self.reponse = reponse
        self.money = 1000.00
        self.type = int(accountType)
        choix =("Etes vous un administeur ? Si oui, Tapez O :")
        if choix.lower() == "o":
            self.admin = True
        else:
            self.admin = False
        print("Class account initialized")
        if accountType == 2:
            print("""Le mode entreprise vous permet d'effectuer un paimenet à vos employés
inscrits dans la bank.""")
            self.companyName = input("Entrez le nom de votre entreprise :")
            self.employes = []
            choix = input("Voulez-vous ajoutez un employé ? Tapez O.")
            while choix.lower() == "o":
                choix2 = 0
        while choix2 not in [1,2]:
            choix2 = int(input("""Voulez-vous l'ajouter par son:\n1. Identifiant         2.Nom et prénom\nVotre choix :"""))
            if choix2 == 2:
                employeNom = input("Entrez le nom de l'employé :")
                employePrenom = input("Entrez le prénom de l'employé :")
                employeUser = getUserByName(employeNom, employePrenom)
                if employeUser is not None:
                    if employeUser in self.employes:
                        print("Cet identifiant est déja ajouté dans la liste")
                    else:
                        self.employes.append(employeUser)
                        print("Compte bancaire ajouté avec succès à la liste des employés.")
                else:
                    print("Nom ou prenom introuvable.")
            elif choix2 == 1:
                employeUser = input("Entrez l'identifiant du compte de votre employé : ")
                if checkUser(employeUser) is not False:
                    if employeUser in self.employes:
                        print("Cet identifiant est déja ajouté dans la liste")
                    else:
                        self.employes.append(employeUser)
                        print("Le compte de votre employé ajouté avec succès !")
                else:
                    print("Identifiant introuvable")
                    choix = input("Voulez-vous ajoutez un employé ? Tapez O.")

# def makePayment(self, ammount):s


    def addMoney(self,ammount):
        ammount = abs(ammount)
        if self.money == None:
            self.money = ammount
        else:
            self.money += ammount

    def setMoney(self,ammount):
        self.money = ammount

    def takeMoney(self,ammount):
        ammount = abs(ammount)
        self.money -= ammount
    
    def getUser(self):
        return self.user

    def getPwd(self):
        return decryptPwd(self.pwd)
    def setPwd(self, newPwd):
        self.pwd = encryptPwd(newPwd)

    def getRep(self):
        return self.reponse
    def getMoney(self):
        return self.money

    def addEmployee(self):
        choix2 = 0
        while choix2 not in [1,2]:
            choix2 = int(input("""Voulez-vous l'ajouter par son:\n1. Identifiant         2.Nom et prénom\nVotre choix :"""))
            if choix2 == 2:
                employeNom = input("Entrez le nom de l'employé :")
                employePrenom = input("Entrez le prénom de l'employé :")
                employeUser = getUserByName(employeNom, employePrenom)
                if employeUser is not None:
                    if employeUser in self.employes:
                        print("Cet identifiant est déja ajouté dans la liste")
                    else:
                        self.employes.append(employeUser)
                        print("Compte bancaire ajouté avec succès à la liste des employés.")
                else:
                    print("Nom ou prenom introuvable.")
            elif choix2 == 1:
                employeUser = input("Entrez l'identifiant du compte de votre employé : ")
                if checkUser(employeUser) is not False:
                    if employeUser in self.employes:
                        print("Cet identifiant est déja ajouté dans la liste")
                    else:
                        self.employes.append(employeUser)
                        print("Le compte de votre employé ajouté avec succès !")
                else:
                    print("Identifiant introuvable")

def encryptPwd(pwd : str):
        cryptedPwd = ""
        for x in pwd:
             if ord(x)%2 == 0:
                 cryptedPwd += chr(int(ord(x)/2))
                 continue
             else:
                 cryptedPwd += chr(ord(x)+150)
                 continue
        return cryptedPwd

def decryptPwd(cryptedPwd):
         decryptedPwd = ""
         for x in cryptedPwd:
             if ord(x) < 150:
                 decryptedPwd += chr(int(ord(x)*2))
                 continue
             else:
                 decryptedPwd += chr(ord(x)-150)
                 continue
             
         return decryptedPwd

# [54, 255, 54, 39, 219, 44, 199, 25, 201, 32, 32, 32]

# ['6', 'ÿ', '6', "'", 'Û', ',', 'Ç', '\x19', 'É', ' ', ' ', ' ']

# ['l', 'i', 'l', 'N', 'E', 'X', '1', '2', '3', '@', '@', '@']

 
        





