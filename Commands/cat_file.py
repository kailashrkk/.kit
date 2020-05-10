import sys

from Commands.read_kit_object import read_object
from Commands.find_object import object_find

def cat_file(repo, object, fmt=None):
	obj = read_object(repo, object_find(repo, object, fmt=fmt))
	sys.stdout.buffer.write(obj.serialize())
