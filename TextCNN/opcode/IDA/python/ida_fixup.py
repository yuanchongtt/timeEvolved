# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: fixup
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_fixup', [dirname(__file__)])
        except ImportError:
            import _ida_fixup
            return _ida_fixup
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_fixup', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_fixup = swig_import_helper()
    del swig_import_helper
else:
    import _ida_fixup
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

FIXUP_OFF8 = _ida_fixup.FIXUP_OFF8
FIXUP_OFF16 = _ida_fixup.FIXUP_OFF16
FIXUP_SEG16 = _ida_fixup.FIXUP_SEG16
FIXUP_PTR16 = _ida_fixup.FIXUP_PTR16
FIXUP_OFF32 = _ida_fixup.FIXUP_OFF32
FIXUP_PTR32 = _ida_fixup.FIXUP_PTR32
FIXUP_HI8 = _ida_fixup.FIXUP_HI8
FIXUP_HI16 = _ida_fixup.FIXUP_HI16
FIXUP_LOW8 = _ida_fixup.FIXUP_LOW8
FIXUP_LOW16 = _ida_fixup.FIXUP_LOW16
V695_FIXUP_VHIGH = _ida_fixup.V695_FIXUP_VHIGH
V695_FIXUP_VLOW = _ida_fixup.V695_FIXUP_VLOW
FIXUP_OFF64 = _ida_fixup.FIXUP_OFF64
FIXUP_CUSTOM = _ida_fixup.FIXUP_CUSTOM

def is_fixup_custom(*args):
  """
  is_fixup_custom(type) -> bool


  Is fixup processed by processor module?
  
  
  @param type (C++: fixup_type_t)
  """
  return _ida_fixup.is_fixup_custom(*args)
