from Domain.alimente import *
import datetime


class RepoAliment:
    def __init__(self, file_name):
        self.file = file_name
        self.store = []
        self.store = self.readFile()

    def readFile(self):
        store_b = []
        f = open(self.file, "r")
        lines = f.readlines()
        for line in lines:
            s = line[:-1]
            rip = s.split("/")
            id_ = int(rip[0])
            id_magazin = int(rip[1])
            nume = rip[2]
            data = rip[3]
            valabil = data.split('-')
            data_valabil = datetime.date(int(valabil[0]), int(valabil[1]), int(valabil[2]))
            c = Aliment(id_, id_magazin, nume, data_valabil)
            store_b.append(c)
        f.close()
        return store_b

    def writeFile(self):
        f = open(self.file, "w")
        content = ""
        for p in self.store:
            line = '{}/{}/{}/{}\n'.format(p.get_id(), p.get_id_magazin(), p.get_nume(), p.get_valabilitate())
            content += line
        f.write(content)
        f.close()

    def create(self, c):
        for p in self.store:
            if p.get_id() == c.get_id():
                raise ValueError('ID-ul exista deja')
        self.store.append(c)
        self.writeFile()

    def read(self, id_=None):
        if id_ is None:
            return self.store[:]
        for p in self.store:
            if p.get_id() == id_:
                return p
        return None

    def update(self, c):
        id_ = c.get_id()
        for index in range(len(self.store)):
            if self.store[index].get_id() == id_:
                self.store[index] = c
                break
        self.writeFile()

    def delete(self, id_):
        for index in range(len(self.store)):
            if id_ == self.store[index].get_id():
                del self.store[index]
                break
        self.writeFile()
        KeyError('Nu exista acest id')

    def all(self):
        return self.store
