# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: xref
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_xref', [dirname(__file__)])
        except ImportError:
            import _ida_xref
            return _ida_xref
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_xref', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_xref = swig_import_helper()
    del swig_import_helper
else:
    import _ida_xref
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


def create_switch_xrefs(*args):
  """
  create_switch_xrefs(ea, si) -> bool


  This function creates xrefs from the indirect jump.
  
  Usually there is no need to call this function directly because the kernel
  will call it for switch tables
  
  Note: Custom switch information are not supported yet.
  
  @param ea: address of the 'indirect jump' instruction
  @param si: switch information
  
  @return: Boolean
  """
  return _ida_xref.create_switch_xrefs(*args)
class cases_and_targets_t(object):
    """
    Proxy of C++ cases_and_targets_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    cases = _swig_property(_ida_xref.cases_and_targets_t_cases_get, _ida_xref.cases_and_targets_t_cases_set)
    targets = _swig_property(_ida_xref.cases_and_targets_t_targets_get, _ida_xref.cases_and_targets_t_targets_set)
    def __init__(self, *args):
        """
        __init__(self) -> cases_and_targets_t
        """
        this = _ida_xref.new_cases_and_targets_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_xref.delete_cases_and_targets_t
    __del__ = lambda self : None;
cases_and_targets_t_swigregister = _ida_xref.cases_and_targets_t_swigregister
cases_and_targets_t_swigregister(cases_and_targets_t)


def calc_switch_cases(*args):
  """
  calc_switch_cases(ea, si) -> cases_and_targets_t


  Get information about a switch's cases.
  
  The returned information can be used as follows:
  
      for idx in xrange(len(results.cases)):
          cur_case = results.cases[idx]
          for cidx in xrange(len(cur_case)):
              print "case: %d" % cur_case[cidx]
          print "  goto 0x%x" % results.targets[idx]
  
  @param ea: address of the 'indirect jump' instruction
  @param si: switch information
  
  @return: a structure with 2 members: 'cases', and 'targets'.
  """
  return _ida_xref.calc_switch_cases(*args)

def create_switch_table(*args):
  """
  create_switch_table(ea, si) -> bool


  Create switch table from the switch information
  
  @param ea: address of the 'indirect jump' instruction
  @param si: switch information
  
  @return: Boolean
  """
  return _ida_xref.create_switch_table(*args)
fl_U = _ida_xref.fl_U
fl_CF = _ida_xref.fl_CF
fl_CN = _ida_xref.fl_CN
fl_JF = _ida_xref.fl_JF
fl_JN = _ida_xref.fl_JN
fl_USobsolete = _ida_xref.fl_USobsolete
fl_F = _ida_xref.fl_F
dr_U = _ida_xref.dr_U
dr_O = _ida_xref.dr_O
dr_W = _ida_xref.dr_W
dr_R = _ida_xref.dr_R
dr_T = _ida_xref.dr_T
dr_I = _ida_xref.dr_I
XREF_USER = _ida_xref.XREF_USER
"""
User specified xref. This xref will not be deleted by IDA. This bit
should be combined with the existing xref types ( 'cref_t' & 'dref_t'
) Can not be used for fl_F xrefs
"""
XREF_TAIL = _ida_xref.XREF_TAIL
"""
Reference to tail byte in extrn symbols.
"""
XREF_BASE = _ida_xref.XREF_BASE
"""
Reference to the base part of an offset.
"""
XREF_MASK = _ida_xref.XREF_MASK
"""
Mask to get xref type.
"""
XREF_PASTEND = _ida_xref.XREF_PASTEND
"""
Reference is past item. This bit may be passed to 'add_dref()'
functions but it won't be saved in the database. It will prevent the
destruction of eventual alignment directives.
"""

def xrefchar(*args):
  """
  xrefchar(xrtype) -> char


  Get character describing the xref type.
  
  @param xrtype: combination of  Cross-Reference type flags  and a
                 cref_t  of  dref_t  value (C++: char)
  """
  return _ida_xref.xrefchar(*args)

def add_cref(*args):
  """
  add_cref(frm, to, type) -> bool


  Create a code cross-reference.
  
  @param to: linear address of referenced instruction (C++: ea_t)
  @param type: cross-reference type (C++: cref_t)
  @return: success
  """
  return _ida_xref.add_cref(*args)

def del_cref(*args):
  """
  del_cref(frm, to, expand) -> int


  Delete a code cross-reference.
  
  @param to: linear address of referenced instruction (C++: ea_t)
  @param expand: policy to delete the referenced instruction   1: plan
                 to delete the referenced instruction if it has no more
                 references. 0: don't delete the referenced instruction
                 even if no more cross-references point to it (C++:
                 bool)
  """
  return _ida_xref.del_cref(*args)

def add_dref(*args):
  """
  add_dref(frm, to, type) -> bool


  Create a data cross-reference.
  
  @param to: linear address of referenced data (C++: ea_t)
  @param type: cross-reference type (C++: dref_t)
  @return: success (may fail if user-defined xref exists from->to)
  """
  return _ida_xref.add_dref(*args)

def del_dref(*args):
  """
  del_dref(frm, to)


  Delete a data cross-reference.
  
  @param to: linear address of referenced data (C++: ea_t)
  """
  return _ida_xref.del_dref(*args)
class xrefblk_t(object):
    """
    Proxy of C++ xrefblk_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    frm = _swig_property(_ida_xref.xrefblk_t_frm_get, _ida_xref.xrefblk_t_frm_set)
    to = _swig_property(_ida_xref.xrefblk_t_to_get, _ida_xref.xrefblk_t_to_set)
    iscode = _swig_property(_ida_xref.xrefblk_t_iscode_get, _ida_xref.xrefblk_t_iscode_set)
    type = _swig_property(_ida_xref.xrefblk_t_type_get, _ida_xref.xrefblk_t_type_set)
    user = _swig_property(_ida_xref.xrefblk_t_user_get, _ida_xref.xrefblk_t_user_set)
    def first_from(self, *args):
        """
        first_from(self, _from, flags) -> bool
        """
        return _ida_xref.xrefblk_t_first_from(self, *args)

    def first_to(self, *args):
        """
        first_to(self, _to, flags) -> bool
        """
        return _ida_xref.xrefblk_t_first_to(self, *args)

    def next_from(self, *args):
        """
        next_from(self) -> bool
        next_from(self, _from, _to, flags) -> bool
        """
        return _ida_xref.xrefblk_t_next_from(self, *args)

    def next_to(self, *args):
        """
        next_to(self) -> bool
        next_to(self, _from, _to, flags) -> bool
        """
        return _ida_xref.xrefblk_t_next_to(self, *args)

    def __init__(self, *args):
        """
        __init__(self) -> xrefblk_t
        """
        this = _ida_xref.new_xrefblk_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_xref.delete_xrefblk_t
    __del__ = lambda self : None;
