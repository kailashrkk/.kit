from Commands.write_kit_object import write_object
from Objects.internal_objects.KitBlob import KitBlob


def object_hash(obj, type, repo=None):
	data = obj.read()

	if type == b'blob':
		new_obj = KitBlob(repo, data)
	else:
		raise Exception(f"Object of type {type} not found")

	return write_object(new_obj)