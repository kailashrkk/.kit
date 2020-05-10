import os
import configparser

class Repository(object):
	"""A Repository object for the directory we need to keep track of"
		worktree: dir we are keeping track of
		internalDir: .kit internal directory
		conf: i wanna say config file, dunno what this is for yet :TODO

	"""
	worktree = None
	internalDir = None
	conf = None

	def __init__(self, path, force=False):
		super(Repository, self).__init__()
		self.worktree = path
		self.internalDir = os.path.join(path, '.kit')

		if not (force or os.path.isdir(self.internalDir)):
			raise Exception(f"{self.path} is not a kit directory")

		#read config
		self.conf = configparser.ConfigParser()
		cf = make_and_get_repo_folder_path(self, "config")
		if cf and os.path.exists(cf):
			self.conf.read([cf])
		elif not force:
			raise Exception("There needs to be a config file bruh")

		#check config file versions, has to be 0 at all times
		if not force:
			version = int(self.conf.get("core", "repositoryformatversion"))
			if version != 0:
				raise Exception(f"Unsupported repositoryformatversion {version}")


def get_full_repo_path(repo, *path):
	"""
	Helper function to make a full repo path for some internal files in the .kit directory
	"""
	return os.path.join(repo.internalDir, *path)

def make_and_get_repo_folder_path(repo, *path, mkdir=False):
	"""
	Helper function to make a file repo path for some internal directories in the .kit directory 
	"""
	if make_repo_folder_dir(repo, *path[:-1], mkdir=mkdir):
		return get_full_repo_path(repo, *path)

def make_repo_folder_dir(repo, *path, mkdir=False):
	"""
	Helper function to make a repo dir and return path
	"""
	full_path = get_full_repo_path(repo, *path)

	if os.path.exists(full_path):
		if os.path.isdir(full_path):
			return full_path
		else:
			raise Exception(f"{path} is not a directory")

	if mkdir:
		os.makedirs(full_path)
		return full_path
	else:
		return None