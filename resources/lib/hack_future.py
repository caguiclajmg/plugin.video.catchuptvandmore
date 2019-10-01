from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import sys

from future.utils import PY3


# Harmless renames that we can insert.
# These modules need names from elsewhere being added to them:
#   subprocess: should provide getoutput and other fns from commands
#               module but these fns are missing: getstatus, mk2arg,
#               mkarg
#   re:         needs an ASCII constant that works compatibly with Py3

# etc: see lib2to3/fixes/fix_imports.py

# (New module name, new object name, old module name, old object name)
MOVES = [('collections', 'UserList', 'UserList', 'UserList'),
         ('collections', 'UserDict', 'UserDict', 'UserDict'),
         ('collections', 'UserString','UserString', 'UserString'),
         ('collections', 'ChainMap', 'future.backports.misc', 'ChainMap'),
         ('itertools', 'filterfalse','itertools', 'ifilterfalse'),
         ('itertools', 'zip_longest','itertools', 'izip_longest'),
         ('sys', 'intern','__builtin__', 'intern'),
         # The re module has no ASCII flag in Py2, but this is the default.
         # Set re.ASCII to a zero constant. stat.ST_MODE just happens to be one
         # (and it exists on Py2.6+).
         ('re', 'ASCII','stat', 'ST_MODE'),
         ('base64', 'encodebytes','base64', 'encodestring'),
         ('base64', 'decodebytes','base64', 'decodestring'),
         ('subprocess', 'getoutput', 'commands', 'getoutput'),
         ('subprocess', 'getstatusoutput', 'commands', 'getstatusoutput'),
         ('subprocess', 'check_output', 'future.backports.misc', 'check_output'),
         ('math', 'ceil', 'future.backports.misc', 'ceil'),
         ('collections', 'OrderedDict', 'future.backports.misc', 'OrderedDict'),
         ('collections', 'Counter', 'future.backports.misc', 'Counter'),
         ('collections', 'ChainMap', 'future.backports.misc', 'ChainMap'),
         ('itertools', 'count', 'future.backports.misc', 'count'),
         ('reprlib', 'recursive_repr', 'future.backports.misc', 'recursive_repr'),
         ('functools', 'cmp_to_key', 'future.backports.misc', 'cmp_to_key'),

# This is no use, since "import urllib.request" etc. still fails:
#          ('urllib', 'error', 'future.moves.urllib', 'error'),
#          ('urllib', 'parse', 'future.moves.urllib', 'parse'),
#          ('urllib', 'request', 'future.moves.urllib', 'request'),
#          ('urllib', 'response', 'future.moves.urllib', 'response'),
#          ('urllib', 'robotparser', 'future.moves.urllib', 'robotparser'),
]


def install_aliases():
    """
    Monkey-patches the standard library in Py2.6/7 to provide
    aliases for better Py3 compatibility.
    """
    if PY3:
        return
    # if hasattr(install_aliases, 'run_already'):
    #     return
    for (newmodname, newobjname, oldmodname, oldobjname) in MOVES:
        __import__(newmodname)
        # We look up the module in sys.modules because __import__ just returns the
        # top-level package:
        newmod = sys.modules[newmodname]
        # newmod.__future_module__ = True

        __import__(oldmodname)
        oldmod = sys.modules[oldmodname]

        obj = getattr(oldmod, oldobjname)
        setattr(newmod, newobjname, obj)

    # Hack for urllib so it appears to have the same structure on Py2 as on Py3
    

    """
    # We disable this block because of a bug with urllib that cause error on Youtube-DL
    # see: https://github.com/ytdl-org/youtube-dl/issues/17974 for more information

    import urllib
    from future.backports.urllib import request
    from future.backports.urllib import response
    from future.backports.urllib import parse
    from future.backports.urllib import error
    from future.backports.urllib import robotparser
    urllib.request = request
    urllib.response = response
    urllib.parse = parse
    urllib.error = error
    urllib.robotparser = robotparser
    sys.modules['urllib.request'] = request
    sys.modules['urllib.response'] = response
    sys.modules['urllib.parse'] = parse
    sys.modules['urllib.error'] = error
    sys.modules['urllib.robotparser'] = robotparser
    """

    # Instead we use this to support Python 2 AND python 3
    try:
        from urllib.parse import urlparse, urlencode
        from urllib.request import urlopen, Request
        from urllib.error import HTTPError
    except ImportError:
        from urlparse import urlparse
        from urllib import urlencode
        from urllib2 import urlopen, Request, HTTPError

    # Patch the test module so it appears to have the same structure on Py2 as on Py3
    try:
        import test
    except ImportError:
        pass
    try:
        from future.moves.test import support
    except ImportError:
        pass
    else:
        test.support = support
        sys.modules['test.support'] = support

    # Patch the dbm module so it appears to have the same structure on Py2 as on Py3
    try:
        import dbm
    except ImportError:
        pass
    else:
        from future.moves.dbm import dumb
        dbm.dumb = dumb
        sys.modules['dbm.dumb'] = dumb
        try:
            from future.moves.dbm import gnu
        except ImportError:
            pass
        else:
            dbm.gnu = gnu
            sys.modules['dbm.gnu'] = gnu
        try:
            from future.moves.dbm import ndbm
        except ImportError:
            pass
        else:
            dbm.ndbm = ndbm
            sys.modules['dbm.ndbm'] = ndbm

    # install_aliases.run_already = True