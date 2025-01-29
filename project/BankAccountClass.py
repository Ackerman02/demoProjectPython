#Definizione superclasse e classe
class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto


class ContoCorrente(Conto):
    #Definizione inizializzatore con 3 parametri
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    #Definizione metodi di prelievo, deposito e descrizione conti

    def preleva(self, importo):
        if importo <= self.__saldo:
            self.__saldo -= importo
            return True
        else:
            return False

    def deposita(self, importo):
        self.__saldo += importo
        return self.__saldo

    def descrizione(self):
        print("Nome: " + self.nome)
        print("Conto: " + self.conto)
        print("Saldo: " + str(self.__saldo))


    #Definizione metodi getter (@property) e setter e rendendo
    #l'attributo saldo "privato".

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)


#Creazione terza classe
class GestoriContiCorrenti:
    @staticmethod
    #Definizione metodo statico con condizione
    def bonifico(sorgente, destinazione, importo):
        if sorgente.preleva(importo):
            destinazione.deposita(importo)
            return True
        print("Bonifico senza successo a causa di fondi insufficienti!")
        return False


#Run del programma con alcune funzioni
#Mocked and hardcoded data. It can be modified and place it dynamically. 
#In the future I'll try!
conto1 = ContoCorrente('Federico', 'IT5456', 10000)
conto2 = ContoCorrente('Marco', 'IT4446', 20000)
contoDruido = ContoCorrente('Antonio', 'Ischia', 50000)

#Esempio di utilizzo della terza classe creata
GestoriContiCorrenti.bonifico(conto1, conto2, 11000)

print("\nSaldo dopo il bonifico:")
print(f"Federico: {conto1.saldo}€")
print(f"Marco: {conto2.saldo}€")
print(f"Antonio: {contoDruido.saldo}€")
