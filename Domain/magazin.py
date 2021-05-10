class Magazin:
    def __init__(self, id_, nume, categorie):
        self.id_ = id_
        self.nume = nume
        self.categorie = categorie

    def __str__(self):
        return 'ID : {}, Nume : {}, Categorie : {}'.format(self.id_, self.nume, self.categorie)

    def get_id(self):
        return self.id_

    def get_nume(self):
        return self.nume

    def get_categorie(self):
        return self.categorie
