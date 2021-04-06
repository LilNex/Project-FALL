from database import *
import account
import pickle

class transaction:
    def __init__(self, fromId, toId, ammount, reason):
        self.fromId = fromId
        self.toId = toId
        self.ammount = ammount
        self.reason = reason
        self.fromUser = loadDb()[fromId].getUser()
        self.toUser = loadDb()[toId].getUser()
        addLog("{} a envoyé à {} un montant de {}$. Raison : {}".format(self.fromUser, self.toUser, self.ammount, self.reason))
        self.statut = "En attente"
    #def __del__(self, name):

    #    return super().__delattr__(name)

    def getFromUser(self):
        return self.fromUser
    def getToUser(self):
        return self.toUser
    def getAmmount(self):
        return self.ammount
    def getReason(self):
        return self.reason

    
def loadTransactions():
    try:
        file = open("transactions.txt", "rb")
        T = pickle.load(file)
        return T
    except FileNotFoundError:
        T = []
        return T

def	saveTransactions(pending):
	pendingFile = open('transactions.txt', 'wb')
	pickle.dump(pending, pendingFile)                      
	pendingFile.close()

def getTransaction(id : int): 
     T = loadTransactions()
     try:
        return T[id]
     except:
         print("Cette transaction est introuvable")
         return None

