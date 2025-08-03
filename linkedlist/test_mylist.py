import pytest
from books.python_exercise.Chapter7.mylist import mylist

def test_append_and_len():
    l = mylist()
    assert len(l) == 0
    l.append(1)
    l.append(2)
    assert len(l) == 2
    assert l[0] == 1
    assert l[1] == 2

def test_pop():
    l = mylist()
    l.append(10)
    l.append(20)
    assert l.pop() == 20
    assert l.pop() == 10
    with pytest.raises(IndexError):
        l.pop()

def test_clear():
    l = mylist()
    l.append(1)
    l.append(2)
    l.clear()
    assert len(l) == 0

def test_find():
    l = mylist()
    l.append(5)
    l.append(10)
    l.append(5)
    assert l.find(10) == (10, 1)
    assert l.find(99) is None

def test_insert():
    l = mylist()
    l.append(1)
    l.append(3)
    l.insert(1, 2)
    assert l[0] == 1
    assert l[1] == 2
    assert l[2] == 3
