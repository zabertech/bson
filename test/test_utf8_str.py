#!/usr/bin/env python
from unittest import TestCase

from zaber_bson import dumps, loads


class TestUtf8Str(TestCase):
    def setUp(self):
        self.doc = {
            '😍': '무지개',
            '😅': '驴',
        }

    def test_utf8_str(self):
        dump = dumps(self.doc)
        decoded = loads(dump)
        self.assertEqual(decoded, self.doc)
