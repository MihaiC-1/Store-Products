from Domain.magazin import *


def test_magazin_getter():
    m = Magazin(1, 'Dacia', 'mixt')

    assert m.get_id() == 1
    assert m.get_nume() == 'Dacia'
    assert m.get_categorie() == 'mixt'
