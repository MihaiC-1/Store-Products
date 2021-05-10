from Domain.alimente import *


def test_aliment_getter():
    a = Aliment(1, 4, 'Paine', 2020-10-21)

    assert a.get_id() == 1
    assert a.get_id_magazin() == 4
    assert a.get_nume() == 'Paine'
    assert a.get_valabilitate() == 2020-10-21
