import os
import configparser

from Objects.repository import *


def repo_create(path):
	"""
	Create a new repo at the specified path
	"""
	repo = Repository(path, force = True)

	#validations
	if os.path.exists(repo.worktree):
		if not os.path.isdir(repo.worktree):
			raise Exception("Kit worktree is not a directory")

		if os.path.isdir(repo.internalDir):
			raise Exception("Kit already a repository")
	else:
		os.makedirs(repo.worktree)

	assert(make_repo_folder_dir(repo, "branches", mkdir=True))
	assert(make_repo_folder_dir(repo, "objects", mkdir=True))
	assert(make_repo_folder_dir(repo, "refs", "tags", mkdir=True))
	assert(make_repo_folder_dir(repo, "refs", "heads", mkdir=True))

	with open(make_and_get_repo_folder_path(repo, "description"), "w") as f:
		f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

	# .git/HEAD
	with open(make_and_get_repo_folder_path(repo, "HEAD"), "w") as f:
		f.write("ref: refs/heads/master\n")

	with open(make_and_get_repo_folder_path(repo, "config"), "w") as f:
		config = create_repo_default_config()
		config.write(f)

	return repo

def create_repo_default_config():
	ret = configparser.ConfigParser()

	ret.add_section("core")
	ret.set("core", "repositoryformatversion", "0")
	ret.set("core", "filemode", "false")
	ret.set("core", "bare", "false")

	return ret