from deposito_strumenti import DepositoStrumenti # richiamo classe deposito_strumenti
from datetime import datetime # importo funzione per data attuale

def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")
    return input("Scegli un'opzione >> ")

def main():
    deposito = DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")
    elenco_strumenti = [] # creo lista vuota per inserire oggetti strumenti
    elenco_prestiti = [] # creo lista vuota per inserire oggetti prestiti
    while True:
        scelta = menu()
        if scelta == "1":
            # TODO: Aggiorna responsabile nel sistema
            print("Responsabile attuale: ", deposito.responsabile) # stampo a video il responsabile attuale
            nuovo_responsabile = input(str("Inserisci il nuovo responsabile: "))
            deposito.responsabile=nuovo_responsabile # richiamo oggetto deposito in classe DepositoStrumenti

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    for i in deposito.carica_file_strumenti(file_path): # Per ogni elemento della lista restituita dal metodo
                        elenco_strumenti.append(i) # Aggiungi strumento alla lista nel main
                    break
                except Exception as e:
                    print(e)


        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")
            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore (euro): ").strip())
                codice = len(elenco_strumenti)
            except ValueError:
                print("Errore: inserire valori numerici validi per anno e valore.")
                continue
            strumento = deposito.aggiungi_strumento(codice, tipo, marca, anno_acquisto, valore)

            # CODICE OPZIONALE PER VERIFICARE UNICITA' DEGLI STRUMENTI
            '''flag=True
            for i in elenco_strumenti:
                if i.tipo==strumento.tipo and i.marca==strumento.marca and i.valore==strumento.valore and i.anno_acquisto==strumento.anno_acquisto:
                    flag=False
                    break
                else:
                    flag=True
            if flag is True:
                elenco_strumenti.append(strumento)
                print(f"Strumento aggiunto: {strumento}")
            else:
                print("Strumento già presente")'''

            elenco_strumenti.append(strumento) # Aggiungo strumento alla lista
            print(f"Strumento aggiunto: {strumento}")

        elif scelta == "4":
            strumenti_ordinati = deposito.strumenti_ordinati_per_marca(elenco_strumenti)
            if strumenti_ordinati is None: # Stampa messaggio in caso di deposito vuoto
                print("Nessuno strumento inserito")
            else:
                for s in strumenti_ordinati:
                    print(f'- {s}')

        elif scelta == "5":
            id_strumento = input("ID strumento: ")
            cognome_allievo = input("Cognome allievo: ")
            data = datetime.now().date()
            try:
                prestito = deposito.nuovo_prestito(data, id_strumento, cognome_allievo, elenco_strumenti, elenco_prestiti)
                elenco_prestiti.append(prestito) # Aggiungo oggetto prestito a lista
                print(f"Prestito andato a buon fine: {prestito}")
            except Exception as e: # Altrimenti scatena eccezione generica
                print(e)

        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ")
            try:
                elenco_prestiti=deposito.termina_prestito(id_prestito, elenco_prestiti) # Lista prestiti modificata
                print(f"Prestito {id_prestito} terminato con successo.")
            except Exception as e:
                print(e)

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
