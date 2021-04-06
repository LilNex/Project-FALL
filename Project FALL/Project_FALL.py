import os

from getpass import getpass as inputPass
from account import *
from transaction import *
from Admin import *
from database import *
#user : ismail   PWD : LILnex123@@@
#user : lilnex   PWD : lilNEX123]]]
#user : koba	 PWD : LADlad777@@@
clear = lambda: os.system('cls')
global tentative
tentative = 0
database = []


def recoverPwd():
	tentativeRep = 0
	recUser = str(input("Entrez votre identifiant : "))
	if recUser !="":
		for id in range(0, len(database)):
			if recUser == database[id].getUser():
				print("La question secrète : Quel est votre animal  ?")
				while tentativeRep < 3:
					recRep = str(input("Entrez la réponse secrète : "))
					if recRep == database[id].getRep():
						new_pwd = str(input("Entrez votre nouveau mot de passe : "))
						while(checkPwd(new_pwd) == False):
							new_pwd = input("Le mot de passe doit contenir au moins 12 caractères, avec 3 majuscules, 3 miniscules et 3 chiffres : ")
						database[id].setPwd(new_pwd)
						saveDb(database)
						addLog("{} a changé le mot de passe".format(database[id].user))
						print("Le mot de passe a été modifié avec succès.")
						redirection(3)
						return True
					else:
						tentativeRep += 1
						print("Mauvaise réponse.")
				if tentativeRep >= 3:
					print("Vous êtes bloqués par le système.")
					x = 2
					while x > 1:
						pass
		print("Identifiant introuvable.")
		redirection(3)
	else:
		page_acceuil()
				#break

def transferMoney(fromId, toId, ammount, reason):
	global database
	database = loadDb()
	ammount = int(ammount)
	if database[fromId].getMoney() >= ammount :
		database[fromId].takeMoney(ammount)
		addPendingTransactions(database, fromId, toId, ammount, reason)
		#database[toId].addMoney(ammount)
		saveDb(database)
		return True
	else:
		print("Vous n'avez pas ce montant.")
	
		return False
def parametre(id):
    print("1. Changer le nom et prénom")
    print("2. Changer le mot de passe")


def registerDatabase(accountType, nom, prenom, addUser, addPwd, addRep):
	database.append(account.account(accountType, nom, prenom, addUser,addPwd,addRep))
	saveDb(database)
	return True

def checkPwd(tempPwd):
	cptUpper = int(0)
	cptLower = int(0)
	cptDigits = int(0)
	cptUpper = int(0)
	for l in tempPwd:
		if l in {"@", "\\", ";"}:
			return False
		if (l.isupper()):
			cptUpper += 1
		if (l.islower()):
			cptLower += 1
		if (l.isnumeric()):
			cptDigits += 1
	if (cptUpper >= 3) and (cptLower >= 3) and (cptDigits >= 3) and (len(tempPwd) >= 12):
		return True
	else:
		return False

def register():
	clear()
	print("Création d'un compte".center(50,"-"))
	accountType = input("Choisissez le type du compte:\n1. Personel		2.Entreprise\nVotre choix : ")
	while accountType not in ["1" ,"2"]:
		accountType = input("Choisissez le type du compte:\n1. Personel		2.Entreprise\nVotre choix : ")	
	nom = input("Entrez votre nom :").capitalize()
	while nom.isalpha() is not True:
		print("Nom incorrect.")
		nom = input("Entrez votre nom :").capitalize()
	prenom = input("Entrez votre prénom :").capitalize()
	while prenom.isalpha() is not True: 
		print("Prénom incorrect.")
		prenom = input("Entrez votre prénom :").capitalize()
	new_user = input("Entrez le nom du compte : ")
	if new_user !="":
		while(checkUser(new_user) is not False):
			new_user = input("Nom de compte déja utilisée, essayez un autre : ")
		new_pwd = input("Entrez le mot du passe : ")### must contain 12 characters that must include 3 lowercase letters,
													### 3 uppercase letters, 3 digits, and three other characters that are not digits and not letters
		while(checkPwd(new_pwd) == False):
			  new_pwd = input("Le mot de passe doit contenir au moins 12 caractères, avec 3 majuscules, 3 miniscules et 3 chiffres : ")		
		print("La question secrète : Quel est votre animale préféré")
		new_rep = input("Entrez la réponse secrète : ")
		if registerDatabase(int(accountType), nom, prenom, new_user, new_pwd, new_rep) == True:
			print("Votre compte a été crée avec succès")
			addLog("{} a crée un compte.".format(new_user))
			print("-----------------------------------------------------")
			redirection(3)
			clear()
	else: 
		print("-----------------------------------------------------")