FIXUPF_REL = _ida_fixup.FIXUPF_REL
"""
fixup is relative to the linear address `base'. Otherwise fixup is
relative to the start of the segment with `sel' selector.
"""
FIXUPF_EXTDEF = _ida_fixup.FIXUPF_EXTDEF
"""
target is a location (otherwise - segment). Use this bit if the target
is a symbol rather than an offset from the beginning of a segment.
"""
FIXUPF_UNUSED = _ida_fixup.FIXUPF_UNUSED
"""
fixup is ignored by IDAdisallows the kernel to convert operandsthis
fixup is not used during output
"""
FIXUPF_CREATED = _ida_fixup.FIXUPF_CREATED
"""
fixup was not present in the input file
"""
FIXUPF_LOADER_MASK = _ida_fixup.FIXUPF_LOADER_MASK
"""
additional flags. The bits from this mask are not stored in the
database and can be used by the loader at its discretion.
"""
class fixup_data_t(object):
    """
    Proxy of C++ fixup_data_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    sel = _swig_property(_ida_fixup.fixup_data_t_sel_get, _ida_fixup.fixup_data_t_sel_set)
    off = _swig_property(_ida_fixup.fixup_data_t_off_get, _ida_fixup.fixup_data_t_off_set)
    displacement = _swig_property(_ida_fixup.fixup_data_t_displacement_get, _ida_fixup.fixup_data_t_displacement_set)
    def __init__(self, *args):
        """
        __init__(self) -> fixup_data_t
        __init__(self, type_, flags_=0) -> fixup_data_t
        """
        this = _ida_fixup.new_fixup_data_t(*args)
        try: self.this.append(this)
        except: self.this = this
    def get_type(self, *args):
        """
        get_type(self) -> fixup_type_t
        """
        return _ida_fixup.fixup_data_t_get_type(self, *args)

    def set_type(self, *args):
        """
        set_type(self, type_)
        """
        return _ida_fixup.fixup_data_t_set_type(self, *args)

    def set_type_and_flags(self, *args):
        """
        set_type_and_flags(self, type_, flags_=0)
        """
        return _ida_fixup.fixup_data_t_set_type_and_flags(self, *args)

    def is_custom(self, *args):
        """
        is_custom(self) -> bool
        """
        return _ida_fixup.fixup_data_t_is_custom(self, *args)

    def get_flags(self, *args):
        """
        get_flags(self) -> uint32
        """
        return _ida_fixup.fixup_data_t_get_flags(self, *args)

    def is_extdef(self, *args):
        """
        is_extdef(self) -> bool
        """
        return _ida_fixup.fixup_data_t_is_extdef(self, *args)

    def set_extdef(self, *args):
        """
        set_extdef(self)
        """
        return _ida_fixup.fixup_data_t_set_extdef(self, *args)

    def clr_extdef(self, *args):
        """
        clr_extdef(self)
        """
        return _ida_fixup.fixup_data_t_clr_extdef(self, *args)

    def is_unused(self, *args):
        """
        is_unused(self) -> bool
        """
        return _ida_fixup.fixup_data_t_is_unused(self, *args)

    def set_unused(self, *args):
        """
        set_unused(self)
        """
        return _ida_fixup.fixup_data_t_set_unused(self, *args)

    def clr_unused(self, *args):
        """
        clr_unused(self)
        """
        return _ida_fixup.fixup_data_t_clr_unused(self, *args)

    def has_base(self, *args):
        """
        has_base(self) -> bool
        """
        return _ida_fixup.fixup_data_t_has_base(self, *args)

    def was_created(self, *args):
        """
        was_created(self) -> bool
        """
        return _ida_fixup.fixup_data_t_was_created(self, *args)

    def get_base(self, *args):
        """
        get_base(self) -> ea_t
        """
        return _ida_fixup.fixup_data_t_get_base(self, *args)

    def set_base(self, *args):
        """
        set_base(self, new_base)
        """
        return _ida_fixup.fixup_data_t_set_base(self, *args)

    def set_sel(self, *args):
        """
        set_sel(self, seg)
        """
        return _ida_fixup.fixup_data_t_set_sel(self, *args)

    def set_target_sel(self, *args):
        """
        set_target_sel(self)
        """
        return _ida_fixup.fixup_data_t_set_target_sel(self, *args)

    def set(self, *args):
        """
        set(self, source)
        """
        return _ida_fixup.fixup_data_t_set(self, *args)

    def get(self, *args):
        """
        get(self, source) -> bool
        """
        return _ida_fixup.fixup_data_t_get(self, *args)

    def get_handler(self, *args):
        """
        get_handler(self) -> fixup_handler_t const *
        """
        return _ida_fixup.fixup_data_t_get_handler(self, *args)

    def get_desc(self, *args):
        """
        get_desc(self, source) -> char const *
        """
        return _ida_fixup.fixup_data_t_get_desc(self, *args)

    def calc_size(self, *args):
        """
        calc_size(self) -> int
        """
        return _ida_fixup.fixup_data_t_calc_size(self, *args)

    def get_value(self, *args):
        """
        get_value(self, ea) -> uval_t
        """
        return _ida_fixup.fixup_data_t_get_value(self, *args)

    def patch_value(self, *args):
        """
        patch_value(self, ea) -> bool
        """
        return _ida_fixup.fixup_data_t_patch_value(self, *args)

    __swig_destroy__ = _ida_fixup.delete_fixup_data_t
    __del__ = lambda self : None;
fixup_data_t_swigregister = _ida_fixup.fixup_data_t_swigregister
fixup_data_t_swigregister(fixup_data_t)


def get_fixup(*args):
  """
  get_fixup(fd, source) -> bool


  Get fixup information.
  
  
  @param fd (C++: fixup_data_t  *)
  @param source (C++: ea_t)
  """
  return _ida_fixup.get_fixup(*args)

def exists_fixup(*args):
  """
  exists_fixup(source) -> bool


  Check that a fixup exists at the given address.
  
  
  @param source (C++: ea_t)
  """
  return _ida_fixup.exists_fixup(*args)

def set_fixup(*args):
  """
  set_fixup(source, fd)


  Set fixup information. You should fill 'fixup_data_t' and call this
  function and the kernel will remember information in the database.
  
  @param source: the fixup source address, i.e. the address modified by
                 the fixup (C++: ea_t)
  @param fd: fixup data (C++: const  fixup_data_t  &)
  """
  return _ida_fixup.set_fixup(*args)

def del_fixup(*args):
  """
  del_fixup(source)


  Delete fixup information.
  
  
  @param source (C++: ea_t)
  """
  return _ida_fixup.del_fixup(*args)

def get_first_fixup_ea(*args):
  """
  get_first_fixup_ea() -> ea_t


  Get the first address with fixup information
  
  @return: the first address with fixup information, or BADADDR
  """
  return _ida_fixup.get_first_fixup_ea(*args)

def get_next_fixup_ea(*args):
  """
  get_next_fixup_ea(ea) -> ea_t


  Find next address with fixup information
  
  @param ea: current address (C++: ea_t)
  @return: the next address with fixup information, or BADADDR
  """
  return _ida_fixup.get_next_fixup_ea(*args)

def get_prev_fixup_ea(*args):
  """
  get_prev_fixup_ea(ea) -> ea_t


  Find previous address with fixup information
  
  @param ea: current address (C++: ea_t)
  @return: the previous address with fixup information, or BADADDR
  """
  return _ida_fixup.get_prev_fixup_ea(*args)

def get_fixup_handler(*args):
  """
  get_fixup_handler(type) -> fixup_handler_t const *


  Get handler of standard or custom fixup.
  
  
  @param type (C++: fixup_type_t)
  """
  return _ida_fixup.get_fixup_handler(*args)

def get_fixup_value(*args):
  """
  get_fixup_value(ea, type) -> uval_t


  Get the operand value. This function get fixup bytes from data or an
  instruction at `ea' and convert them to the operand value (maybe
  partially). It is opposite in meaning to the. For example, FIXUP_HI8
  read a byte at `ea' and shifts it left by 8 bits, or AArch64's custom
  fixup BRANCH26 get low 26 bits of the insn at `ea' and shifts it left
  by 2 bits. This function is mainly used to get a relocation addend.
  'patch_fixup_value()'  'fixup_handler_t::size'
  
  @param ea: address to get fixup bytes from, the size of the fixup
             bytes depends on the fixup type. (C++: ea_t)
  @param type (C++: fixup_type_t)
  """
  return _ida_fixup.get_fixup_value(*args)

def patch_fixup_value(*args):
  """
  patch_fixup_value(ea, fd) -> bool


  Patch the fixup bytes. This function updates data or an instruction at
  `ea' to the fixup bytes. For example, FIXUP_HI8 updates a byte at `ea'
  to the high byte of `fd->off', or AArch64's custom fixup BRANCH26
  updates low 26 bits of the insn at `ea' to the value of `fd->off'
  shifted right by 2. 'fixup_handler_t::size'
  
  @param ea: address where data are changed, the size of the changed
             data depends on the fixup type. (C++: ea_t)
  @param fd (C++: const  fixup_data_t  &)
  """
  return _ida_fixup.patch_fixup_value(*args)

def get_fixup_desc(*args):
  """
  get_fixup_desc(source, fd) -> char const *


  Get FIXUP description comment.
  
  
  @param source (C++: ea_t)
  @param fd (C++: const  fixup_data_t  &)
  """
  return _ida_fixup.get_fixup_desc(*args)

def calc_fixup_size(*args):
  """
  calc_fixup_size(type) -> int


  Calculate size of fixup in bytes (the number of bytes the fixup
  patches)
  
  @param type (C++: fixup_type_t)
  """
  return _ida_fixup.calc_fixup_size(*args)

def find_custom_fixup(*args):
  """
  find_custom_fixup(name) -> fixup_type_t


  Get id of a custom fixup handler.
  
  @param name: name of the custom fixup handler (C++: const char *)
  @return: id with FIXUP_CUSTOM bit set or 0
  """
  return _ida_fixup.find_custom_fixup(*args)
class fixup_info_t(object):
    """
    Proxy of C++ fixup_info_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = _swig_property(_ida_fixup.fixup_info_t_ea_get, _ida_fixup.fixup_info_t_ea_set)
    fd = _swig_property(_ida_fixup.fixup_info_t_fd_get, _ida_fixup.fixup_info_t_fd_set)
    def __init__(self, *args):
        """
        __init__(self) -> fixup_info_t
        """
        this = _ida_fixup.new_fixup_info_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_fixup.delete_fixup_info_t
    __del__ = lambda self : None;
