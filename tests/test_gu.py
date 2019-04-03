# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words


class Num2WordsGUTest(TestCase):
    def test_cardinal(self):
        lang_code = "gu"
        items = [
            (72, "બોતેર"),
            (100, "સો"),
            (179, "એક સો ઓગણાએંસી"),
            (200, "બે સો"),
            (202, "બે સો બે"),
            (523, "પાંચ સો તેવીસ"),
            (729, "સાત સો ઓગણત્રીસ"),
            (1000, "એક હજાર"),
            (1111, "એક હજાર એક સો અગિયાર"),
            (1072, "એક હજાર બોતેર"),
            (2019, "બે હજાર ઓગણિસ"),
            (10000, "દસ હજાર")
        ]
        skipped_items = [
            (1000000000, "સો કરોડ઼")
        ]

        for num, word in items:
            self.assertEqual(num2words(num, lang=lang_code), word)
