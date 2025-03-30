import pytest
from List import LinkedList

def test_empty_list():
    lst = LinkedList()
    assert len(lst) == 0
    assert str(lst) == ""

def test_append():
    lst = LinkedList()
    lst.append(1)
    assert str(lst) == "1"
    assert len(lst) == 1
    lst.append(2)
    assert str(lst) == "1 2"
    assert len(lst) == 2

def test_clear():
    lst = LinkedList()
    lst.append(1)
    assert str(lst) == "1"
    assert len(lst) == 1
    lst.clear()
    assert str(lst) == ""
    assert len(lst) == 0

def test_insert():
    lst = LinkedList()
    lst.insert(0, 1)
    assert str(lst) == "1"
    assert len(lst) == 1
    lst.insert(0, 10)
    assert str(lst) == "10 1"
    assert len(lst) == 2
    lst.insert(1, 4)
    assert str(lst) == "10 4 1"
    assert len(lst) == 3



def test_remove():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    assert str(lst) == "1 2 3 4 5"
    assert len(lst) == 5
    lst.remove(0)
    assert str(lst) == "2 3 4 5"
    assert len(lst) == 4
    lst.remove(3)
    assert str(lst) == "2 3 4"
    assert len(lst) == 3
    lst.remove(1)
    assert str(lst) == "2 4"
    assert len(lst) == 2

def test_getitem():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert lst[0] == 1
    assert lst[1] == 2

def test_getitems_errors():
    lst = LinkedList()
    with pytest.raises(ValueError, match="The list is empty"):
        lst[0]
    lst.append(1)
    with pytest.raises(IndexError, match="Index out of range"):
        lst[1]
    with pytest.raises(IndexError, match="Index out of range"):
        lst[-1]

def test_insert_errors():
    lst = LinkedList()
    with pytest.raises(IndexError, match="Index out of range"):
        lst.insert(1, 0)
    lst.append(1)
    with pytest.raises(IndexError, match="Index out of range"):
        lst.insert(5, 0)
    with pytest.raises(IndexError, match="Index out of range"):
        lst.insert(-1, 0)

def test_remove_errors():
    lst = LinkedList()
    with pytest.raises(ValueError, match='The list is empty'):
        lst.remove(0)
    lst.append(1)
    with pytest.raises(IndexError, match="Index out of range"):
         lst.remove(1)
    with pytest.raises(IndexError, match="Index out of range"):
        lst.remove(-1)
