import magic as pymagic
from afile.hooks import HookedFunction
from functools import wraps
from contextlib import contextmanager
from magic.flags import *

class AttributeDict(dict):
	def __getattr__(self,k):
		return self[k]

hooks = AttributeDict(id_filename=AttributeDict(pre=[],post=[]),id_buffer=AttributeDict(pre=[],post=[]))

def add_hook(target,func,pre=False):
	hooks[target]["pre" if pre else "post"].append(func)

def del_hook(target,func,pre=False):
	hooks[target]["pre" if pre else "post"].remove(func)

def clear_hooks(target,pre=False):
	while len(hooks[target]["pre" if pre else "post"])>0:
		hooks[target]["pre" if pre else "post"].pop()

def apply_hooks(func):
	hooked = HookedFunction(func)
	hooked.__pre_hooks__ = hooks[func.__name__]["pre"]
	hooked.__post_hooks__ = hooks[func.__name__]["post"]
	return hooked

HOOKED = "id_filename id_buffer".split()

@contextmanager
def magic(*args,**kwargs):
	m = AttributeDict()
	mag = pymagic.Magic(*args,**kwargs)
	m.update(mag.__dict__)
	for func in HOOKED:
		m[func]=apply_hooks(getattr(mag,func))
	yield m
	mag.close()

def newmagic(*args,**kwargs):
	m = AttributeDict()
	mag = pymagic.Magic(*args,**kwargs)
	m.update(mag.__dict__)
	for func in HOOKED:
		m[func]=apply_hooks(getattr(mag,func))
	return m

