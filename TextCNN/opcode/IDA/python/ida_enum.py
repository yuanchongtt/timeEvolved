# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: enum
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_enum', [dirname(__file__)])
        except ImportError:
            import _ida_enum
            return _ida_enum
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_enum', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_enum = swig_import_helper()
    del swig_import_helper
else:
    import _ida_enum
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

DEFMASK = _ida_enum.DEFMASK
"""
default bitmask
"""

def get_enum_qty(*args):
  """
  get_enum_qty() -> size_t


  Get number of declared 'enum_t' types.
  """
  return _ida_enum.get_enum_qty(*args)

def getn_enum(*args):
  """
  getn_enum(n) -> enum_t


  Get enum by its ordinal number (0..n).
  
  
  @param n (C++: size_t)
  """
  return _ida_enum.getn_enum(*args)

def get_enum_idx(*args):
  """
  get_enum_idx(id) -> uval_t


  Get serial number of enum. The serial number determines the place of
  the enum in the enum window.
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_idx(*args)

def get_enum(*args):
  """
  get_enum(name) -> enum_t


  Get enum by name.
  
  
  @param name (C++: const char *)
  """
  return _ida_enum.get_enum(*args)

def is_bf(*args):
  """
  is_bf(id) -> bool


  Is enum a bitfield? (otherwise - plain enum, no bitmasks except for
  'DEFMASK' are allowed)
  
  @param id (C++: enum_t)
  """
  return _ida_enum.is_bf(*args)

def is_enum_hidden(*args):
  """
  is_enum_hidden(id) -> bool


  Is enum collapsed?
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.is_enum_hidden(*args)

def set_enum_hidden(*args):
  """
  set_enum_hidden(id, hidden) -> bool


  Collapse enum.
  
  
  @param id (C++: enum_t)
  @param hidden (C++: bool)
  """
  return _ida_enum.set_enum_hidden(*args)

def is_enum_fromtil(*args):
  """
  is_enum_fromtil(id) -> bool


  Does enum come from type library?
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.is_enum_fromtil(*args)

def set_enum_fromtil(*args):
  """
  set_enum_fromtil(id, fromtil) -> bool


  Specify that enum comes from a type library.
  
  
  @param id (C++: enum_t)
  @param fromtil (C++: bool)
  """
  return _ida_enum.set_enum_fromtil(*args)

def is_ghost_enum(*args):
  """
  is_ghost_enum(id) -> bool


  Is a ghost copy of a local type?
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.is_ghost_enum(*args)

def set_enum_ghost(*args):
  """
  set_enum_ghost(id, ghost) -> bool


  Specify that enum is a ghost copy of a local type.
  
  
  @param id (C++: enum_t)
  @param ghost (C++: bool)
  """
  return _ida_enum.set_enum_ghost(*args)

def get_enum_name(*args):
  """
  get_enum_name(id) -> ssize_t


  Get name of enum.
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_name(*args)

def get_enum_width(*args):
  """
  get_enum_width(id) -> size_t


  Get the width of a enum element allowed values: 0
  (unspecified),1,2,4,8,16,32,64
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_width(*args)

def set_enum_width(*args):
  """
  set_enum_width(id, width) -> bool


  See comment for 'get_enum_width()'
  
  
  @param id (C++: enum_t)
  @param width (C++: int)
  """
  return _ida_enum.set_enum_width(*args)

def get_enum_cmt(*args):
  """
  get_enum_cmt(id, repeatable) -> ssize_t


  Get enum comment.
  
  
  @param id (C++: enum_t)
  @param repeatable (C++: bool)
  """
  return _ida_enum.get_enum_cmt(*args)

def get_enum_size(*args):
  """
  get_enum_size(id) -> size_t


  Get the number of the members of the enum.
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_size(*args)

def get_enum_flag(*args):
  """
  get_enum_flag(id) -> flags_t


  Get flags determining the representation of the enum. (currently they
  define the numeric base: octal, decimal, hex, bin) and signness.
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_flag(*args)

def get_enum_member_by_name(*args):
  """
  get_enum_member_by_name(name) -> const_t


  Get a reference to an enum member by its name.
  
  
  @param name (C++: const char *)
  """
  return _ida_enum.get_enum_member_by_name(*args)

def get_enum_member_value(*args):
  """
  get_enum_member_value(id) -> uval_t


  Get value of an enum member.
  
  
  @param id (C++: const_t)
  """
  return _ida_enum.get_enum_member_value(*args)

