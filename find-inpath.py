#!/usr/bin/env python3
import argparse
import os
import re


arg_parser = argparse.ArgumentParser(description="Find files on the system PATH (or other PATH-like variable) matching the given pattern")
arg_parser.add_argument("name", help="the file name to search for")
arg_parser.add_argument("-r", "--regex", action="store_true", help="interpret 'name' argument as a regular expression")
arg_parser.add_argument("-f", "--fullpath", action="store_true", help="print full file paths")
arg_parser.add_argument("-x", "--executable-only", action="store_true", help="ignore files without execute permissions")
arg_parser.add_argument("-v", "--pathvar", help="environment variable to use for search space", default="PATH")

args = arg_parser.parse_args()

try:
	paths = os.environ[args.pathvar].split(os.pathsep)
except KeyError as e:
	arg_parser.error("environment variable {} not found".format(e))

re_search = re.compile(args.name if args.regex else re.escape(args.name))

#note: searching could be made more efficient (indexing, utilising OS search features, etc)
searched = set()
for path in reversed(paths):
	#ignore paths that have already been searched
	if path not in searched:
		searched.add(path)
	else:
		continue
	
	for directory, _, files in os.walk(path):
		for file_name in files:
			if re_search.search(file_name):
				if args.fullpath or args.executable_only:
					file_path = os.path.join(directory, file_name)
				
				if args.executable_only and not os.access(file_path, os.X_OK):
					continue
					
				print(file_path if args.fullpath else file_name)