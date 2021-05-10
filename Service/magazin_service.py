from Repository.magazin_repo import *


class ServiceMagazin:
    def __init__(self):
        self.repo = RepoMagazin('/Users/c.mihai/Desktop/exersare/laborator 12/magazine.txt')

    def create(self, id_, nume, categorie):
        clas = Magazin(id_, nume, categorie)
        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, nume, categorie):
        clas = Magazin(id_, nume, categorie)
        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()
