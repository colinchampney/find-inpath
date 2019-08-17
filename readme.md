# find-inpath.py
A tiny, OS-independent Python utility for finding files contained in directories on the system PATH (or any PATH-like environment variable, e.g. "PYTHONPATH" or "JAVA_PATH").

## Usage
```
usage: find-inpath.py [-h] [-r] [-f] [-x] [-v PATHVAR] name

Find files on the system PATH (or other PATH-like variable) matching the given
pattern

positional arguments:
  name                  the file name to search for

optional arguments:
  -h, --help            show this help message and exit
  -r, --regex           interpret 'name' argument as a regular expression
  -f, --fullpath        print full file paths
  -x, --executable-only
                        ignore files without execute permissions
  -v PATHVAR, --pathvar PATHVAR
                        environment variable to use for search space
```
