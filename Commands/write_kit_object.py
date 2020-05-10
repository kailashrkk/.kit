import zlib
import hashlib

from Objects.repository import *

def write_object(object, force_write=True):

	data = object.serialize()
	#add header, example: objecttype length data
	total = object.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
	#compute hash
	sha = hashlib.sha1(total).hexdigest()

	if force_write:
		path = make_and_get_repo_folder_path(object.repo, 'objects', sha[0:2], sha[2:], mkdir=force_write)

		with open(path, 'wb') as f:
			f.write(zlib.compress(total))

	return sha