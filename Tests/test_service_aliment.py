from Service.alimente_service import *


def test_service_aliment():
    serv = ServiceAliment()

    a = serv.read(1000)
    assert a is None
    serv.create(1000, 100, 'TEST', 2020-12-12)
    a = serv.read(1000)
    assert a.get_id() == 1000
    assert a.get_id_magazin() == 100
    assert a.get_nume() == 'TEST'
    assert a.get_valabilitate() == 2020-12-12

    serv.update(1000, 200, 'TEST 2', 2012-2-2)
    a = serv.read(1000)
    assert a.get_id() == 1000
    assert a.get_id_magazin() == 200
    assert a.get_nume() == 'TEST 2'
    assert a.get_valabilitate() == 2012 - 2 - 2

    serv.delete(1000)
    a = serv.read(1000)
    assert a is None
