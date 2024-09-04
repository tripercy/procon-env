# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _board_env
else:
    import _board_env

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _board_env.delete_SwigPyIterator

    def value(self):
        return _board_env.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _board_env.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _board_env.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _board_env.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _board_env.SwigPyIterator_equal(self, x)

    def copy(self):
        return _board_env.SwigPyIterator_copy(self)

    def next(self):
        return _board_env.SwigPyIterator_next(self)

    def __next__(self):
        return _board_env.SwigPyIterator___next__(self)

    def previous(self):
        return _board_env.SwigPyIterator_previous(self)

    def advance(self, n):
        return _board_env.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _board_env.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _board_env.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _board_env.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _board_env.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _board_env.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _board_env.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _board_env:
_board_env.SwigPyIterator_swigregister(SwigPyIterator)
class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _board_env.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _board_env.IntVector___nonzero__(self)

    def __bool__(self):
        return _board_env.IntVector___bool__(self)

    def __len__(self):
        return _board_env.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _board_env.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _board_env.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _board_env.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _board_env.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _board_env.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _board_env.IntVector___setitem__(self, *args)

    def pop(self):
        return _board_env.IntVector_pop(self)

    def append(self, x):
        return _board_env.IntVector_append(self, x)

    def empty(self):
        return _board_env.IntVector_empty(self)

    def size(self):
        return _board_env.IntVector_size(self)

    def swap(self, v):
        return _board_env.IntVector_swap(self, v)

    def begin(self):
        return _board_env.IntVector_begin(self)

    def end(self):
        return _board_env.IntVector_end(self)

    def rbegin(self):
        return _board_env.IntVector_rbegin(self)

    def rend(self):
        return _board_env.IntVector_rend(self)

    def clear(self):
        return _board_env.IntVector_clear(self)

    def get_allocator(self):
        return _board_env.IntVector_get_allocator(self)

    def pop_back(self):
        return _board_env.IntVector_pop_back(self)

    def erase(self, *args):
        return _board_env.IntVector_erase(self, *args)

    def __init__(self, *args):
        _board_env.IntVector_swiginit(self, _board_env.new_IntVector(*args))

    def push_back(self, x):
        return _board_env.IntVector_push_back(self, x)

    def front(self):
        return _board_env.IntVector_front(self)

    def back(self):
        return _board_env.IntVector_back(self)

    def assign(self, n, x):
        return _board_env.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _board_env.IntVector_resize(self, *args)

    def insert(self, *args):
        return _board_env.IntVector_insert(self, *args)

    def reserve(self, n):
        return _board_env.IntVector_reserve(self, n)

    def capacity(self):
        return _board_env.IntVector_capacity(self)
    __swig_destroy__ = _board_env.delete_IntVector

# Register IntVector in _board_env:
_board_env.IntVector_swigregister(IntVector)
class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _board_env.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _board_env.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _board_env.DoubleVector___bool__(self)

    def __len__(self):
        return _board_env.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _board_env.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _board_env.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _board_env.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _board_env.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _board_env.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _board_env.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _board_env.DoubleVector_pop(self)

    def append(self, x):
        return _board_env.DoubleVector_append(self, x)

    def empty(self):
        return _board_env.DoubleVector_empty(self)

    def size(self):
        return _board_env.DoubleVector_size(self)

    def swap(self, v):
        return _board_env.DoubleVector_swap(self, v)

    def begin(self):
        return _board_env.DoubleVector_begin(self)

    def end(self):
        return _board_env.DoubleVector_end(self)

    def rbegin(self):
        return _board_env.DoubleVector_rbegin(self)

    def rend(self):
        return _board_env.DoubleVector_rend(self)

    def clear(self):
        return _board_env.DoubleVector_clear(self)

    def get_allocator(self):
        return _board_env.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _board_env.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _board_env.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _board_env.DoubleVector_swiginit(self, _board_env.new_DoubleVector(*args))

    def push_back(self, x):
        return _board_env.DoubleVector_push_back(self, x)

    def front(self):
        return _board_env.DoubleVector_front(self)

    def back(self):
        return _board_env.DoubleVector_back(self)

    def assign(self, n, x):
        return _board_env.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _board_env.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _board_env.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _board_env.DoubleVector_reserve(self, n)

    def capacity(self):
        return _board_env.DoubleVector_capacity(self)
    __swig_destroy__ = _board_env.delete_DoubleVector