def get_enum_member_enum(*args):
  """
  get_enum_member_enum(id) -> enum_t


  Get the parent enum of an enum member.
  
  
  @param id (C++: const_t)
  """
  return _ida_enum.get_enum_member_enum(*args)

def get_enum_member_bmask(*args):
  """
  get_enum_member_bmask(id) -> bmask_t


  Get bitmask of an enum member.
  
  
  @param id (C++: const_t)
  """
  return _ida_enum.get_enum_member_bmask(*args)

def get_enum_member(*args):
  """
  get_enum_member(id, value, serial, mask) -> const_t


  Find an enum member by enum, value and bitmaskif serial -1, return a
  member with any serial
  
  @param id (C++: enum_t)
  @param value (C++: uval_t)
  @param serial (C++: int)
  @param mask (C++: bmask_t)
  """
  return _ida_enum.get_enum_member(*args)

def get_first_bmask(*args):
  """
  get_first_bmask(id) -> bmask_t


  Get first bitmask in the enum (bitfield)
  
  @param id (C++: enum_t)
  @return: the smallest bitmask for enum, or DEFMASK
  """
  return _ida_enum.get_first_bmask(*args)

def get_last_bmask(*args):
  """
  get_last_bmask(id) -> bmask_t


  Get last bitmask in the enum (bitfield)
  
  @param id (C++: enum_t)
  @return: the biggest bitmask for enum, or DEFMASK
  """
  return _ida_enum.get_last_bmask(*args)

def get_next_bmask(*args):
  """
  get_next_bmask(id, bmask) -> bmask_t


  Get next bitmask in the enum (bitfield)
  
  @param id (C++: enum_t)
  @param bmask (C++: bmask_t)
  @return: value of a bitmask with value higher than the specified
           value, or DEFMASK
  """
  return _ida_enum.get_next_bmask(*args)

def get_prev_bmask(*args):
  """
  get_prev_bmask(id, bmask) -> bmask_t


  Get prev bitmask in the enum (bitfield)
  
  @param id (C++: enum_t)
  @param bmask (C++: bmask_t)
  @return: value of a bitmask with value lower than the specified value,
           or DEFMASK
  """
  return _ida_enum.get_prev_bmask(*args)

def get_first_enum_member(*args):
  """
  get_first_enum_member(id, bmask=(bmask_t(-1))) -> uval_t
  """
  return _ida_enum.get_first_enum_member(*args)

def get_last_enum_member(*args):
  """
  get_last_enum_member(id, bmask=(bmask_t(-1))) -> uval_t
  """
  return _ida_enum.get_last_enum_member(*args)

def get_next_enum_member(*args):
  """
  get_next_enum_member(id, value, bmask=(bmask_t(-1))) -> uval_t
  """
  return _ida_enum.get_next_enum_member(*args)

def get_prev_enum_member(*args):
  """
  get_prev_enum_member(id, value, bmask=(bmask_t(-1))) -> uval_t
  """
  return _ida_enum.get_prev_enum_member(*args)

def get_enum_member_name(*args):
  """
  get_enum_member_name(id) -> ssize_t


  Get name of an enum member by const_t.
  
  
  @param id (C++: const_t)
  """
  return _ida_enum.get_enum_member_name(*args)

def get_enum_member_cmt(*args):
  """
  get_enum_member_cmt(id, repeatable) -> ssize_t


  Get enum member's comment.
  
  
  @param id (C++: const_t)
  @param repeatable (C++: bool)
  """
  return _ida_enum.get_enum_member_cmt(*args)

def get_first_serial_enum_member(*args):
  """
  get_first_serial_enum_member(id, value, bmask) -> const_t
  """
  return _ida_enum.get_first_serial_enum_member(*args)

def get_last_serial_enum_member(*args):
  """
  get_last_serial_enum_member(id, value, bmask) -> const_t
  """
  return _ida_enum.get_last_serial_enum_member(*args)

def get_next_serial_enum_member(*args):
  """
  get_next_serial_enum_member(in_out_serial, first_cid) -> const_t
  """
  return _ida_enum.get_next_serial_enum_member(*args)

def get_prev_serial_enum_member(*args):
  """
  get_prev_serial_enum_member(in_out_serial, first_cid) -> const_t
  """
  return _ida_enum.get_prev_serial_enum_member(*args)
