from Repository.magazin_repo import *


def test_repo_magazin():
    repo = RepoMagazin('/Users/c.mihai/Desktop/exersare/laborator 12/test_magazin.txt')

    m = Magazin(1, 'Dacia', 'mixt')

    a = repo.read(1)
    assert a is None
    repo.create(m)
    a = repo.read(1)
    assert a == m

    m_2 = Magazin(1, 'Dacia 2', 'mixt 2')
    repo.update(m_2)
    a = repo.read(1)
    assert a == m_2

    repo.delete(1)
    a = repo.read(1)
    assert a is None
