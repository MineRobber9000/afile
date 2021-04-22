from functools import update_wrapper
class HookedFunction:
	def __init__(self,func):
		update_wrapper(self,func)
		self.__function__ = func
		self.__pre_hooks__ = []
		self.__post_hooks__ = []
	def __call__(self,*args,**kwargs):
		for f in self.__pre_hooks__:
			args, kwargs = f(self.__function__,args,kwargs)
		ret = self.__function__(*args,**kwargs)
		for f in self.__post_hooks__:
			rv = f(self.__function__,args,kwargs,ret)
			if rv is not None:
				ret = rv
		return ret
	def add_hook(self,func,pre=False):
		if pre:
			self.__pre_hooks__.append(func)
		else:
			self.__post_hooks__.append(func)
	def clear_hooks(self):
		self.__pre_hooks__ = []
		self.__post_hooks__ = []
	def hook(self,pre=False):
		def _add_hook(func):
			self.add_hook(func,pre)
		return _add_hook

def hooked(func):
	return HookedFunction(func)
