import os
from Objects.repository import Repository

def find_repo(path='.', required=True):
	path = os.path.realpath(path)

	if os.path.isdir(path):
		return Repository(path)

	parent = os.path.realpath(os.path.join(path, '..'))

	if parent == path:
		if required:
			raise Exception("No kit internal dir found, try init")
		else:
			return None
	
	return find_repo(parent, required)