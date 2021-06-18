# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: segregs
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_segregs', [dirname(__file__)])
        except ImportError:
            import _ida_segregs
            return _ida_segregs
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_segregs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_segregs = swig_import_helper()
    del swig_import_helper
else:
    import _ida_segregs
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

import ida_range
R_es = _ida_segregs.R_es
R_cs = _ida_segregs.R_cs
R_ss = _ida_segregs.R_ss
R_ds = _ida_segregs.R_ds
R_fs = _ida_segregs.R_fs
R_gs = _ida_segregs.R_gs
class sreg_range_t(ida_range.range_t):
    """
    Proxy of C++ sreg_range_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    val = _swig_property(_ida_segregs.sreg_range_t_val_get, _ida_segregs.sreg_range_t_val_set)
    tag = _swig_property(_ida_segregs.sreg_range_t_tag_get, _ida_segregs.sreg_range_t_tag_set)
    def __init__(self, *args):
        """
        __init__(self) -> sreg_range_t
        """
        this = _ida_segregs.new_sreg_range_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_segregs.delete_sreg_range_t
    __del__ = lambda self : None;
sreg_range_t_swigregister = _ida_segregs.sreg_range_t_swigregister
sreg_range_t_swigregister(sreg_range_t)
SR_inherit = _ida_segregs.SR_inherit
"""
the value is inherited from the previous range
"""
SR_user = _ida_segregs.SR_user
"""
the value is specified by the user
"""
SR_auto = _ida_segregs.SR_auto
"""
the value is determined by IDA
"""
SR_autostart = _ida_segregs.SR_autostart
"""
used as 'SR_auto' for segment starting address
"""


def get_sreg(*args):
  """
  get_sreg(ea, rg) -> sel_t


  Get value of a segment register. This function uses segment register
  range and default segment register values stored in the segment
  structure.
  
  @param ea: linear address in the program (C++: ea_t)
  @param rg: number of the segment register (C++: int)
  @return: value of the segment register,  BADSEL  if value is unknown.
  """
  return _ida_segregs.get_sreg(*args)

def split_sreg_range(*args):
  """
  split_sreg_range(ea, rg, v, tag, silent=False) -> bool


  Create a new segment register range. This function is used when the
  IDP emulator detects that a segment register changes its value.
  
  @param ea: linear address where the segment register will have a new
             value. if ea== BADADDR , nothing to do. (C++: ea_t)
  @param rg: the number of the segment register (C++: int)
  @param v: the new value of the segment register. If the value is
            unknown, you should specify  BADSEL . (C++: sel_t)
  @param tag: the register info tag. see  Segment register range tags
              (C++: uchar)
  @param silent: if false, display a warning() in the case of failure
                 (C++: bool)
  @return: success
  """
  return _ida_segregs.split_sreg_range(*args)

def set_default_sreg_value(*args):
  """
  set_default_sreg_value(sg, rg, value) -> bool


  Set default value of a segment register for a segment.
  
  @param sg: pointer to segment structure if NULL, then set the register
             for all segments (C++: segment_t  *)
  @param rg: number of segment register (C++: int)
  @param value: its default value. this value will be used by
                get_sreg()  if value of the register is unknown at the
                specified address. (C++: sel_t)
  @return: success
  """
  return _ida_segregs.set_default_sreg_value(*args)

def set_sreg_at_next_code(*args):
  """
  set_sreg_at_next_code(ea1, ea2, rg, value)


  Set the segment register value at the next instruction. This function
  is designed to be called from 'idb_event::sgr_changed' handler in
  order to contain the effect of changing a segment register value only
  until the next instruction.It is useful, for example, in the ARM
  module: the modification of the T register does not affect existing
  instructions later in the code.
  
  @param ea1: address to start to search for an instruction (C++: ea_t)
  @param ea2: the maximal address (C++: ea_t)
  @param rg: the segment register number (C++: int)
  @param value: the segment register value (C++: sel_t)
  """
  return _ida_segregs.set_sreg_at_next_code(*args)

def get_sreg_range(*args):
  """
  get_sreg_range(out, ea, rg) -> bool


  Get segment register range by linear address.
  
  @param out: segment register range (C++: sreg_range_t  *)
  @param ea: any linear address in the program (C++: ea_t)
  @param rg: the segment register number (C++: int)
  @return: success
  """
  return _ida_segregs.get_sreg_range(*args)

def get_prev_sreg_range(*args):
  """
  get_prev_sreg_range(out, ea, rg) -> bool


  Get segment register range previous to one with address.more efficient
  then get_sreg_range(reg, ea-1)
  
  @param out: segment register range (C++: sreg_range_t  *)
  @param ea: any linear address in the program (C++: ea_t)
  @param rg: the segment register number (C++: int)
  @return: success
  """
  return _ida_segregs.get_prev_sreg_range(*args)

def set_default_dataseg(*args):
  """
  set_default_dataseg(ds_sel)


  Set default value of DS register for all segments.
  
  
  @param ds_sel (C++: sel_t)
  """
  return _ida_segregs.set_default_dataseg(*args)

def get_sreg_ranges_qty(*args):
  """
  get_sreg_ranges_qty(rg) -> size_t


  Get number of segment register ranges.
  
  @param rg: the segment register number (C++: int)
  """
  return _ida_segregs.get_sreg_ranges_qty(*args)

def getn_sreg_range(*args):
  """
  getn_sreg_range(out, rg, n) -> bool


  Get segment register range by its number.
  
  @param out: segment register range (C++: sreg_range_t  *)
  @param rg: the segment register number (C++: int)
  @param n: number of range (0..qty()-1) (C++: int)
  @return: success
  """
  return _ida_segregs.getn_sreg_range(*args)

def get_sreg_range_num(*args):
  """
  get_sreg_range_num(ea, rg) -> int


  Get number of segment register range by address.
  
  @param ea: any address in the range (C++: ea_t)
  @param rg: the segment register number (C++: int)
  @return: -1 if no range occupies the specified address. otherwise
           returns number of the specified range
           (0..get_srranges_qty()-1)
  """
  return _ida_segregs.get_sreg_range_num(*args)

def del_sreg_range(*args):
  """
  del_sreg_range(ea, rg) -> bool


  Delete segment register range started at ea. When a segment register
  range is deleted, the previous range is extended to cover the empty
  space. The segment register range at the beginning of a segment can
  not be deleted.
  
  @param ea: start_ea of the deleted range (C++: ea_t)
  @param rg: the segment register number (C++: int)
  @return: success
  """
  return _ida_segregs.del_sreg_range(*args)

def copy_sreg_ranges(*args):
  """
  copy_sreg_ranges(dst_rg, src_rg, map_selector=False)


  Duplicate segment register ranges.
  
  @param dst_rg: number of destination segment register (C++: int)
  @param src_rg: copy ranges from (C++: int)
  @param map_selector: map selectors to linear addresses using  sel2ea()
                       (C++: bool)
  """
  return _ida_segregs.copy_sreg_ranges(*args)
if _BC695:
    import sys
    sys.modules["ida_srarea"] = sys.modules["ida_segregs"]
    SetDefaultRegisterValue=set_default_sreg_value
    copy_srareas=copy_sreg_ranges
    def ___looks_like_ea_not_segreg(thing):
        # yay heuristics. Not sure how best to do this...
        return (type(thing) == long) or (thing > 0x200)
    def del_sreg_range(*args):
        if ___looks_like_ea_not_segreg(args[1]): # 6.95: rg, ea
            ea, rg = args[1], args[0]
        else:                                    # 7.00: ea, rg
            ea, rg = args
        return _ida_segregs.del_sreg_range(ea, rg)
    del_srarea=del_sreg_range
    getSR=get_sreg
    get_prev_srarea=get_prev_sreg_range
    get_srarea2=get_sreg_range
    def get_sreg_range_num(*args):
        if ___looks_like_ea_not_segreg(args[1]): # 6.95: rg, ea
            ea, rg = args[1], args[0]
        else:                                    # 7.00: ea, rg
            ea, rg = args
        return _ida_segregs.get_sreg_range_num(ea, rg)
    get_srarea_num=get_sreg_range_num
    get_srareas_qty2=get_sreg_ranges_qty
    getn_srarea2=getn_sreg_range
    import ida_idaapi
    is_segreg_locked=ida_idaapi._BC695.false_p
    class lock_segreg:
        def __init__():
            pass
    segreg_area_t=sreg_range_t
    splitSRarea1=split_sreg_range
    split_srarea=split_sreg_range
    get_segreg=get_sreg
    set_default_segreg_value=set_default_sreg_value



