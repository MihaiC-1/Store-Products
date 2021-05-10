from Repository.alimente_repo import *
import datetime


class ServiceAliment:
    def __init__(self):
        self.repo = RepoAliment('/Users/c.mihai/Desktop/exersare/laborator 12/alimente.txt')

    def create(self, id_, id_magazin, nume, data_valabil):
        clas = Aliment(id_, id_magazin, nume, data_valabil)
        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, id_magazin, nume, data_valabil):
        clas = Aliment(id_, id_magazin, nume, data_valabil)
        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()

    def nr_alimete_magazin(self, id_):
        counter = 0
        alimente = self.show_all()

        for a in alimente:
            if a.get_id_magazin() == id_:
                counter += 1

        return counter

    def alimente_in_magazine(self):
        alimente = self.show_all()
        rez = []
        for a in alimente:
            counter = 1
            if a.get_nume() in rez:
                for a2 in alimente:
                    if a2 != a and a2.get_valabilitate() > datetime.date.today() and \
                            a.get_valabilitate() > datetime.date.today():
                        counter += 1
            else:
                rez.append(a.get_nume())

            if counter > 1:
                for a3 in alimente:
                    if a3.get_nume() == a.get_nume() and a3.get_valabilitate() > datetime.date.today():
                        print(a3, '\n')
