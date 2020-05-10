#cli
import argparse
#for ordereddict
import collections
#for parsing config files
import configparser
#for sha1, used by git extensively
import hashlib
#for path and other os related methods
import os
#for simple regex
import re
#for reading cli arguments
import sys
#for compressing
import zlib

from Commands.create_repository import repo_create
from Commands.find_repository import find_repo
from Objects.repository import Repository
from Commands.cat_file import cat_file
from Commands.hash_object import object_hash

argparser = argparse.ArgumentParser('This is a git clone thingy')
argsubparsers = argparser.add_subparsers(title='Commands', dest='command')
argsubparsers.required = True


def setup():
	#setup cli commands with arguments
	#init command
	argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
	argsp.add_argument("path",
               metavar="directory",
               nargs="?",
               default=".",
               help="Where to create the repository.")
	#add command
	argsp = argsubparsers.add_parser("add", help="Add changes to work tree.")
	argsp.add_argument("path",
               metavar="directory",
               nargs="?",
               default=".",
               help="Which files to add to the work tree.")

	argsp = argsubparsers.add_parser('cat-file', help='Content of repo objects')

	argsp.add_argument('type',
               choices=['blob', 'commit', 'tag', 'tree'],
               help='type of object to be inserted.'
               )

	argsp.add_argument('object',
				metavar='object',
				help='The object to display.'
				)

	argsp = argsubparsers.add_parser(
    "hash-object",
    help="Compute object ID and optionally creates a blob from a file")

	argsp.add_argument("-t",
	                   metavar="type",
	                   dest="type",
	                   choices=["blob", "commit", "tag", "tree"],
	                   default="blob",
	                   help="Specify the type")

	argsp.add_argument("-w",
	                   dest="write",
	                   action="store_true",
	                   help="Actually write the object into the database")

	argsp.add_argument("path",
                   help="Read object from <file>")


def main(argv=sys.argv[1:]):
	args = argparser.parse_args(argv)
	if args.command == 'init': 
		cmd_init(args)
	elif args.command == 'add':
		cmd_add(args)
	elif args.command == 'cat-file':
		cmd_cat_file(args)
	elif args.command == 'hash-object':
		cmd_hash_object(args)

def cmd_init(args):
	repo_create(args.path)

def cmd_add(args):
	print('in add')
	print(args.path)
	pass

def cmd_cat_file(args):
	repo = find_repo()
	cat_file(repo, args.object, fmt=args.type.encode())

def cmd_hash_object(args):
	if args.write:
		repo = Repository('.')
	else:
		repo = None

	with open(args.path, "rb") as fd:
		sha = object_hash(fd, args.type.encode(), repo)
		print(sha)


