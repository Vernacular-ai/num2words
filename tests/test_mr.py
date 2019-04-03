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


class Num2WordsMRTest(TestCase):
    def test_cardinal(self):
        lang_code = "mr"
        items = [
            (72, "बाहत्तर"),
            (200, "दोन शंभर"),
            (202, "दोन शे दोन"),
            (2019, "दोन हजार एकोणीस"),
            # TODO: This is incorrect, the right way to say this is शंभर कोटी
            #       but we will keep this form for now
            (1000000000, "एक शे कोटी")
        ]

        for num, word in items:
            self.assertEqual(num2words(num, lang=lang_code), word)