xrefblk_t_swigregister = _ida_xref.xrefblk_t_swigregister
xrefblk_t_swigregister(xrefblk_t)
XREF_ALL = _ida_xref.XREF_ALL
"""
return all references
"""
XREF_FAR = _ida_xref.XREF_FAR
"""
don't return ordinary flow xrefs
"""
XREF_DATA = _ida_xref.XREF_DATA
"""
return data references only
"""


def get_first_dref_from(*args):
  """
  get_first_dref_from(frm) -> ea_t


  Get first data referenced from the specified address.
  
  @return: linear address of first (lowest) data referenced from the
           specified address. The  lastXR  variable contains type of the
           reference. Return  BADADDR  if the specified instruction/data
           doesn't reference to anything.
  """
  return _ida_xref.get_first_dref_from(*args)

def get_next_dref_from(*args):
  """
  get_next_dref_from(frm, current) -> ea_t


  Get next data referenced from the specified address.
  
  @param current: linear address of current referenced data. This value
                  is returned by  get_first_dref_from()  or previous
                  call to  get_next_dref_from()  functions. (C++: ea_t)
  @return: linear address of next data or  BADADDR . The  lastXR
           variable contains type of the reference
  """
  return _ida_xref.get_next_dref_from(*args)

def get_first_dref_to(*args):
  """
  get_first_dref_to(to) -> ea_t


  Get address of instruction/data referencing to the specified data.
  
  @param to: linear address of referencing instruction or data (C++:
             ea_t)
  @return: BADADDR  if nobody refers to the specified data. The  lastXR
           variable contains type of the reference.
  """
  return _ida_xref.get_first_dref_to(*args)

