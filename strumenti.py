class Strumenti:

    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.__codice=codice
        self.__tipo=tipo
        self.__marca=marca
        self.__anno_acquisto=anno_acquisto
        self.__valore=valore

    def __str__(self): # Definisco print
        return f"{self.__codice}, {self.__tipo}, {self.__marca}, {self.__anno_acquisto}, {self.__valore}"

    @property  # Getter per ordinamento alfabetico
    def marca(self):
        return self.__marca

    @property # Getter per aggiungere prestito
    def codice(self):
        return self.__codice

    # GETTER PER CHECK UGUAGLIANZA STRUMENTI IN AGGIUNGI STRUMENTO - IN ALTERNATIVA DATACLASS
    '''@property
    def tipo(self):
        return self.__tipo

    @property
    def valore(self):
        return self.__valore

    @property
    def anno_acquisto(self):
        return self.__anno_acquisto'''