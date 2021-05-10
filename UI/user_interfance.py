from Service.magazin_service import *
from Service.alimente_service import *
import datetime
import json


class Console:
    def __init__(self):
        self.magazine = ServiceMagazin()
        self.alimente = ServiceAliment()

    def menu(self):
        print('1. Adauga magazin')
        print('2. Adauga aliment')
        print('3. Afisare magazine crescator dupa nr alimente')
        print('4. Afisare alimente din minim 2 magazine.')
        print('5. Export Excel.')
        print('6. Exit')

    def handle_add_magazin(self):
        try:
            id_ = int(input('ID : '))
            nume = input('Nume : ')
            categorie = input('Categorie : ')

            if nume == '':
                raise ValueError('Numele trebuie sa fie nenul.')

            self.magazine.create(id_, nume, categorie)
        except Exception as ex:
            print(ex)

    def handle_add_aliment(self):
        try:
            id_ = int(input('ID : '))
            id_magazin = int(input('ID magazin : '))
            nume = input('Nume : ')
            data = input('Data valabilitate an,luna,zi : ')

            if nume == '':
                raise ValueError('Numele trebuie sa fie nenul.')

            magazin = self.magazine.show_all()
            ok = True
            for m in magazin:
                if m.get_id() == id_magazin:
                    ok = False
                    break
            if ok:
                raise ValueError('ID magazin nu exista.')

            v = data.split(',')
            valabil = datetime.date(int(v[0]), int(v[1]), int(v[2]))

            self.alimente.create(id_, id_magazin, nume, valabil)
        except Exception as ex:
            print(ex)

    def handle_show_magazine_crescator(self):
        magazine = self.magazine.show_all()

        for i in range(len(magazine) - 1):
            for j in range(i+1, len(magazine)):
                if self.alimente.nr_alimete_magazin(magazine[i].get_id()) > \
                        self.alimente.nr_alimete_magazin(magazine[j].get_id()):
                    aux = magazine[i]
                    magazine[i] = magazine[j]
                    magazine[j] = aux

        for m in magazine:
            print(m, ' --> nr alimente : ', self.alimente.nr_alimete_magazin(m.get_id()), '\n')

    def handle_alimente_in_magazine(self):
        self.alimente.alimente_in_magazine()

    def handle_Excel_file(self):
        magazine = self.magazine.show_all()
        alimente = self.alimente.show_all()
        data = {}
        for m in magazine:
            if m.get_categorie() not in data:
                data[m.get_categorie()] = []

        for a in alimente:
            for m in magazine:
                if m.get_id() == a.get_id_magazin():
                    data[m.get_categorie()].append(a.get_nume())
                    break

        file = '/Users/c.mihai/Desktop/exersare/laborator 12/'
        name = input('Numele fisierului : ')
        name += '.xls'
        file += name
        f = open(file, "w")
        json.dump(data, f, indent=4)

    def run_console(self):
        while True:
            self.menu()
            op = input('Alegeti optiunea : ')

            if op == '1':
                self.handle_add_magazin()
            elif op == '2':
                self.handle_add_aliment()
            elif op == '3':
                self.handle_show_magazine_crescator()
            elif op == '4':
                self.handle_alimente_in_magazine()
            elif op == '5':
                self.handle_Excel_file()
            elif op == '6':
                print('Exit program')
                break
            else:
                print('Nu exista optiunea.')