def get_next_dref_to(*args):
  """
  get_next_dref_to(to, current) -> ea_t


  Get address of instruction/data referencing to the specified data
  
  @param to: linear address of referencing instruction or data (C++:
             ea_t)
  @param current: current linear address. This value is returned by
                  get_first_dref_to()  or previous call to
                  get_next_dref_to()  functions. (C++: ea_t)
  @return: BADADDR  if nobody refers to the specified data. The  lastXR
           variable contains type of the reference.
  """
  return _ida_xref.get_next_dref_to(*args)

def get_first_cref_from(*args):
  """
  get_first_cref_from(frm) -> ea_t


  Get first instruction referenced from the specified instruction. If
  the specified instruction passes execution to the next instruction
  then the next instruction is returned. Otherwise the lowest referenced
  address is returned (remember that xrefs are kept sorted!).
  
  @return: first referenced address. The  lastXR  variable contains type
           of the reference. If the specified instruction doesn't
           reference to other instructions then returns  BADADDR .
  """
  return _ida_xref.get_first_cref_from(*args)

def get_next_cref_from(*args):
  """
  get_next_cref_from(frm, current) -> ea_t


  Get next instruction referenced from the specified instruction.
  
  @param current: linear address of current referenced instruction This
                  value is returned by  get_first_cref_from()  or
                  previous call to  get_next_cref_from()  functions.
                  (C++: ea_t)
  @return: next referenced address or  BADADDR . The  lastXR  variable
           contains type of the reference.
  """
  return _ida_xref.get_next_cref_from(*args)

def get_first_cref_to(*args):
  """
  get_first_cref_to(to) -> ea_t


  Get first instruction referencing to the specified instruction. If the
  specified instruction may be executed immediately after its previous
  instruction then the previous instruction is returned. Otherwise the
  lowest referencing address is returned. (remember that xrefs are kept
  sorted!).
  
  @param to: linear address of referenced instruction (C++: ea_t)
  @return: linear address of the first referencing instruction or
           BADADDR . The  lastXR  variable contains type of the
           reference.
  """
  return _ida_xref.get_first_cref_to(*args)

def get_next_cref_to(*args):
  """
  get_next_cref_to(to, current) -> ea_t


  Get next instruction referencing to the specified instruction.
  
  @param to: linear address of referenced instruction (C++: ea_t)
  @param current: linear address of current referenced instruction This
                  value is returned by  get_first_cref_to()  or previous
                  call to  get_next_cref_to()  functions. (C++: ea_t)
  @return: linear address of the next referencing instruction or
           BADADDR . The  lastXR  variable contains type of the
           reference.
  """
  return _ida_xref.get_next_cref_to(*args)

def get_first_fcref_from(*args):
  """
  get_first_fcref_from(frm) -> ea_t
  """
  return _ida_xref.get_first_fcref_from(*args)

def get_next_fcref_from(*args):
  """
  get_next_fcref_from(frm, current) -> ea_t
  """
  return _ida_xref.get_next_fcref_from(*args)

def get_first_fcref_to(*args):
  """
  get_first_fcref_to(to) -> ea_t
  """
  return _ida_xref.get_first_fcref_to(*args)

def get_next_fcref_to(*args):
  """
  get_next_fcref_to(to, current) -> ea_t
  """
  return _ida_xref.get_next_fcref_to(*args)

def has_external_refs(*args):
  """
  has_external_refs(pfn, ea) -> bool


  Has a location external to the function references?
  
  
  @param pfn (C++: func_t  *)
  @param ea (C++: ea_t)
  """
  return _ida_xref.has_external_refs(*args)

