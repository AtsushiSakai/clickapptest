
# for common module use in other python scripts.
try:  # for pip package
    from clickapptest.lib.common import common
except ModuleNotFoundError:  # for local call
    from lib.common import common