# Register DoubleVector in _board_env:
_board_env.DoubleVector_swigregister(DoubleVector)
class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _board_env.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _board_env.StringVector___nonzero__(self)

    def __bool__(self):
        return _board_env.StringVector___bool__(self)

    def __len__(self):
        return _board_env.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _board_env.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _board_env.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _board_env.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _board_env.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _board_env.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _board_env.StringVector___setitem__(self, *args)

    def pop(self):
        return _board_env.StringVector_pop(self)

    def append(self, x):
        return _board_env.StringVector_append(self, x)

    def empty(self):
        return _board_env.StringVector_empty(self)

    def size(self):
        return _board_env.StringVector_size(self)

    def swap(self, v):
        return _board_env.StringVector_swap(self, v)

    def begin(self):
        return _board_env.StringVector_begin(self)

    def end(self):
        return _board_env.StringVector_end(self)

    def rbegin(self):
        return _board_env.StringVector_rbegin(self)

    def rend(self):
        return _board_env.StringVector_rend(self)

    def clear(self):
        return _board_env.StringVector_clear(self)

    def get_allocator(self):
        return _board_env.StringVector_get_allocator(self)

    def pop_back(self):
        return _board_env.StringVector_pop_back(self)

    def erase(self, *args):
        return _board_env.StringVector_erase(self, *args)

    def __init__(self, *args):
        _board_env.StringVector_swiginit(self, _board_env.new_StringVector(*args))

    def push_back(self, x):
        return _board_env.StringVector_push_back(self, x)

    def front(self):
        return _board_env.StringVector_front(self)

    def back(self):
        return _board_env.StringVector_back(self)

    def assign(self, n, x):
        return _board_env.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _board_env.StringVector_resize(self, *args)

    def insert(self, *args):
        return _board_env.StringVector_insert(self, *args)

    def reserve(self, n):
        return _board_env.StringVector_reserve(self, n)

    def capacity(self):
        return _board_env.StringVector_capacity(self)
    __swig_destroy__ = _board_env.delete_StringVector

# Register StringVector in _board_env:
_board_env.StringVector_swigregister(StringVector)
class DieVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _board_env.DieVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _board_env.DieVector___nonzero__(self)

    def __bool__(self):
        return _board_env.DieVector___bool__(self)

    def __len__(self):
        return _board_env.DieVector___len__(self)

    def __getslice__(self, i, j):
        return _board_env.DieVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _board_env.DieVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _board_env.DieVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _board_env.DieVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _board_env.DieVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _board_env.DieVector___setitem__(self, *args)

    def pop(self):
        return _board_env.DieVector_pop(self)

    def append(self, x):
        return _board_env.DieVector_append(self, x)

    def empty(self):
        return _board_env.DieVector_empty(self)

    def size(self):
        return _board_env.DieVector_size(self)

    def swap(self, v):
        return _board_env.DieVector_swap(self, v)

    def begin(self):
        return _board_env.DieVector_begin(self)

    def end(self):
        return _board_env.DieVector_end(self)

    def rbegin(self):
        return _board_env.DieVector_rbegin(self)

    def rend(self):
        return _board_env.DieVector_rend(self)

    def clear(self):
        return _board_env.DieVector_clear(self)

    def get_allocator(self):
        return _board_env.DieVector_get_allocator(self)

    def pop_back(self):
        return _board_env.DieVector_pop_back(self)

    def erase(self, *args):
        return _board_env.DieVector_erase(self, *args)

    def __init__(self, *args):
        _board_env.DieVector_swiginit(self, _board_env.new_DieVector(*args))

    def push_back(self, x):
        return _board_env.DieVector_push_back(self, x)

    def front(self):
        return _board_env.DieVector_front(self)

    def back(self):
        return _board_env.DieVector_back(self)

    def assign(self, n, x):
        return _board_env.DieVector_assign(self, n, x)

    def resize(self, *args):
        return _board_env.DieVector_resize(self, *args)

    def insert(self, *args):
        return _board_env.DieVector_insert(self, *args)

    def reserve(self, n):
        return _board_env.DieVector_reserve(self, n)

    def capacity(self):
        return _board_env.DieVector_capacity(self)
    __swig_destroy__ = _board_env.delete_DieVector

# Register DieVector in _board_env:
_board_env.DieVector_swigregister(DieVector)
class Die(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _board_env.Die_swiginit(self, _board_env.new_Die(*args))

    def at(self, x, y):
        return _board_env.Die_at(self, x, y)
    __swig_destroy__ = _board_env.delete_Die

# Register Die in _board_env:
_board_env.Die_swigregister(Die)
class Board(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _board_env.Board_swiginit(self, _board_env.new_Board(*args))

    def at(self, x, y):
        return _board_env.Board_at(self, x, y)
    __swig_destroy__ = _board_env.delete_Board

# Register Board in _board_env:
_board_env.Board_swigregister(Board)
class Game(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, initBoardStr, targetStr, w, h, generalDies):
        _board_env.Game_swiginit(self, _board_env.new_Game(initBoardStr, targetStr, w, h, generalDies))

    def cutDie(self, dieIndex, x, y):
        return _board_env.Game_cutDie(self, dieIndex, x, y)

    def getReward(self):
        return _board_env.Game_getReward(self)

    def getDies(self):
        return _board_env.Game_getDies(self)

    def getInitBoard(self):
        return _board_env.Game_getInitBoard(self)

    def getTargetBoard(self):
        return _board_env.Game_getTargetBoard(self)
    __swig_destroy__ = _board_env.delete_Game

# Register Game in _board_env:
_board_env.Game_swigregister(Game)

