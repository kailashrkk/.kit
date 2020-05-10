

class KitObject(object):
	"""
	Base object for all internal kit objects,
	ex: all blobs, commits, tags base objects will subclass from this object
	"""
	repo = None

	def __init__(self, repo, data=None):
		self.repo = repo

		if data:
			self.deserialize(data)

	def serialize(self):
		raise Exception("Unimplemented Error")

	def deserialize(self, data):
		raise Exception("Unimplemented Error")