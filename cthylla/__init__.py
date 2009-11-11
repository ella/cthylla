
VERSION = (0, 1)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

from cthylla.config import get_buildmaster_config