def delete_switch_table(*args):
  """
  delete_switch_table(jump_ea, si)
  """
  return _ida_xref.delete_switch_table(*args)
class casevec_t(object):
    """
    Proxy of C++ qvector<(qvector<(sval_t)>)> class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> casevec_t
        __init__(self, x) -> casevec_t
        """
        this = _ida_xref.new_casevec_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_xref.delete_casevec_t
    __del__ = lambda self : None;
    def push_back(self, *args):
        """
        push_back(self, x)
        push_back(self) -> qvector< long long > &
        """
        return _ida_xref.casevec_t_push_back(self, *args)

    def pop_back(self, *args):
        """
        pop_back(self)
        """
        return _ida_xref.casevec_t_pop_back(self, *args)

    def size(self, *args):
        """
        size(self) -> size_t
        """
        return _ida_xref.casevec_t_size(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_xref.casevec_t_empty(self, *args)

    def at(self, *args):
        """
        at(self, _idx) -> qvector< long long > const &
        """
        return _ida_xref.casevec_t_at(self, *args)

    def qclear(self, *args):
        """
        qclear(self)
        """
        return _ida_xref.casevec_t_qclear(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_xref.casevec_t_clear(self, *args)

    def resize(self, *args):
        """
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_xref.casevec_t_resize(self, *args)

    def grow(self, *args):
        """
        grow(self, x=qvector< long long >())
        """
        return _ida_xref.casevec_t_grow(self, *args)

    def capacity(self, *args):
        """
        capacity(self) -> size_t
        """
        return _ida_xref.casevec_t_capacity(self, *args)

    def reserve(self, *args):
        """
        reserve(self, cnt)
        """
        return _ida_xref.casevec_t_reserve(self, *args)

    def truncate(self, *args):
        """
        truncate(self)
        """
        return _ida_xref.casevec_t_truncate(self, *args)

    def swap(self, *args):
        """
        swap(self, r)
        """
        return _ida_xref.casevec_t_swap(self, *args)

    def extract(self, *args):
        """
        extract(self) -> qvector< long long > *
        """
        return _ida_xref.casevec_t_extract(self, *args)

    def inject(self, *args):
        """
        inject(self, s, len)
        """
        return _ida_xref.casevec_t_inject(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_xref.casevec_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_xref.casevec_t___ne__(self, *args)

    def begin(self, *args):
        """
        begin(self) -> qvector< qvector< long long > >::iterator
        begin(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> qvector< qvector< long long > >::iterator
        end(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_end(self, *args)

    def insert(self, *args):
        """
        insert(self, it, x) -> qvector< qvector< long long > >::iterator
        """
        return _ida_xref.casevec_t_insert(self, *args)

    def erase(self, *args):
        """
        erase(self, it) -> qvector< qvector< long long > >::iterator
        erase(self, first, last) -> qvector< qvector< long long > >::iterator
        """
        return _ida_xref.casevec_t_erase(self, *args)

    def find(self, *args):
        """
        find(self, x) -> qvector< qvector< long long > >::iterator
        find(self, x) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_find(self, *args)

    def has(self, *args):
        """
        has(self, x) -> bool
        """
        return _ida_xref.casevec_t_has(self, *args)

    def add_unique(self, *args):
        """
        add_unique(self, x) -> bool
        """
        return _ida_xref.casevec_t_add_unique(self, *args)

    def _del(self, *args):
        """
        _del(self, x) -> bool
        """
        return _ida_xref.casevec_t__del(self, *args)

    def __len__(self, *args):
        """
        __len__(self) -> size_t
        """
        return _ida_xref.casevec_t___len__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, i) -> qvector< long long > const &
        """
        return _ida_xref.casevec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, i, v)
        """
        return _ida_xref.casevec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

casevec_t_swigregister = _ida_xref.casevec_t_swigregister
casevec_t_swigregister(casevec_t)

#<pycode(py_xref)>

import ida_idaapi
ida_idaapi._listify_types(
        casevec_t)

#</pycode(py_xref)>