def login():
	clear()
	if len(database) != 0:
		global tentative
		while tentative < 3:
			global id
			id = None
			print("Connexion à un compte".center(50,"-"))
			log_user = input("Entrez le nom du compte : ")
			if log_user != "":
				log_pwd = inputPass("Entrez le mot de passe : ")
				for i in range(0, len(database)):
					if log_user == database[i].getUser():
						if log_pwd == database[i].getPwd():
							id = i
							print("Vous êtes connecté à votre compte")
							addLog("{} s'est connecté à son compte.".format(database[id].user))
							redirection(3)
							print("\n-----------------------------------------------------\n")
							page_principal(id)
							break
						else:
							tentative += 1
							print("Mot de passe invalide")
							if tentative ==3:
								y = input("Voulez vous récuperer votre mot de passe ? Tapez O")
								if y.lower() == "o":
									recoverPwd()
								else:
									print("Vous êtes bloqués par le système")
									x = 2
									while x > 1:
										pass
							break
					elif i+1== len(database): 
						print("Votre identifiant n'est pas enregistré")
			else:
				page_acceuil()
				break
			if id is not None :
				break
	else: 
		print("Base de données vide\nVous serez redirigé vers l'inscription.")
		redirection(3)
		register()

def deconnexion(id):
	saveDb(database)
	id = None
	page_acceuil()




def page_acceuil():
	while True:
		clear()
		print("FALL Bank".center(50))
		print("1. Connectez vous ")
		print("2. Créez un nouveau compte ")
		print("3. Mot de passe oubilé ? ")
		print("4. Quitter le programme")
		choix = input("Entrez votre choix : ")
		print("\n-----------------------------------------------------\n")
		menu = {
			"1" : login,
			"2" : register,
			"3" : recoverPwd,
			"4" : exit
			}
		if choix in menu.keys():
			menu[choix]()
		else:
			pass

def page_principal(id):
	clear()
	global database
	database = loadDb()
	print("Votre solde : ", database[id].getMoney(),"$")
	print("1. Transferez à un autre compte.") 
	print("2. Voir les transactions en attente.")
	if database[id].type == 2:
		print("3. Effectuer un paiement à vos employés")
		print("4. Ajouter ou supprimer un employés")
	print("0. Deconnexion.")
	choix = input("Entrez votre choix :")
	print("\n-----------------------------------------------------\n")
	menu = {
		'1' : page_transfer,
		'2' : page_pending,
		'3'	: page_business_pay,
		'4' : page_business_employe,
		'0' : deconnexion
		}
	menu.get(choix,page_principal)(id)