class enum_member_visitor_t(object):
    """
    Proxy of C++ enum_member_visitor_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def visit_enum_member(self, *args):
        """
        visit_enum_member(self, cid, value) -> int
        """
        return _ida_enum.enum_member_visitor_t_visit_enum_member(self, *args)

    def __init__(self, *args):
        """
        __init__(self) -> enum_member_visitor_t
        """
        if self.__class__ == enum_member_visitor_t:
            _self = None
        else:
            _self = self
        this = _ida_enum.new_enum_member_visitor_t(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_enum.delete_enum_member_visitor_t
    __del__ = lambda self : None;
    def __disown__(self):
        self.this.disown()
        _ida_enum.disown_enum_member_visitor_t(self)
        return weakref_proxy(self)
enum_member_visitor_t_swigregister = _ida_enum.enum_member_visitor_t_swigregister
enum_member_visitor_t_swigregister(enum_member_visitor_t)
cvar = _ida_enum.cvar
MAX_ENUM_SERIAL = cvar.MAX_ENUM_SERIAL


def for_all_enum_members(*args):
  """
  for_all_enum_members(id, cv) -> int


  Visit all members of a given enum.
  
  
  @param id (C++: enum_t)
  @param cv (C++: enum_member_visitor_t  &)
  """
  return _ida_enum.for_all_enum_members(*args)

def get_enum_member_serial(*args):
  """
  get_enum_member_serial(cid) -> uchar


  Get serial number of an enum member.
  
  
  @param cid (C++: const_t)
  """
  return _ida_enum.get_enum_member_serial(*args)

def get_enum_type_ordinal(*args):
  """
  get_enum_type_ordinal(id) -> int32


  Get corresponding type ordinal number.
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.get_enum_type_ordinal(*args)

def set_enum_type_ordinal(*args):
  """
  set_enum_type_ordinal(id, ord)


  Set corresponding type ordinal number.
  
  
  @param id (C++: enum_t)
  @param ord (C++: int32)
  """
  return _ida_enum.set_enum_type_ordinal(*args)

def add_enum(*args):
  """
  add_enum(idx, name, flag) -> enum_t


  Add new enum type.if idx== 'BADADDR' then add as the last idxif
  name==NULL then generate a unique name "enum_%d"
  
  @param idx (C++: size_t)
  @param name (C++: const char *)
  @param flag (C++: flags_t)
  """
  return _ida_enum.add_enum(*args)

def del_enum(*args):
  """
  del_enum(id)


  Delete an enum type.
  
  
  @param id (C++: enum_t)
  """
  return _ida_enum.del_enum(*args)

def set_enum_idx(*args):
  """
  set_enum_idx(id, idx) -> bool


  Set serial number of enum. Also see 'get_enum_idx()' .
  
  @param id (C++: enum_t)
  @param idx (C++: size_t)
  """
  return _ida_enum.set_enum_idx(*args)

def set_enum_bf(*args):
  """
  set_enum_bf(id, bf) -> bool


  Set 'bitfield' bit of enum (i.e. convert it to a bitfield)
  
  
  @param id (C++: enum_t)
  @param bf (C++: bool)
  """
  return _ida_enum.set_enum_bf(*args)

def set_enum_name(*args):
  """
  set_enum_name(id, name) -> bool


  Set name of enum type.
  
  
  @param id (C++: enum_t)
  @param name (C++: const char *)
  """
  return _ida_enum.set_enum_name(*args)

def set_enum_cmt(*args):
  """
  set_enum_cmt(id, cmt, repeatable) -> bool


  Set comment for enum type.
  
  
  @param id (C++: enum_t)
  @param cmt (C++: const char *)
  @param repeatable (C++: bool)
  """
  return _ida_enum.set_enum_cmt(*args)

def set_enum_flag(*args):
  """
  set_enum_flag(id, flag) -> bool


  Set data representation flags.
  
  
  @param id (C++: enum_t)
  @param flag (C++: flags_t)
  """
  return _ida_enum.set_enum_flag(*args)

def add_enum_member(*args):
  """
  add_enum_member(id, name, value, bmask=(bmask_t(-1))) -> int


  Add member to enum type.
  
  @param id (C++: enum_t)
  @param name (C++: const char *)
  @param value (C++: uval_t)
  @param bmask (C++: bmask_t)
  @return: 0 if ok, otherwise one of  Add enum member result codes
  """
  return _ida_enum.add_enum_member(*args)
