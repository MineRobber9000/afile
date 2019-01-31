import afile.magic as magic

def post_hook(func,args,kwargs,ret):
#	return "{}({},{}) == {!r}".format(func.__name__,",".join([repr(x) for x in args]),",".join(["{}={!r}".format(k,kwargs[k]) for k in kwargs]),ret)
	return "{}: {}".format(args[0],ret)

magic.add_hook("id_filename",post_hook)