def page_pending(id):
	clear()
	database = loadDb()
	transactions = []
	transactions = loadTransactions()
	#print(pending)
	id_pending = {}
	id_transac =0
	for i in range(len(transactions)):
		if transactions[i].statut == "En attente":
			if transactions[i].getToUser() == database[id].getUser():
				id_transac += 1
				id_pending[id_transac]= (transactions[i], i)
				if id_transac == 1 :
					print("Liste des transactions en attente".center(50,"*"))
				print("N°{} : {} vous a envoyé {}$, Raison :{}".format(id_transac,transactions[i].getFromUser(), transactions[i].getAmmount(),transactions[i].getReason() ))
			if transactions[i].getFromUser() == database[id].getUser():
				id_transac += 1
				id_pending[id_transac]= (transactions[i], i)
				if id_transac == 1 :
					print("Liste des transactions en attente".center(50,"*"))
				print("N°{} : Vous avez envoyé {}$ à {}, Raison :{}".format(id_transac,transactions[i].getAmmount(), transactions[i].getToUser(),transactions[i].getReason() ))
	if id_pending == {} :
		print("Vous n'avez aucune transactions en attente")
		print("1 . Voir l'historique des transactions")
		print("Autres. Retour en arrière")
		x = input("Votre choix : ")
		try:
			if int(x) == 1:
				pass
			else: page_principal(id)
		except:
			page_principal(id)
		

	else:
		# print(id_pending)
		while True:
			choix = input("Entrez le numéro de transaction pour plus de détaille :")
			try:
				id_choix = int(choix)
			except ValueError:
				page_principal(id)
			if id_pending.get(id_choix, None) == None:
				print("Numero incorrect")
			else:
				if id_pending.get(id_choix)[0].getFromUser() == database[id].getUser():
					clear()
					print("Transaction N°{}".format(id_pending.get(id_choix)[1]).center(30,"*"))
					print("Virement au compte :",id_pending.get(id_choix)[0].getToUser())
					print("Au nom de : {} {}".format(database[checkUser(id_pending.get(id_choix)[0].getToUser())].nom,database[checkUser(id_pending.get(id_choix)[0].getToUser())].prenom))
					print("Montant : {}$".format(id_pending.get(id_choix)[0].getAmmount()))
					print("Raison :",id_pending.get(id_choix)[0].getReason())
					print("******************************")
					print("1- Annuler la transaction         2-Retour")
					x = int(input("Votre choix : "))
					if x == 1:
						database[id].addMoney(id_pending.get(id_choix)[0].getAmmount())
						id_pending.get(id_choix)[0].statut = "Annulé"
						#print(id_pending.get(id_choix))
						transactions[id_pending.get(id_choix)[1]] = id_pending.get(id_choix)[0]
						addLog("{} a annulé la transaction N°{}.".format(database[id].getUser(),id_pending.get(id_choix)[1]))
						saveTransactions(transactions)
						saveDb(database)
						print('Vous avez annulé la transaction.')
						redirection(3)
						page_pending(id)
					else:
						page_pending(id)
				elif id_pending.get(id_choix)[0].getToUser() == database[id].getUser():
					clear()
					print("Transaction N°{}".format(id_pending.get(id_choix)[1]).center(30,"*"))
					print("Recu du compte :",id_pending.get(id_choix)[0].getFromUser())
					print("Au nom de : {} {}".format(database[checkUser(id_pending.get(id_choix)[0].getFromUser())].nom,database[checkUser(id_pending.get(id_choix)[0].getFromUser())].prenom))
					print("Montant : {}$".format(id_pending.get(id_choix)[0].getAmmount()))
					print("Raison :",id_pending.get(id_choix)[0].getReason())
					print("******************************")
					print("1- Accepter la transaction       2-Refuser la transaction       3-Retour")
					x = int(input("Votre choix : "))
					if x == 1:
						database[id].addMoney(id_pending.get(id_choix)[0].getAmmount())
						id_pending.get(id_choix)[0].statut = "Accepté"
						transactions[id_pending.get(id_choix)[1]] = id_pending.get(id_choix)[0]
						addLog("{} a accepté la transaction N°{}.".format(database[id].getUser(),id_pending.get(id_choix)[1]))
						saveTransactions(transactions)
						saveDb(database)
						print("Transaction effectué")
						redirection(3)
						page_principal(id)
					elif x == 2:
						for j in range(0, len(database)):
							if database[j].getUser() == id_pending.get(id_choix)[0].getFromUser():
								print(database[j].getUser(),"--",id_pending.get(id_choix)[0].getFromUser() )
								id_pending.get(id_choix)[0].statut = "Refusé - Remboursé"
								database[j].addMoney(id_pending.get(id_choix)[0].getAmmount())
								addLog("{} a refusé la transaction N°{}.".format(database[id].getUser(),id_pending.get(id_choix)[1]))
								break
						transactions[id_pending.get(id_choix)[1]] = id_pending.get(id_choix)[0]
						saveTransactions(transactions)
						saveDb(database)
						print("Vous avez refuser la transaction.")
						page_principal(id)
					else:
						page_pending(id)
				break

	#print(id_pending)
	
	print("\n-----------------------------------------------------\n")

def page_business_employe(id):
	database = loadDb()
	clear()
	if database[id].type == 2:
		while True:
			database = loadDb()
			clear()
			print("Gestion des employés de l'entreprise".center(50,"-"))
			print("1. Afficher la liste des identifiants de vos employés.")
			print("2. Ajouter un employé.")
			choix = input("Votre choix :")
			if choix == "1":
				id_employe = {}
				for i in range(len(database[id].employes)):
					id_employe[i+1] = database[id].employes[i]
					print("{}. {}".format(i+1,database[id].employes[i]))
				if id_employe != {}:
					choix2= input("Tapez le numero de l'identifiant pour le supprimer, sinon laissez vide et tapez Entrer: ")
					if choix2 == "":
						pass
					elif int(choix2) in id_employe.keys():
						del database[id].employes[int(choix2)-1]
						print("Employé retiré de la liste avec succès.")
						saveDb(database)
						redirection(3)
				else:
					print("Vous n'avez aucun employé ajouté.")
					redirection()
			elif choix == "2":
				database[id].addEmployee()
				saveDb(database)
				redirection(3)
			else:
				break
		page_principal(id)
	else:
		print("Vous devez avoir un compte entreprise.")
		redirection(3)
		page_principal(id)

