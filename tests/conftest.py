import sys
from os.path import dirname
from os.path import abspath, join

tests_dir = dirname(abspath(__file__))
root_dir = dirname(abspath(tests_dir + "/../src/src"))
sys.path.append(root_dir)
