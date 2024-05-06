
from . import utils
from . import runner
import sys
__version__ = '0.1.3.0'
from jittor import LOG
import os
dirname = os.path.dirname(__file__)
LOG.i(f"JNeRF({__version__}) at {dirname}")
assert sys.platform in ["linux", "win32"], "MacOS is not supported yet, everyone is welcome to contribute to this"

sp_char = ' "\''
for char in sp_char:
    assert char not in dirname, f"Special char '{char}' detect in '{dirname}', please change jnerf to another directory and reinstall it."
