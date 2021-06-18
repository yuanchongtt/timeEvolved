# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: range
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_range', [dirname(__file__)])
        except ImportError:
            import _ida_range
            return _ida_range
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_range', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_range = swig_import_helper()
    del swig_import_helper
else:
    import _ida_range
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class rangevec_base_t(object):
    """
    Proxy of C++ qvector<(range_t)> class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> rangevec_base_t
        __init__(self, x) -> rangevec_base_t
        """
        this = _ida_range.new_rangevec_base_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_range.delete_rangevec_base_t
    __del__ = lambda self : None;
    def push_back(self, *args):
        """
        push_back(self, x)
        push_back(self) -> range_t
        """
        return _ida_range.rangevec_base_t_push_back(self, *args)

    def pop_back(self, *args):
        """
        pop_back(self)
        """
        return _ida_range.rangevec_base_t_pop_back(self, *args)

    def size(self, *args):
        """
        size(self) -> size_t
        """
        return _ida_range.rangevec_base_t_size(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_range.rangevec_base_t_empty(self, *args)

    def at(self, *args):
        """
        at(self, _idx) -> range_t
        """
        return _ida_range.rangevec_base_t_at(self, *args)

    def qclear(self, *args):
        """
        qclear(self)
        """
        return _ida_range.rangevec_base_t_qclear(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_range.rangevec_base_t_clear(self, *args)

    def resize(self, *args):
        """
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_range.rangevec_base_t_resize(self, *args)

    def grow(self, *args):
        """
        grow(self, x=range_t())
        """
        return _ida_range.rangevec_base_t_grow(self, *args)

    def capacity(self, *args):
        """
        capacity(self) -> size_t
        """
        return _ida_range.rangevec_base_t_capacity(self, *args)

    def reserve(self, *args):
        """
        reserve(self, cnt)
        """
        return _ida_range.rangevec_base_t_reserve(self, *args)

    def truncate(self, *args):
        """
        truncate(self)
        """
        return _ida_range.rangevec_base_t_truncate(self, *args)

    def swap(self, *args):
        """
        swap(self, r)
        """
        return _ida_range.rangevec_base_t_swap(self, *args)

    def extract(self, *args):
        """
        extract(self) -> range_t
        """
        return _ida_range.rangevec_base_t_extract(self, *args)

    def inject(self, *args):
        """
        inject(self, s, len)
        """
        return _ida_range.rangevec_base_t_inject(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_range.rangevec_base_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_range.rangevec_base_t___ne__(self, *args)

    def begin(self, *args):
        """
        begin(self) -> range_t
        begin(self) -> range_t
        """
        return _ida_range.rangevec_base_t_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> range_t
        end(self) -> range_t
        """
        return _ida_range.rangevec_base_t_end(self, *args)

    def insert(self, *args):
        """
        insert(self, it, x) -> range_t
        """
        return _ida_range.rangevec_base_t_insert(self, *args)

    def erase(self, *args):
        """
        erase(self, it) -> range_t
        erase(self, first, last) -> range_t
        """
        return _ida_range.rangevec_base_t_erase(self, *args)

    def find(self, *args):
        """
        find(self, x) -> range_t
        find(self, x) -> range_t
        """
        return _ida_range.rangevec_base_t_find(self, *args)

    def has(self, *args):
        """
        has(self, x) -> bool
        """
        return _ida_range.rangevec_base_t_has(self, *args)

    def add_unique(self, *args):
        """
        add_unique(self, x) -> bool
        """
        return _ida_range.rangevec_base_t_add_unique(self, *args)

    def _del(self, *args):
        """
        _del(self, x) -> bool
        """
        return _ida_range.rangevec_base_t__del(self, *args)

    def __len__(self, *args):
        """
        __len__(self) -> size_t
        """
        return _ida_range.rangevec_base_t___len__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, i) -> range_t
        """
        return _ida_range.rangevec_base_t___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, i, v)
        """
        return _ida_range.rangevec_base_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

rangevec_base_t_swigregister = _ida_range.rangevec_base_t_swigregister
rangevec_base_t_swigregister(rangevec_base_t)

class array_of_rangesets(object):
    """
    Proxy of C++ qvector<(rangeset_t)> class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> array_of_rangesets
        __init__(self, x) -> array_of_rangesets
        """
        this = _ida_range.new_array_of_rangesets(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_range.delete_array_of_rangesets
    __del__ = lambda self : None;
    def push_back(self, *args):
        """
        push_back(self, x)
        push_back(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_push_back(self, *args)

    def pop_back(self, *args):
        """
        pop_back(self)
        """
        return _ida_range.array_of_rangesets_pop_back(self, *args)

    def size(self, *args):
        """
        size(self) -> size_t
        """
        return _ida_range.array_of_rangesets_size(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_range.array_of_rangesets_empty(self, *args)

    def at(self, *args):
        """
        at(self, _idx) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_at(self, *args)

    def qclear(self, *args):
        """
        qclear(self)
        """
        return _ida_range.array_of_rangesets_qclear(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_range.array_of_rangesets_clear(self, *args)

    def resize(self, *args):
        """
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_range.array_of_rangesets_resize(self, *args)

    def grow(self, *args):
        """
        grow(self, x=rangeset_t())
        """
        return _ida_range.array_of_rangesets_grow(self, *args)

    def capacity(self, *args):
        """
        capacity(self) -> size_t
        """
        return _ida_range.array_of_rangesets_capacity(self, *args)

    def reserve(self, *args):
        """
        reserve(self, cnt)
        """
        return _ida_range.array_of_rangesets_reserve(self, *args)

    def truncate(self, *args):
        """
        truncate(self)
        """
        return _ida_range.array_of_rangesets_truncate(self, *args)

    def swap(self, *args):
        """
        swap(self, r)
        """
        return _ida_range.array_of_rangesets_swap(self, *args)

    def extract(self, *args):
        """
        extract(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_extract(self, *args)

    def inject(self, *args):
        """
        inject(self, s, len)
        """
        return _ida_range.array_of_rangesets_inject(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_range.array_of_rangesets___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_range.array_of_rangesets___ne__(self, *args)

    def begin(self, *args):
        """
        begin(self) -> rangeset_t
        begin(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> rangeset_t
        end(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_end(self, *args)

    def insert(self, *args):
        """
        insert(self, it, x) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_insert(self, *args)

    def erase(self, *args):
        """
        erase(self, it) -> rangeset_t
        erase(self, first, last) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_erase(self, *args)

    def find(self, *args):
        """
        find(self, x) -> rangeset_t
        find(self, x) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_find(self, *args)

    def has(self, *args):
        """
        has(self, x) -> bool
        """
        return _ida_range.array_of_rangesets_has(self, *args)

    def add_unique(self, *args):
        """
        add_unique(self, x) -> bool
        """
        return _ida_range.array_of_rangesets_add_unique(self, *args)

    def _del(self, *args):
        """
        _del(self, x) -> bool
        """
        return _ida_range.array_of_rangesets__del(self, *args)

    def __len__(self, *args):
        """
        __len__(self) -> size_t
        """
        return _ida_range.array_of_rangesets___len__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, i) -> rangeset_t
        """
        return _ida_range.array_of_rangesets___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, i, v)
        """
        return _ida_range.array_of_rangesets___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

array_of_rangesets_swigregister = _ida_range.array_of_rangesets_swigregister
array_of_rangesets_swigregister(array_of_rangesets)

class range_t(object):
    """
    Proxy of C++ range_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    start_ea = _swig_property(_ida_range.range_t_start_ea_get, _ida_range.range_t_start_ea_set)
    end_ea = _swig_property(_ida_range.range_t_end_ea_get, _ida_range.range_t_end_ea_set)
    def __init__(self, *args):
        """
        __init__(self) -> range_t
        __init__(self, ea1, ea2) -> range_t
        """
        this = _ida_range.new_range_t(*args)
        try: self.this.append(this)
        except: self.this = this
    def compare(self, *args):
        """
        compare(self, r) -> int
        """
        return _ida_range.range_t_compare(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_range.range_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_range.range_t___ne__(self, *args)

    def __gt__(self, *args):
        """
        __gt__(self, r) -> bool
        """
        return _ida_range.range_t___gt__(self, *args)

    def __lt__(self, *args):
        """
        __lt__(self, r) -> bool
        """
        return _ida_range.range_t___lt__(self, *args)

    def contains(self, *args):
        """
        contains(self, ea) -> bool
        contains(self, r) -> bool
        """
        return _ida_range.range_t_contains(self, *args)

    def overlaps(self, *args):
        """
        overlaps(self, r) -> bool
        """
        return _ida_range.range_t_overlaps(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_range.range_t_clear(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_range.range_t_empty(self, *args)

    def size(self, *args):
        """
        size(self) -> asize_t
        """
        return _ida_range.range_t_size(self, *args)

    def intersect(self, *args):
        """
        intersect(self, r)
        """
        return _ida_range.range_t_intersect(self, *args)

    def extend(self, *args):
        """
        extend(self, ea)
        """
        return _ida_range.range_t_extend(self, *args)

    def _print(self, *args):
        """
        _print(self) -> size_t
        """
        return _ida_range.range_t__print(self, *args)

    __swig_destroy__ = _ida_range.delete_range_t
    __del__ = lambda self : None;
range_t_swigregister = _ida_range.range_t_swigregister
range_t_swigregister(range_t)

def range_t_print(*args):
  """
  range_t_print(cb) -> size_t


  Helper function. Should not be called directly!
  """
  return _ida_range.range_t_print(*args)

class rangevec_t(rangevec_base_t):
    """
    Proxy of C++ rangevec_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> rangevec_t
        """
        this = _ida_range.new_rangevec_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_range.delete_rangevec_t
    __del__ = lambda self : None;
rangevec_t_swigregister = _ida_range.rangevec_t_swigregister
rangevec_t_swigregister(rangevec_t)

RANGE_KIND_UNKNOWN = _ida_range.RANGE_KIND_UNKNOWN
RANGE_KIND_FUNC = _ida_range.RANGE_KIND_FUNC
RANGE_KIND_SEGMENT = _ida_range.RANGE_KIND_SEGMENT
RANGE_KIND_HIDDEN_RANGE = _ida_range.RANGE_KIND_HIDDEN_RANGE
class rangeset_t(object):
    """
    Proxy of C++ rangeset_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> rangeset_t
        __init__(self, range) -> rangeset_t
        __init__(self, ivs) -> rangeset_t
        """
        this = _ida_range.new_rangeset_t(*args)
        try: self.this.append(this)
        except: self.this = this
    def swap(self, *args):
        """
        swap(self, r)
        """
        return _ida_range.rangeset_t_swap(self, *args)

    def add(self, *args):
        """
        add(self, range) -> bool
        add(self, start, _end) -> bool
        add(self, aset) -> bool
        """
        return _ida_range.rangeset_t_add(self, *args)

    def sub(self, *args):
        """
        sub(self, range) -> bool
        sub(self, ea) -> bool
        sub(self, aset) -> bool
        """
        return _ida_range.rangeset_t_sub(self, *args)

    def includes(self, *args):
        """
        includes(self, range) -> bool
        """
        return _ida_range.rangeset_t_includes(self, *args)

    def _print(self, *args):
        """
        _print(self) -> size_t
        """
        return _ida_range.rangeset_t__print(self, *args)

    def getrange(self, *args):
        """
        getrange(self, idx) -> range_t
        """
        return _ida_range.rangeset_t_getrange(self, *args)

    def lastrange(self, *args):
        """
        lastrange(self) -> range_t
        """
        return _ida_range.rangeset_t_lastrange(self, *args)

    def nranges(self, *args):
        """
        nranges(self) -> size_t
        """
        return _ida_range.rangeset_t_nranges(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_range.rangeset_t_empty(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_range.rangeset_t_clear(self, *args)

    def has_common(self, *args):
        """
        has_common(self, range) -> bool
        has_common(self, aset) -> bool
        """
        return _ida_range.rangeset_t_has_common(self, *args)

    def contains(self, *args):
        """
        contains(self, ea) -> bool
        contains(self, aset) -> bool
        """
        return _ida_range.rangeset_t_contains(self, *args)

    def intersect(self, *args):
        """
        intersect(self, aset) -> bool
        """
        return _ida_range.rangeset_t_intersect(self, *args)

    def is_subset_of(self, *args):
        """
        is_subset_of(self, aset) -> bool
        """
        return _ida_range.rangeset_t_is_subset_of(self, *args)

    def is_equal(self, *args):
        """
        is_equal(self, aset) -> bool
        """
        return _ida_range.rangeset_t_is_equal(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, aset) -> bool
        """
        return _ida_range.rangeset_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, aset) -> bool
        """
        return _ida_range.rangeset_t___ne__(self, *args)

    def begin(self, *args):
        """
        begin(self) -> range_t
        begin(self) -> range_t
        """
        return _ida_range.rangeset_t_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> range_t
        end(self) -> range_t
        """
        return _ida_range.rangeset_t_end(self, *args)

    def find_range(self, *args):
        """
        find_range(self, ea) -> range_t
        """
        return _ida_range.rangeset_t_find_range(self, *args)

    def cached_range(self, *args):
        """
        cached_range(self) -> range_t
        """
        return _ida_range.rangeset_t_cached_range(self, *args)

    def next_addr(self, *args):
        """
        next_addr(self, ea) -> ea_t
        """
        return _ida_range.rangeset_t_next_addr(self, *args)

    def prev_addr(self, *args):
        """
        prev_addr(self, ea) -> ea_t
        """
        return _ida_range.rangeset_t_prev_addr(self, *args)

    def next_range(self, *args):
        """
        next_range(self, ea) -> ea_t
        """
        return _ida_range.rangeset_t_next_range(self, *args)

    def prev_range(self, *args):
        """
        prev_range(self, ea) -> ea_t
        """
        return _ida_range.rangeset_t_prev_range(self, *args)

    def __getitem__(self, idx):
        return self.getrange(idx)

    import ida_idaapi
    __len__ = nranges
    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_range.delete_rangeset_t
    __del__ = lambda self : None;
rangeset_t_swigregister = _ida_range.rangeset_t_swigregister
rangeset_t_swigregister(rangeset_t)

if _BC695:
    import sys
    sys.modules["ida_area"] = sys.modules["ida_range"]
    area_t = range_t
    areaset_t = rangeset_t
    def __set_startEA(inst, v):
        inst.start_ea = v
    range_t.startEA = property(lambda self: self.start_ea, __set_startEA)
    def __set_endEA(inst, v):
        inst.end_ea = v
    range_t.endEA = property(lambda self: self.end_ea, __set_endEA)