ENUM_MEMBER_ERROR_NAME = _ida_enum.ENUM_MEMBER_ERROR_NAME
"""
already have member with this name (bad name)
"""
ENUM_MEMBER_ERROR_VALUE = _ida_enum.ENUM_MEMBER_ERROR_VALUE
"""
already have 256 members with this value
"""
ENUM_MEMBER_ERROR_ENUM = _ida_enum.ENUM_MEMBER_ERROR_ENUM
"""
bad enum id
"""
ENUM_MEMBER_ERROR_MASK = _ida_enum.ENUM_MEMBER_ERROR_MASK
"""
bad bmask
"""
ENUM_MEMBER_ERROR_ILLV = _ida_enum.ENUM_MEMBER_ERROR_ILLV
"""
bad bmask and value combination (~bmask & value != 0)
"""

def del_enum_member(*args):
  """
  del_enum_member(id, value, serial, bmask) -> bool


  Delete member of enum type.
  
  
  @param id (C++: enum_t)
  @param value (C++: uval_t)
  @param serial (C++: uchar)
  @param bmask (C++: bmask_t)
  """
  return _ida_enum.del_enum_member(*args)

def set_enum_member_name(*args):
  """
  set_enum_member_name(id, name) -> bool


  Set name of enum member.
  
  
  @param id (C++: const_t)
  @param name (C++: const char *)
  """
  return _ida_enum.set_enum_member_name(*args)

def set_enum_member_cmt(*args):
  """
  set_enum_member_cmt(id, cmt, repeatable) -> bool


  Set comment for enum member.
  
  
  @param id (C++: const_t)
  @param cmt (C++: const char *)
  @param repeatable (C++: bool)
  """
  return _ida_enum.set_enum_member_cmt(*args)

def is_one_bit_mask(*args):
  """
  is_one_bit_mask(mask) -> bool


  Is bitmask one bit?
  
  
  @param mask (C++: bmask_t)
  """
  return _ida_enum.is_one_bit_mask(*args)

def set_bmask_name(*args):
  """
  set_bmask_name(id, bmask, name) -> bool
  """
  return _ida_enum.set_bmask_name(*args)

def get_bmask_name(*args):
  """
  get_bmask_name(id, bmask) -> ssize_t
  """
  return _ida_enum.get_bmask_name(*args)

def set_bmask_cmt(*args):
  """
  set_bmask_cmt(id, bmask, cmt, repeatable) -> bool
  """
  return _ida_enum.set_bmask_cmt(*args)

def get_bmask_cmt(*args):
  """
  get_bmask_cmt(id, bmask, repeatable) -> ssize_t
  """
  return _ida_enum.get_bmask_cmt(*args)
if _BC695:
    CONST_ERROR_ENUM=ENUM_MEMBER_ERROR_NAME
    CONST_ERROR_ILLV=ENUM_MEMBER_ERROR_VALUE
    CONST_ERROR_MASK=ENUM_MEMBER_ERROR_ENUM
    CONST_ERROR_NAME=ENUM_MEMBER_ERROR_MASK
    CONST_ERROR_VALUE=ENUM_MEMBER_ERROR_ILLV
    add_const=add_enum_member
    del_const=del_enum_member
    get_const=get_enum_member
    get_const_bmask=get_enum_member_bmask
    get_const_by_name=get_enum_member_by_name
    get_const_cmt=get_enum_member_cmt
    get_const_enum=get_enum_member_enum
    get_const_name=get_enum_member_name
    get_const_serial=get_enum_member_serial
    get_const_value=get_enum_member_value
    get_first_const=get_first_enum_member
    get_first_serial_const=get_first_serial_enum_member
    get_last_const=get_last_enum_member
    get_last_serial_const=get_last_serial_enum_member
    get_next_const=get_next_enum_member
    get_next_serial_const=get_next_serial_enum_member
    get_prev_const=get_prev_enum_member
    get_prev_serial_const=get_prev_serial_enum_member
    set_const_cmt=set_enum_member_cmt
    set_const_name=set_enum_member_name
    def get_next_serial_enum_member(*args):
        serial, cid = args[0], args[1]
        if serial > 0xFF:
            serial, cid = cid, serial
        return _ida_enum.get_next_serial_enum_member(serial, cid)
    def get_prev_serial_enum_member(*args):
        serial, cid = args[0], args[1]
        if serial > 0xFF:
            serial, cid = cid, serial
        return _ida_enum.get_prev_serial_enum_member(serial, cid)



