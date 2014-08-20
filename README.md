sphinxapi-py3
=============

Python 3 port of official python client for Sphinx Search http://sphinxsearch.com/

### Porting notes / reliability

Initially base sphinxapi.py was processed by 2to3 and then a bunch of manual modifications was made.
Most of them are concerned with unicode/bytes issues (and they are the most important) and there're also some PEP8/cosmetical ones and minor optimizations.

This lib is now used in several projects and may be considered as quite stable as most of the bugs are already caught. Feel free to report if you'll face some new issues.

### Installation

```sh
pip install https://github.com/a1tus/sphinxapi-py3/zipball/master
```

### Using

```sh
import sphinxapi
```

### Current version

* Sphinx 2.1.9-release
* sphinxapi.py 4505 2014-01-22 15:16:21Z

It's the last available version at the moment. I'm trying to keep it up-to-date but if you know about some newer version (which is basically distributed with sphinx source code) please let me know.

### Official documentation

http://sphinxsearch.com/docs/
