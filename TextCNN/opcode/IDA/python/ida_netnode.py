# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: netnode
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_netnode', [dirname(__file__)])
        except ImportError:
            import _ida_netnode
            return _ida_netnode
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_netnode', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_netnode = swig_import_helper()
    del swig_import_helper
else:
    import _ida_netnode
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

BADNODE = _ida_netnode.BADNODE
"""
A number to represent a bad netnode reference.
"""
class netnode(object):
    """
    Proxy of C++ netnode class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> netnode
        __init__(self, num) -> netnode
        __init__(self, _name, namlen=0, do_create=False) -> netnode
        """
        this = _ida_netnode.new_netnode(*args)
        try: self.this.append(this)
        except: self.this = this
    def create(self, *args):
        """
        create(self, _name, namlen=0) -> bool
        create(self) -> bool
        """
        return _ida_netnode.netnode_create(self, *args)

    def kill(self, *args):
        """
        kill(self)
        """
        return _ida_netnode.netnode_kill(self, *args)

    def get_name(self, *args):
        """
        get_name(self) -> ssize_t
        """
        return _ida_netnode.netnode_get_name(self, *args)

    def rename(self, *args):
        """
        rename(self, newname, namlen=0) -> bool
        """
        return _ida_netnode.netnode_rename(self, *args)

    def valobj(self, *args):
        """
        valobj(self) -> ssize_t
        """
        return _ida_netnode.netnode_valobj(self, *args)

    def valstr(self, *args):
        """
        valstr(self) -> ssize_t
        """
        return _ida_netnode.netnode_valstr(self, *args)

    def set(self, *args):
        """
        set(self, value) -> bool
        """
        return _ida_netnode.netnode_set(self, *args)

    def delvalue(self, *args):
        """
        delvalue(self) -> bool
        """
        return _ida_netnode.netnode_delvalue(self, *args)

    def set_long(self, *args):
        """
        set_long(self, x) -> bool
        """
        return _ida_netnode.netnode_set_long(self, *args)

    def value_exists(self, *args):
        """
        value_exists(self) -> bool
        """
        return _ida_netnode.netnode_value_exists(self, *args)

    def long_value(self, *args):
        """
        long_value(self) -> nodeidx_t
        """
        return _ida_netnode.netnode_long_value(self, *args)

    def altval(self, *args):
        """
        altval(self, alt, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altval(self, *args)

    def altval_ea(self, *args):
        """
        altval_ea(self, ea, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altval_ea(self, *args)

    def altset(self, *args):
        """
        altset(self, alt, value, tag=atag) -> bool
        """
        return _ida_netnode.netnode_altset(self, *args)

    def altset_ea(self, *args):
        """
        altset_ea(self, ea, value, tag=atag) -> bool
        """
        return _ida_netnode.netnode_altset_ea(self, *args)

    def altdel_ea(self, *args):
        """
        altdel_ea(self, ea, tag=atag) -> bool
        """
        return _ida_netnode.netnode_altdel_ea(self, *args)

    def easet(self, *args):
        """
        easet(self, ea, addr, tag) -> bool
        """
        return _ida_netnode.netnode_easet(self, *args)

    def eaget(self, *args):
        """
        eaget(self, ea, tag) -> ea_t
        """
        return _ida_netnode.netnode_eaget(self, *args)

    def eadel(self, *args):
        """
        eadel(self, ea, tag) -> bool
        """
        return _ida_netnode.netnode_eadel(self, *args)

    def easet_idx(self, *args):
        """
        easet_idx(self, idx, addr, tag) -> bool
        """
        return _ida_netnode.netnode_easet_idx(self, *args)

    def eaget_idx(self, *args):
        """
        eaget_idx(self, idx, tag) -> ea_t
        """
        return _ida_netnode.netnode_eaget_idx(self, *args)

    def easet_idx8(self, *args):
        """
        easet_idx8(self, idx, addr, tag) -> bool
        """
        return _ida_netnode.netnode_easet_idx8(self, *args)

    def eaget_idx8(self, *args):
        """
        eaget_idx8(self, idx, tag) -> ea_t
        """
        return _ida_netnode.netnode_eaget_idx8(self, *args)

    def eadel_idx8(self, *args):
        """
        eadel_idx8(self, idx, tag) -> bool
        """
        return _ida_netnode.netnode_eadel_idx8(self, *args)

    def altfirst(self, *args):
        """
        altfirst(self, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altfirst(self, *args)

    def altnext(self, *args):
        """
        altnext(self, cur, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altnext(self, *args)

    def altlast(self, *args):
        """
        altlast(self, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altlast(self, *args)

    def altprev(self, *args):
        """
        altprev(self, cur, tag=atag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altprev(self, *args)

    def altshift(self, *args):
        """
        altshift(self, _from, to, size, tag=atag) -> size_t
        """
        return _ida_netnode.netnode_altshift(self, *args)

    def charval(self, *args):
        """
        charval(self, alt, tag) -> uchar
        """
        return _ida_netnode.netnode_charval(self, *args)

    def charset(self, *args):
        """
        charset(self, alt, val, tag) -> bool
        """
        return _ida_netnode.netnode_charset(self, *args)

    def chardel(self, *args):
        """
        chardel(self, alt, tag) -> bool
        """
        return _ida_netnode.netnode_chardel(self, *args)

    def charval_ea(self, *args):
        """
        charval_ea(self, ea, tag) -> uchar
        """
        return _ida_netnode.netnode_charval_ea(self, *args)

    def charset_ea(self, *args):
        """
        charset_ea(self, ea, val, tag) -> bool
        """
        return _ida_netnode.netnode_charset_ea(self, *args)

    def chardel_ea(self, *args):
        """
        chardel_ea(self, ea, tag) -> bool
        """
        return _ida_netnode.netnode_chardel_ea(self, *args)

    def charfirst(self, *args):
        """
        charfirst(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charfirst(self, *args)

    def charnext(self, *args):
        """
        charnext(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charnext(self, *args)

    def charlast(self, *args):
        """
        charlast(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charlast(self, *args)

    def charprev(self, *args):
        """
        charprev(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charprev(self, *args)

    def charshift(self, *args):
        """
        charshift(self, _from, to, size, tag) -> size_t
        """
        return _ida_netnode.netnode_charshift(self, *args)

    def altval_idx8(self, *args):
        """
        altval_idx8(self, alt, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altval_idx8(self, *args)

    def altset_idx8(self, *args):
        """
        altset_idx8(self, alt, val, tag) -> bool
        """
        return _ida_netnode.netnode_altset_idx8(self, *args)

    def altdel_idx8(self, *args):
        """
        altdel_idx8(self, alt, tag) -> bool
        """
        return _ida_netnode.netnode_altdel_idx8(self, *args)

    def altfirst_idx8(self, *args):
        """
        altfirst_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altfirst_idx8(self, *args)

    def altnext_idx8(self, *args):
        """
        altnext_idx8(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altnext_idx8(self, *args)

    def altlast_idx8(self, *args):
        """
        altlast_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altlast_idx8(self, *args)

    def altprev_idx8(self, *args):
        """
        altprev_idx8(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_altprev_idx8(self, *args)

    def charval_idx8(self, *args):
        """
        charval_idx8(self, alt, tag) -> uchar
        """
        return _ida_netnode.netnode_charval_idx8(self, *args)

    def charset_idx8(self, *args):
        """
        charset_idx8(self, alt, val, tag) -> bool
        """
        return _ida_netnode.netnode_charset_idx8(self, *args)

    def chardel_idx8(self, *args):
        """
        chardel_idx8(self, alt, tag) -> bool
        """
        return _ida_netnode.netnode_chardel_idx8(self, *args)

    def charfirst_idx8(self, *args):
        """
        charfirst_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charfirst_idx8(self, *args)

    def charnext_idx8(self, *args):
        """
        charnext_idx8(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charnext_idx8(self, *args)

    def charlast_idx8(self, *args):
        """
        charlast_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charlast_idx8(self, *args)

    def charprev_idx8(self, *args):
        """
        charprev_idx8(self, cur, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_charprev_idx8(self, *args)

    def altdel(self, *args):
        """
        altdel(self, alt, tag=atag) -> bool
        altdel(self) -> bool
        """
        return _ida_netnode.netnode_altdel(self, *args)

    def altdel_all(self, *args):
        """
        altdel_all(self, tag) -> bool
        """
        return _ida_netnode.netnode_altdel_all(self, *args)

    def supval(self, *args):
        """
        supval(self, alt, tag=stag) -> ssize_t
        """
        return _ida_netnode.netnode_supval(self, *args)

    def supval_ea(self, *args):
        """
        supval_ea(self, ea, tag=stag) -> ssize_t
        """
        return _ida_netnode.netnode_supval_ea(self, *args)

    def supstr(self, *args):
        """
        supstr(self, alt, tag=stag) -> ssize_t
        """
        return _ida_netnode.netnode_supstr(self, *args)

    def supstr_ea(self, *args):
        """
        supstr_ea(self, ea, tag=stag) -> ssize_t
        """
        return _ida_netnode.netnode_supstr_ea(self, *args)

    def supset(self, *args):
        """
        supset(self, alt, value, tag=stag) -> bool
        """
        return _ida_netnode.netnode_supset(self, *args)

    def supset_ea(self, *args):
        """
        supset_ea(self, ea, value, tag=stag) -> bool
        """
        return _ida_netnode.netnode_supset_ea(self, *args)

    def supdel_ea(self, *args):
        """
        supdel_ea(self, ea, tag=stag) -> bool
        """
        return _ida_netnode.netnode_supdel_ea(self, *args)

    def lower_bound(self, *args):
        """
        lower_bound(self, cur, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_lower_bound(self, *args)

    def lower_bound_ea(self, *args):
        """
        lower_bound_ea(self, ea, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_lower_bound_ea(self, *args)

    def supfirst(self, *args):
        """
        supfirst(self, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supfirst(self, *args)

    def supnext(self, *args):
        """
        supnext(self, cur, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supnext(self, *args)

    def suplast(self, *args):
        """
        suplast(self, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_suplast(self, *args)

    def supprev(self, *args):
        """
        supprev(self, cur, tag=stag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supprev(self, *args)

    def supshift(self, *args):
        """
        supshift(self, _from, to, size, tag=stag) -> size_t
        """
        return _ida_netnode.netnode_supshift(self, *args)

    def supval_idx8(self, *args):
        """
        supval_idx8(self, alt, tag) -> ssize_t
        """
        return _ida_netnode.netnode_supval_idx8(self, *args)

    def supstr_idx8(self, *args):
        """
        supstr_idx8(self, alt, tag) -> ssize_t
        """
        return _ida_netnode.netnode_supstr_idx8(self, *args)

    def supset_idx8(self, *args):
        """
        supset_idx8(self, alt, value, tag) -> bool
        """
        return _ida_netnode.netnode_supset_idx8(self, *args)

    def supdel_idx8(self, *args):
        """
        supdel_idx8(self, alt, tag) -> bool
        """
        return _ida_netnode.netnode_supdel_idx8(self, *args)

    def lower_bound_idx8(self, *args):
        """
        lower_bound_idx8(self, alt, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_lower_bound_idx8(self, *args)

    def supfirst_idx8(self, *args):
        """
        supfirst_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supfirst_idx8(self, *args)

    def supnext_idx8(self, *args):
        """
        supnext_idx8(self, alt, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supnext_idx8(self, *args)

    def suplast_idx8(self, *args):
        """
        suplast_idx8(self, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_suplast_idx8(self, *args)

    def supprev_idx8(self, *args):
        """
        supprev_idx8(self, alt, tag) -> nodeidx_t
        """
        return _ida_netnode.netnode_supprev_idx8(self, *args)

    def supdel(self, *args):
        """
        supdel(self, alt, tag=stag) -> bool
        supdel(self) -> bool
        """
        return _ida_netnode.netnode_supdel(self, *args)

    def supdel_all(self, *args):
        """
        supdel_all(self, tag) -> bool
        """
        return _ida_netnode.netnode_supdel_all(self, *args)

    def supdel_range(self, *args):
        """
        supdel_range(self, idx1, idx2, tag) -> int
        """
        return _ida_netnode.netnode_supdel_range(self, *args)

    def supdel_range_idx8(self, *args):
        """
        supdel_range_idx8(self, idx1, idx2, tag) -> int
        """
        return _ida_netnode.netnode_supdel_range_idx8(self, *args)

    def hashval(self, *args):
        """
        hashval(self, idx, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashval(self, *args)

    def hashstr(self, *args):
        """
        hashstr(self, idx, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashstr(self, *args)

    def hashval_long(self, *args):
        """
        hashval_long(self, idx, tag=htag) -> nodeidx_t
        """
        return _ida_netnode.netnode_hashval_long(self, *args)

    def hashset(self, *args):
        """
        hashset(self, idx, value, tag=htag) -> bool
        """
        return _ida_netnode.netnode_hashset(self, *args)

    def hashset_idx(self, *args):
        """
        hashset_idx(self, idx, value, tag=htag) -> bool
        """
        return _ida_netnode.netnode_hashset_idx(self, *args)

    def hashdel(self, *args):
        """
        hashdel(self, idx, tag=htag) -> bool
        """
        return _ida_netnode.netnode_hashdel(self, *args)

    def hashfirst(self, *args):
        """
        hashfirst(self, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashfirst(self, *args)

    def hashnext(self, *args):
        """
        hashnext(self, idx, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashnext(self, *args)

    def hashlast(self, *args):
        """
        hashlast(self, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashlast(self, *args)

    def hashprev(self, *args):
        """
        hashprev(self, idx, tag=htag) -> ssize_t
        """
        return _ida_netnode.netnode_hashprev(self, *args)

    def hashdel_all(self, *args):
        """
        hashdel_all(self, tag=htag) -> bool
        """
        return _ida_netnode.netnode_hashdel_all(self, *args)

    def blobsize(self, *args):
        """
        blobsize(self, _start, tag) -> size_t
        """
        return _ida_netnode.netnode_blobsize(self, *args)

    def blobsize_ea(self, *args):
        """
        blobsize_ea(self, ea, tag) -> size_t
        """
        return _ida_netnode.netnode_blobsize_ea(self, *args)

    def setblob(self, *args):
        """
        setblob(self, buf, _start, tag) -> bool
        """
        return _ida_netnode.netnode_setblob(self, *args)

    def setblob_ea(self, *args):
        """
        setblob_ea(self, buf, ea, tag) -> bool
        """
        return _ida_netnode.netnode_setblob_ea(self, *args)

    def delblob(self, *args):
        """
        delblob(self, _start, tag) -> int
        """
        return _ida_netnode.netnode_delblob(self, *args)

    def delblob_ea(self, *args):
        """
        delblob_ea(self, ea, tag) -> int
        """
        return _ida_netnode.netnode_delblob_ea(self, *args)

    def start(self, *args):
        """
        start(self) -> bool
        """
        return _ida_netnode.netnode_start(self, *args)

    def end(self, *args):
        """
        end(self) -> bool
        """
        return _ida_netnode.netnode_end(self, *args)

    def next(self, *args):
        """
        next(self) -> bool
        """
        return _ida_netnode.netnode_next(self, *args)

    def prev(self, *args):
        """
        prev(self) -> bool
        """
        return _ida_netnode.netnode_prev(self, *args)

    def copyto(self, *args):
        """
        copyto(self, target, count=1) -> size_t
        """
        return _ida_netnode.netnode_copyto(self, *args)

    def moveto(self, *args):
        """
        moveto(self, target, count=1) -> size_t
        """
        return _ida_netnode.netnode_moveto(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, n) -> bool
        __eq__(self, x) -> bool
        """
        return _ida_netnode.netnode___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, n) -> bool
        __ne__(self, x) -> bool
        """
        return _ida_netnode.netnode___ne__(self, *args)

    def index(self, *args):
        """
        index(self) -> nodeidx_t
        """
        return _ida_netnode.netnode_index(self, *args)

    def getblob(self, *args):
        """
        getblob(self, start, tag) -> PyObject *
        """
        return _ida_netnode.netnode_getblob(self, *args)

    def getclob(self, *args):
        """
        getclob(self, start, tag) -> PyObject *
        """
        return _ida_netnode.netnode_getclob(self, *args)

    def getblob_ea(self, *args):
        """
        getblob_ea(self, ea, tag) -> PyObject *
        """
        return _ida_netnode.netnode_getblob_ea(self, *args)

    def hashstr_buf(self, *args):
        """
        hashstr_buf(self, idx, tag=htag) -> PyObject *
        """
        return _ida_netnode.netnode_hashstr_buf(self, *args)

    def hashset_buf(self, *args):
        """
        hashset_buf(self, idx, py_str, tag=htag) -> bool
        """
        return _ida_netnode.netnode_hashset_buf(self, *args)

    __swig_destroy__ = _ida_netnode.delete_netnode
    __del__ = lambda self : None;
netnode_swigregister = _ida_netnode.netnode_swigregister
netnode_swigregister(netnode)
cvar = _ida_netnode.cvar
MAXNAMESIZE = cvar.MAXNAMESIZE
MAX_NODENAME_SIZE = cvar.MAX_NODENAME_SIZE
MAXSPECSIZE = cvar.MAXSPECSIZE
atag = cvar.atag
stag = cvar.stag
htag = cvar.htag
vtag = cvar.vtag
ntag = cvar.ntag
ltag = cvar.ltag
NETMAP_IDX = cvar.NETMAP_IDX
NETMAP_VAL = cvar.NETMAP_VAL
NETMAP_STR = cvar.NETMAP_STR

def exist(*args):
  """
  exist(n) -> bool
  """
  return _ida_netnode.exist(*args)

if _BC695:
    netnode.alt1st       = netnode.altfirst
    netnode.alt1st_idx8  = netnode.altfirst_idx8
    netnode.altnxt       = netnode.altnext
    netnode.char1st      = netnode.charfirst
    netnode.char1st_idx8 = netnode.charfirst_idx8
    netnode.charnxt      = netnode.charnext
    netnode.hash1st      = netnode.hashfirst
    netnode.hashnxt      = netnode.hashnext
    netnode.sup1st       = netnode.supfirst
    netnode.sup1st_idx8  = netnode.supfirst_idx8
    netnode.supnxt       = netnode.supnext



