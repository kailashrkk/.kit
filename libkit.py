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


def main(argv=sys.argv[1:]):
	args = argparser.parse_args(argv)
	if args.command == 'init': 
		cmd_init(args)
	elif args.command == 'add':
		cmd_add(args)

def cmd_init(args):
	repo_create(args.path)

def cmd_add(args):
	print('in add')
	print(args.path)
	pass

