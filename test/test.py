import afile.magic as magic
import basicb

with magic.magic(flags=magic.MAGIC_MIME_TYPE) as m:
	print(m.id_filename("basicb.py"))