def page_business_pay(id):
	database = loadDb()
	clear()
	if database[id].type == 2:
		print("Effectuer un paiement à vos employés".center(50,"*"))
		ammount = float(input("Entrez le montant :"))
		raison = input("Entrez la raison : ")
		print("Détails de la transaction".center(50,"-"))
		print("Votre liste d'employés :")
		for i in range(len(database[id].employes)):
			nom = database[checkUser(database[id].employes[i])].nom
			prenom = database[checkUser(database[id].employes[i])].prenom
			print("{} {} - {} $".format(nom, prenom, ammount))
		print("Total : {} $".format(ammount * len(database[id].employes)))
		confirmation = input("1. Confirmer		Autres. Retour\nVotre choix : ")
		if confirmation == "1":
			if database[id].money >= (ammount * len(database[id].employes)):
				for i in range(len(database[id].employes)):
					if transferMoney(id ,checkUser(database[id].employes[i]), ammount, raison) == True:
						pass
				print("Transaction effectué avec succès.")
				redirection(3)
				page_principal(id)
			else:
				print("Vous n'avez pas ce montant.")
				redirection(3)
				page_principal(id)
		else:
			page_principal(id)
	else:
		print("Vous devez avoir un compte entreprise.")
		redirection(3)
		page_principal(id)

def page_transfer(id):
	while True:
		clear()
		print("Transfers vers un autre compte".center(40,"*"))
		choix = input("Choisissez un moyen :\n1. Par Identifiant		2.Par Nom et prenom.\nVotre choix : ")
		if choix == "1":
			toUser = str(input("Entrez l'identifiant du destinataire :")).lower()
			for i in range(0, len(database)):
				try:
					while toUser == database[id].getUser().lower():
						print("Vous ne pouvez pas envoyé à vous même.")
						toUser = str(input("Entrez l'identifiant du destinataire :")).lower()
					if toUser == database[i].getUser().lower() :
						toId = i
						ammount = float(input("Entrez le montant à transférer :"))
						reason = str(input("Entrez la raison du transfert :"))
						break
					elif toUser == "":
						break
					elif i + 1 == len(database) and toUser != database[i].getUser().lower():
						print("L'identifiant n'est pas enregistré.")
				except:
					print("**ERREUR** - L'identifiant n'est pas enregistré.")
					toUser = ""
		elif choix == "2":
			Nom = input("Entrez le nom du destinataire :")
			Prenom = input("Entrez le prénom du destinataire :")
			toUser = getUserByName(Nom, Prenom)
			for i in range(0, len(database)):
				try:
					while toUser == database[id].getUser().lower():
						print("Vous ne pouvez pas envoyé à vous même.")
						toUser = str(input("Entrez l'identifiant du destinataire :")).lower()
					if toUser == database[i].getUser().lower() :
						toId = i
						ammount = float(input("Entrez le montant à transférer :"))
						reason = str(input("Entrez la raison du transfert :"))
						break
					elif toUser == "":
						break
					elif i + 1 == len(database) and toUser != database[i].getUser().lower():
						print("L'identifiant n'est pas enregistré.")
				except:
					print("L'identifiant n'est pas enregistré.")
					redirection(3)
		else:
			toUser = ""	

		if toUser == "" or toUser is False:
			print("\n-----------------------------------------------------\n")
			page_principal(id)
			break
		else:
			try:
				if transferMoney(id , toId, ammount,reason) == True:
					print("Transaction effectué : ",ammount,"$ envoyé au compte ",database[toId].getUser())
					print("\n-----------------------------------------------------\n")
					redirection(3)
					page_principal(id)
					break
				else:
					print("Transaction échoué.")
					redirection(3)
					page_transfer(id)
			except UnboundLocalError:
				print("Transaction échoué.")
				redirection(3)
				page_transfer(id)
				break
	page_principal(id)

def printDB():
	for id in range(0, len(database)):
		print("User : ",database[id].getUser())
		print("Pwd : ",database[id].getPwd())
		print("Réponse : ",database[id].getRep())
		print("Money : ",database[id].getMoney(),"$")	
		print("-----------------------------------------------------")


database = loadDb()
# id = int(input("id: "))
page_principal(2)
# printDB()
# page_acceuil()
os.system("cls")
saveDb(database)
print("Fin du program".center(50,"-"))
printDB()
#clear()


