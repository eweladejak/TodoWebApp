SCIEZKA = 'todos.txt'


def pobierz_liste(sciezka=SCIEZKA):
    """ Zwraca listę czynności pobraną z pliku todos.txt. """
    with open(sciezka, 'r', encoding='utf-8') as pl:
        lista = pl.readlines()
    return lista

def zapisz_liste(lista, sciezka=SCIEZKA):
    """ Zapisuje listę do pliku tekstowego. """
    with open(sciezka, 'w', encoding='utf-8') as pl:
        pl.writelines(lista)

# print(__name__)
if __name__ == '__main__':
    print('Zaimportowałeś moje funkcje! Gratuluję!')
    print(pobierz_liste())
