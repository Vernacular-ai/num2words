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


class Num2WordsTATest(TestCase):
    def test_cardinal(self):
        lang_code = "ta"
        items = [
            (2, "இரண்டு"),
            (7, "ஏழு"),
            (8, "எட்டு"),
            (20, "இருபது"),
            (22, "இருபத்து இரண்டு"),
            (24, "இருபத்து நான்கு"),
            (50, "ஐம்பது"),
            (60, "அறுபது"),
            (70, "எழுபது"),
            (80, "எண்பது"),
            (82, "எண்பத்திரண்டு")
        ]
        # NOTE: Since we don't have rules to go beyond 100 as of now, we are
        # skipping the following cases
        skipped_items = [
            (200, "இருநூறு"),
            (600, "அறுநூறு"),
            (700, "எழுநூறு"),
            (1000, "ஆயிரம்"),
            (2000, "இரண்டாயிரம்"),
            (6000, "ஆறாயிரம்"),
            (7000, "ஏழாயிரம்"),
            (8000, "எட்டாயிரம்"),
            (100000, "லட்சம்")
        ]

        for num, word in items:
            self.assertEqual(num2words(num, lang=lang_code), word)
