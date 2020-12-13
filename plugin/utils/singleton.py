"""Singleton related stuff. Should only be imported ONCE."""


def singleton(class_):
    """Singleton class wrapper.

    Args:
      class_ (Class): Class to wrap.

    Returns:
      class_: unique instance of object.
    """
    instances = {}

    def getinstance(*args, **kwargs):
        """Get instance of a class."""
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


# ALL the singletons used throughout the codebase go below this line:
##############################################################################
##############################################################################
##############################################################################


@singleton
class ViewConfigCache(dict):
    """Singleton for view configurations cache."""


@singleton
class CppPropertiesCache(dict):
    """Singleton for CppProperties.json file cache."""


@singleton
class CCppPropertiesCache(dict):
    """Singleton for c_cpp_properties.json file cache."""


@singleton
class CMakeFileCache(dict):
    """Singleton for CMakeLists.txt file cache."""


@singleton
class MakefileCache(dict):
    """Singleton for Makefile file cache."""


@singleton
class ComplationDbCache(dict):
    """Singleton for compilation database cache."""


@singleton
class ThreadCache(dict):
    """Singleton for a cache of running threads."""


@singleton
class FlagsFileCache(dict):
    """Singleton for .clang_fomplete file cache."""


def clear_all_caches():
    """Clear all existing caches."""
    CCppPropertiesCache().clear()
    CMakeFileCache().clear()
    MakefileCache().clear()
    ComplationDbCache().clear()
    CppPropertiesCache().clear()
    FlagsFileCache().clear()
    ViewConfigCache().clear()
    ThreadCache().clear()