fixup_info_t_swigregister = _ida_fixup.fixup_info_t_swigregister
fixup_info_t_swigregister(fixup_info_t)


def get_fixups(*args):
  """
  get_fixups(out, ea, size) -> bool
  """
  return _ida_fixup.get_fixups(*args)

def contains_fixups(*args):
  """
  contains_fixups(ea, size) -> bool


  Does the specified address range contain any fixup information?
  
  
  @param ea (C++: ea_t)
  @param size (C++: asize_t)
  """
  return _ida_fixup.contains_fixups(*args)

def gen_fix_fixups(*args):
  """
  gen_fix_fixups(_from, to, size)


  Relocate the bytes with fixup information once more (generic
  function). This function may be called from 'loader_t::move_segm()' if
  it suits the goal. If 'loader_t::move_segm' is not defined then this
  function will be called automatically when moving segments or rebasing
  the entire program. Special parameter values (from = BADADDR, size =
  0, to = delta) are used when the function is called from
  rebase_program(delta).
  
  @param _from (C++: ea_t)
  @param to (C++: ea_t)
  @param size (C++: asize_t)
  """
  return _ida_fixup.gen_fix_fixups(*args)
if _BC695:
    FIXUP_CREATED=FIXUPF_CREATED
    FIXUP_EXTDEF=FIXUPF_EXTDEF
    FIXUP_REL=FIXUPF_REL


