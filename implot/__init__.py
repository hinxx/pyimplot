# -*- coding: utf-8 -*-
VERSION = (0, 1, 0)  # PEP 386
__version__ = ".".join([str(x) for x in VERSION])

import implot.__config__

#from imgui.core import *  # noqa
#from imgui import core
#from imgui.extra import *  # noqa
#from imgui import extra
#from imgui import _compat
#from imgui import internal
from implot.plot import *  # noqa
from implot import plot
