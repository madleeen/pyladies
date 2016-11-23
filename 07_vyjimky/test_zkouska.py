#test spustim "python -m pytest -v" ve slozce kde jsou soubory test_*

import pytest #pro testovani raisovani vyjimek

def secti(a,b):
    if (isinstance (a, (int, float)) and isinstance(b, (int, float))):
        return a + b
    else:
        raise TypeError("Toto neni cislo")

def test_secti():
# assert = otestovani - kdyz je podminka true, je to ok, jinak false
    assert secti (1,3) == 4
    assert secti (1.5,3.5) == 5.0
    #otestuju ze to vyhodi vyjimku
    with pytest.raises(TypeError):
        secti ("a","b")
