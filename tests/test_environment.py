import sys


def test_python_version():
    assert sys.version_info[:2] == (3, 10)


def test_common_dependencies():
    import numpy
    import pandas
    import sklearn