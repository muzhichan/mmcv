import sys
import os

root_dir = os.path.dirname(__file__)
sys.path.insert(0, root_dir)

from tests.test_utils.test_config import mz_test_fromfile


if __name__ == '__main__':
    mz_test_fromfile()
