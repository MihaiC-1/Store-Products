class Aliment:
    def __init__(self, id_, id_magazin, nume, data_valabil):
        self.id_ = id_
        self.id_magazin = id_magazin
        self.nume = nume
        self.data_valabil = data_valabil

    def __str__(self):
        return 'ID : {}, ID magazin : {}, Nume : {}, Data valabilitate : {}'.format(self.id_, self.id_magazin,
                                                                                    self.nume, self.data_valabil)

    def get_id(self):
        return self.id_

    def get_id_magazin(self):
        return self.id_magazin

    def get_nume(self):
        return self.nume

    def get_valabilitate(self):
        return self.data_valabil
