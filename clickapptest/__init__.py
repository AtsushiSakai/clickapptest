
# for common module use in other python scripts.
try:  # for pip package
    from clickapptest.common import common
except ModuleNotFoundError:  # for local call
    from common import common
