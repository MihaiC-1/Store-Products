from Tests.test_aliment import *
from Tests.test_magazin import *
from Tests.test_repo_magazin import *
from Tests.test_repo_aliment import *
from Tests.test_service_magazin import *
from Tests.test_service_aliment import *


def tests():
    test_aliment_getter()
    test_magazin_getter()
    test_repo_magazin()
    test_repo_aliment()
    test_service_magazin()
    test_service_aliment()
