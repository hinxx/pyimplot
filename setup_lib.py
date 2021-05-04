import sys
import os
import shutil
try:
    from setuptools import setup, distutils, Extension
except ImportError:
    sys.exit('setuptools was not detected - please install setuptools and pip')
from distutils import unixccompiler
from distutils.log import set_verbosity
# from distutils.sysconfig import get_config_vars, get_config_var
from distutils.util import get_platform

# from solar_utils import __version__ as VERSION, __name__ as NAME
# from solar_utils.tests import test_cdlls
# import logging

# logging.basicConfig(level=logging.DEBUG)
# LOGGER = logging.getLogger('SETUP')

# from pprint import pprint
# pprint(get_config_vars())

set_verbosity(3)
# build_base = 'build'
# plat_name = get_platform()
# plat_specifier = ".%s-%d.%d" % (plat_name, *sys.version_info[:2])
# build_platlib = os.path.join(build_base, 'temp' + plat_specifier)

LIB_NAME = 'implot'
SRC_DIR = 'implot-cpp'
# BUILD_DIR = build_platlib
# DEST_DIR = os.path.join(NAME, '.libs')

# set platform constants
CCFLAGS, RPATH, INSTALL_NAME, LDFLAGS, MACROS = None, None, None, None, None
PYVERSION = sys.version_info
PLATFORM = sys.platform
if PLATFORM == 'win32':
    LIB_FILE = '%s.dll'
    MACROS = [('WIN32', None)]
    if PYVERSION.major >= 3 and PYVERSION.minor >= 5:
        LDFLAGS = ['/DLL']
elif PLATFORM == 'darwin':
    LIB_FILE = 'lib%s.dylib'
    RPATH = "-Wl,-rpath,@loader_path/"
    INSTALL_NAME = "@rpath/" + LIB_FILE
    CCFLAGS = LDFLAGS = ['-fPIC']
elif PLATFORM in ['linux', 'linux2']:
    PLATFORM = 'linux'
    LIB_FILE = 'lib%s.so'
    # RPATH = "-Wl,-rpath,$ORIGIN/data"
    RPATH = ''
    CCFLAGS = ['-fPIC', '-pthread', '-Wno-unused-result', '-Wsign-compare',
               '-DNDEBUG', '-g', '-fwrapv', '-O3', '-Wall']
    # MACROS = [('IMGUI_USER_CONFIG', '"../config-cpp/imconfig.h"')]
    LDFLAGS = ['-fPIC', '-pthread']
else:
    sys.exit('Platform "%s" is unknown or unsupported.' % PLATFORM)

sources = [
        'implot.cpp',
        'implot_items.cpp',
        'implot_demo.cpp',
       ]
sources = [os.path.join(SRC_DIR, x) for x in sources]
# LIB_NAME = NAME
# LIB_FILE = LIB_FILE % NAME
# LIB_PATH = os.path.join(DEST_DIR, LIB_FILE)

# print("SRCS", SRCS)
# print("LIB_FILE", LIB_FILE)
# # print("LIB_PATH", LIB_PATH)
# print("CCFLAGS", CCFLAGS)
# print("LDFLAGS", LDFLAGS)

lib_filename = LIB_FILE % LIB_NAME

def make_ldflags(ldflags=LDFLAGS, rpath=RPATH):
    """
    Make LDFLAGS with rpath, install_name and lib_name.
    """
    if ldflags and rpath:
        ldflags.extend([rpath])
    elif rpath:
        ldflags = [rpath]
    return ldflags


def make_install_name(lib_name, install_name=INSTALL_NAME):
    """
    Make INSTALL_NAME with and lib_name.
    """
    if install_name:
        return ['-install_name', install_name % lib_name]
    else:
        return None


def dylib_monkeypatch(self):
    """
    Monkey patch :class:`distutils.UnixCCompiler` for darwin so libraries use
    '.dylib' instead of '.so'.
    """
    def link_dylib_lib(self, objects, output_libname, output_dir=None,
                       libraries=None, library_dirs=None,
                       runtime_library_dirs=None, export_symbols=None,
                       debug=0, extra_preargs=None, extra_postargs=None,
                       build_temp=None, target_lang=None):
        """implementation of link_shared_lib"""
        self.link("shared_library", objects,
                  self.library_filename(output_libname, lib_type='dylib'),
                  output_dir,
                  libraries, library_dirs, runtime_library_dirs,
                  export_symbols, debug,
                  extra_preargs, extra_postargs, build_temp, target_lang)
    self.link_so = self.link_shared_lib
    self.link_shared_lib = link_dylib_lib
    return self


def imgui_location(subdir=None):
    imgui_path = ''
    try:
        import imgui
    except ImportError:
        print('pyimgui module is required to build pyimplot')
        exit(1)
    finally:
        imgui_path = imgui.__path__[0]
        print(imgui_path)
    if subdir is not None:
        imgui_path = os.path.join(imgui_path, subdir)
    return imgui_path


def clean(dest_lib):
    lib_fullpath = os.path.join(dest_dir, lib_filename)
    if os.path.exists(lib_fullpath):
        os.remove(lib_fullpath)


def build(dest_dir, temp_dir):
    lib_fullpath = os.path.join(dest_dir, lib_filename)

    print("lib_filename", lib_filename)
    print("lib_fullpath", lib_fullpath)
    print("sources", sources)
    print("CCFLAGS", CCFLAGS)
    print("LDFLAGS", LDFLAGS)

    if os.path.exists(lib_fullpath):
        return

    # clean build directory
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    if PLATFORM == 'darwin':
        CCOMPILER = unixccompiler.UnixCCompiler
        OSXCCOMPILER = dylib_monkeypatch(CCOMPILER)
        CC = OSXCCOMPILER(verbose=3)
    else:
        CC = distutils.ccompiler.new_compiler()

    CC.add_include_dir(SRC_DIR)
    CC.add_include_dir(imgui_location('../imgui.data'))

    # compile sources
    OBJS = CC.compile(sources,
                      output_dir=temp_dir,
                      extra_preargs=CCFLAGS,
                      macros=MACROS
                     )

    CC.add_library('imgui')
    CC.add_library_dir(imgui_location('../imgui.data'))

    # link library
    CC.link_shared_lib(OBJS,
                       LIB_NAME,
                       output_dir=dest_dir,
                       extra_preargs=make_ldflags(),
                       extra_postargs=make_install_name(LIB_NAME)
                      )

    # copy headers to destination directory
    for hdr in ['implot.h', 'implot_internal.h']:
        header_file = os.path.join(SRC_DIR, hdr)
        shutil.copy(header_file, dest_dir)


def sdist():
    pass
    # for plat in ('win32', 'linux', 'darwin'):
    #     PKG_DATA.append('%s.mk' % plat)
    # PKG_DATA.append(os.path.join('src', '*.*'))
    # PKG_DATA.append(os.path.join('src', 'orig', 'solpos', '*.*'))
    # PKG_DATA.append(os.path.join('src', 'orig', 'spectrl2', '*.*'))
