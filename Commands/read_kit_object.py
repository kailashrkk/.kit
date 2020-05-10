import hashlib
import zlib

from Objects.repository import make_and_get_repo_folder_path
from Objects.internal_objects.KitBlob import KitBlob

def read_object(repo, sha):
	"""
	Read object that is assigned by that sha in the objects folder
	"""

	path = make_and_get_repo_folder_path(repo, 'objects', sha[0:2], sha[2:])

	with open(path, 'rb') as f:
		raw_file = zlib.decompress(f.read())

		x = raw_file.find(b' ')
		obj = raw_file[0:x]

		y = raw_file.find(b'\x00', x)
		counted_length = int(raw_file[x:y].decode('ascii'))
		if counted_length != len(raw_file) - y - 1:
			raise Exception(f"Malformed sha passed to function {sha}")

		object_type = obj.decode('ascii')

		if object_type == 'blob':
			return KitBlob(repo, raw_file[y+1:])
		elif object_type == 'commit':
			return KitCommit(repo, raw_file[y+1:])
		elif object_type == 'tag':
			return KitTag(repo, raw_file[y+1:])
		elif object_type == 'tree':
			return KitTree(repo, raw_file[y+1:])
		else:
			raise Exception(f"Unknown object of type {object_type}")