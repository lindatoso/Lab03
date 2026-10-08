import csv
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome=nome # Inizializzo i due attributi
        self.__responsabile=responsabile

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter # Per cambiare il valore dell'attributo nascosto uso metodo setter
    def responsabile(self, responsabile): # La funzione prende l'attributo nascosto dalla classe e lo cambia con quello fornito dal main
        self.__responsabile=responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            filein=open(file_path, 'r', encoding='utf-8') # Apro file in lettura
            file=csv.reader(filein) # Uso csv.reader per leggere le singole righe
            from strumenti import Strumenti # Importo la classe strumenti per inserire i dati
            lista_strumenti=[]
            indice=''
            for riga in file:
                item=Strumenti(riga[0],riga[1], riga[2], int(riga[3]), float(riga[4])) # Per ogni riga associo un oggetto in strumento
                #print(item.__str__())
                lista_strumenti.append(item)
                indice=riga[0]
            filein.close()  # Chiudo il file
            return lista_strumenti

        except FileNotFoundError:
            print('File non trovato')



    def aggiungi_strumento(self, codice, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        from strumenti import Strumenti
        code='S'+str(codice+1)
        item=Strumenti(code, tipo, marca, anno_acquisto, valore)
        return item


    def strumenti_ordinati_per_marca(self, lista_strumenti):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        from operator import attrgetter
        ordinato=sorted(lista_strumenti, key=attrgetter('marca'))
        return ordinato


    def nuovo_prestito(self, data, id_strumento, cognome_allievo, lista_strumenti, lista_prestiti):
        """Crea un nuovo prestito"""
        # TODO
        from prestiti import Prestiti
        codice = len(lista_prestiti) + 1
        for i in lista_prestiti:
            if i.id_strumento==id_strumento:
                raise Exception('Lo strumento selezionato è già in prestito')

        prestito = Prestiti(codice, data, id_strumento, cognome_allievo, lista_strumenti)
        return prestito

    def termina_prestito(self, id_prestito, lista_prestiti):
        """Termina un prestito in atto"""
        # TODO
        from prestiti import Prestiti
        flag=False
        for i in lista_prestiti:
            if i.id==id_prestito:
                lista_prestiti.remove(i)
                flag=True
                break
        if not flag:
            raise Exception('Il prestito selezionato non esiste')

        return lista_prestiti
