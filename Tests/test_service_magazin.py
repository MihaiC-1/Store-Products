from Service.magazin_service import *


def test_service_magazin():
    serv = ServiceMagazin()

    rez = serv.read(1000)
    assert rez is None
    serv.create(1000, 'TEST', 'TEST')
    rez = serv.read(1000)
    assert rez.get_id() == 1000
    assert rez.get_nume() == 'TEST'
    assert rez.get_categorie() == 'TEST'

    m = (1000, 'TEST 2', 'TEST 2')
    serv.update(1000, 'TEST 2', 'TEST 2')
    rez = serv.read(1000)
    assert rez.get_id() == 1000
    assert rez.get_nume() == 'TEST 2'
    assert rez.get_categorie() == 'TEST 2'

    serv.delete(1000)
    rez = serv.read(1000)
    assert rez is None
