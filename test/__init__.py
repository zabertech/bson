#!/usr/bin/env python
import doctest
import os
import sys
import unittest


here = os.path.dirname(__file__)


def test_suite():
    suite = additional_tests()
    loader = unittest.TestLoader()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = "test." + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTests(loader.loadTestsFromModule(module))
    return suite


def additional_tests():
    import zaber_bson
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(zaber_bson))
    return suite


def main():
    sys.path.insert(0,
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(
                                os.path.abspath(__file__)))))
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
