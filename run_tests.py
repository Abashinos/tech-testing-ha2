#!/usr/bin/env python2

import sys
import unittest
from tests.func_tests import FuncTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(FuncTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())