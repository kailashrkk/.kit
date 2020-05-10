
from Objects.kit_object import KitObject

class KitBlob(KitObject):

	fmt = b'blob'

	def serialize(self):
		return self.blobdata

	def deserialize(self, data):
		self.blobdata =  data
