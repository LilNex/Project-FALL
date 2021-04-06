from transaction import *
from database import *
database = loadDb()
transactions = loadTransactions()
def menu_admin():
    print("System d'administration".center(50,"-"))
    print("1. Afficher toutes les transaction")
    print("2. Afficher les transaction en attente")
    print("3. Rechercher une transaction par numéro")
    print("4. Afficher les détailles d'un compte")



def printAccount():
    print("Rechercher le compte par :\n1. Identifiant       2. Nom et prenom")
    choix = input("Votre choix : ")
    if choix == "1":
        user = input("Entrez l'identifiant du compte à afficher :")
    elif choix == "2":
        nom = input("Entrez le nom du titulaire du compte : ")
        prenom = input("Entrez le prenom du titulaire du compte : ")
        if getUserByName(nom,prenom) is not None:
            user = getUserByName(nom,prenom)
        else:
            user = ""
    if checkUser(user) is not False:
        idUser = checkUser(user)
        print("Détaille du compte : {}".format(user).center(50,"-"))
        print("Nom et prénom : {} {}".format(database[idUser].nom, database[idUser].prenom))
        print("Mot de passe : {} {}".format(database[idUser].getPwd()))
        print("Réponse secrète : {}".format(database[idUser].reponse))
        print("Type du compte (1 = Personel, 2 = Entreprise) : {} ".format(database[idUser].type))
        print("Solde : {} $".format(database[idUser].money))
        if database[idUser].type  == 2:
            print("Nom de l'entreprise : {}".format(database[idUser].companyName))
            print("Employés de l'entreprise : {}".format(database[idUser].employes))
        print("--------------------------------------------------------")
        print("1. Modifier      2.Supprimer le compte")
    else:
        print("Compte inexistant")

def menu_admin_modifier(idAccount):
        

def printAllTransactions():
    for i in range(len(transactions)):
        print("Transaction N°{}".format(i).center(40,"-"))
        print("From :", transactions[i].getFromUser())
        print("To :", transactions[i].getToUser())
        print("Ammount :", transactions[i].getAmmount())
        print("Reason :", transactions[i].getReason())
        print("Status :", transactions[i].statut)
        print("--------------------------------------------")

def printTransaction(id):
    T = getTransaction(id)
    print("Transaction N°{}".format(id).center(40,"-"))
    print("From :", T.getFromUser())
    print("To :", T.getToUser())
    print("Ammount :", T.getAmmount())
    print("Reason :", T.getReason())
    print("Status :", T.statut)
    print("--------------------------------------------")

def printPendingTransactions():
    T = loadTransactions()
    print(T)
    for i in range(len(T)):
        if T[i].statut == "En attente":
            print("Transaction N°{}".format(i).center(40,"-"))
            print("From :", T[i].getFromUser())
            print("To :", T[i].getToUser())
            print("Ammount :", T[i].getAmmount())
            print("Reason :", T[i].getReason())
            print("Status :", T[i].statut)
            print("--------------------------------------------")

def deleteAccount(user : str):
    database = loadDb()
    userId = checkUser(user)
    if checkUser(user) is not False:
        del database[userId]
    else:
        print('User not found')
    saveDb(database)


#printTransaction(5)