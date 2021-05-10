from Repository.alimente_repo import *


def test_repo_aliment():
    a = Aliment(1, 4, 'Paine', 2020-2-18)
    repo = RepoAliment('/Users/c.mihai/Desktop/exersare/laborator 12/test_aliment.txt')

    aux = repo.read(1)
    assert aux is None
    repo.create(a)
    aux = repo.read(1)
    assert aux == a

    a2 = Aliment(1, 5, 'Gogoasa', 2021-3-10)
    repo.update(a2)
    aux = repo.read(1)
    assert aux == a2

    repo.delete(1)
    aux = repo.read(1)
    assert aux is None
