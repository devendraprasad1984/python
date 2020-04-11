"""
Like several other scripting languages, Python parses the outer level of each module as normal code.
Un-indented assignment statements, expressions, and even loops and conditionals will execute as the module is imported.
This presents an excellent opportunity to supplement a module’s classes and functions with constants and
data structures that callers will find useful — but also offers dangerous temptations: mutable global objects can wind up
coupling distant code, and I/O operations impose import-time expense and side effects.
"""



# The Constant Pattern¶
January = 1                   # calendar.py
WARNING = 30                  # logging.py
MAX_INTERPOLATION_DEPTH = 10  # configparser.py
SSL_HANDSHAKE_TIMEOUT = 60.0  # asyncio.constants.py
TICK = "'"                    # email.utils.py
CRLF = "\r\n"                 # smtplib.py

# Remember that these are “constants” only in the sense that the objects themselves are immutable. The names can still be reassigned.
import calendar
calendar.January = 13
print(calendar.January)

# Import-time computation¶
# zipfile.py
ZIP_FILECOUNT_LIMIT = (1 << 16) - 1
# encoder.py
INFINITY = float('inf')
# shutil.py
COPY_BUFSIZE = 1024 * 1024 if _WINDOWS else 16 * 1024

# My favorite example of computed constants in the Standard Library is the types module. I had always assumed it was implemented in C, to gain special access to built-in type objects like FunctionType and LambdaType that are defined by the language implementation itself.
# types.py
def _f(): pass
FunctionType = type(_f)


# Dunder Constants¶ eg __name__ & __file__
here = os.path.dirname(__file__)
# but use pkgutil.get_data() instead
# bz2.py
__author__ = "Nadeem Vawda <nadeem.vawda@gmail.com>"
# inspect.py
__author__ = ('Ka-Ping Yee <ping@lfw.org>','Yury Selivanov <yselivanov@sprymix.com>')


# The Global Object Pattern¶
# In the full-fledged Global Object pattern, as in the Constant pattern, a module instantiates an object at import time and assigns it a name in the module’s global scope
# The simplest Global Objects are immutable. A common example is a compiled regular expression

escapesre = re.compile(r'[\\"]')       # email/utils.py
magic_check = re.compile('([*?[])')    # glob.py
commentclose = re.compile(r'--\s*>')   # html/parser.py
HAS_UTF8 = re.compile(b'[\x80-\xff]')  # json/encoder.py

# Global Objects that are mutable? eg
import os
os.environ['TERM'] = 'xterm'


# Import-time I/O - Many of the worst Global Objects are those that perform file or network I/O at import time.






