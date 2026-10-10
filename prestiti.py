class Prestiti:

    def __init__(self, id, data, id_strumento, cognome_allievo, lista_strumenti):

        flag = False # Check esistenza strumento --> se non esiste non creo l'oggetto
        for i in lista_strumenti:
            if i.codice==id_strumento:
                flag=True
                break
        if not flag:
            raise Exception('Lo strumento selezionato non esiste')

        self.__id='P'+str(id) # Id è il codice calcolato in deposito_strumenti
        self.__data=data
        self.__id_strumento=id_strumento
        self.__cognome_allievo=cognome_allievo


    def __str__(self): # Definisco funzione print
        return f"{self.__id}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"

    @property # Accedere all'id strumento per aggiungere prestito
    def id_strumento(self):
        return self.__id_strumento

    @property # Accedere all'id prestito per terminare prestito
    def id(self):
        return self.__id