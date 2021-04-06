import pickle
from datetime import *
from time import sleep



pending_transactions = []

def loadDb():
	try:
		dbFile = open("database.txt", "rb")
		db = pickle.load(dbFile)
	except:
		db = []
	return db

def saveDb(db):
	dbfile = open('database.txt', 'wb')
	pickle.dump(db, dbfile)                      
	dbfile.close()

def addLog(line:str):
	#logs = []
	logsFile = open('logs.txt', 'a')  
	logsFile.write("{} | {}\n".format(datetime.now(), line))
	#print("logs added")
	logsFile.close()

def redirection(sec):
	print("Retour automatique dans", end =' ')
	for i in range(sec):
		print(str(sec-i),end =' ')
		sleep(1.0)
		if i + 1 == sec:
			break

from account import *
getUser = lambda id: loadDb()[id].getUser()

from transaction import *

def loadPendingTransactions():
	transactions = loadTransactions()
	print(transactions)
	pending_transactions = []
	for i in range(len(transactions)):
		if transactions[i].statut == "En attente":
			pending_transactions.append((transactions[i],i))
	return pending_transactions



def addPendingTransactions(database, fromId, toId, ammount, reason):
	transactions = loadTransactions()
	transactions.append(transaction(fromId, toId,ammount,reason))
	file = open("transactions.txt", "wb")
	pickle.dump(transactions, file)
	file.close()
	print(transactions)

def checkUser(user : str):
	database = loadDb()
	for i in range(len(database)):
		if database[i].getUser() == user:
			return i
	return False

def getUserByName(nom : str , prenom : str):
	database = loadDb()
	for i in range(0, len(database)):
		if database[i].nom.lower() == nom.lower():
			if database[i].prenom.lower() == prenom.lower():
				return database[i].user
	return None

#def getIdByUser(user: str):
#	database = loadDb()
#	for i in range(0, len(database)):
#		if database[i].user.lower() == user.lower():
#			return i
#	return None

