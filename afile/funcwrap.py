from functools import wraps
def funcwrap(pre,post):
	def _call_hooks(func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			for f in pre:
				f(func,args,kwargs)
			ret = func(*args,**kwargs)
			for f in post:
				rv = f(func,args,kwargs,ret)
				if rv is not None:
					ret = rv
			return ret
		return wrapper
	return _call_hooks
