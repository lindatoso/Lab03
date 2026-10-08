from typing import dataclass_transform


class Prestiti:

    def __init__(self, id, data, id_strumento, cognome_allievo, lista_strumenti):

        flag = False
        for i in lista_strumenti:
            if i.codice==id_strumento:
                flag=True
                break
        if not flag:
            raise Exception('Lo strumento selezionato non esiste')

        self.__id='P'+str(id)
        self.__data=data
        self.__id_strumento=id_strumento
        self.__cognome_allievo=cognome_allievo


    def __str__(self):
        return f"{self.__id}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"

    @property
    def id_strumento(self):
        return self.__id_strumento

    @property
    def id(self):
        return self.__id